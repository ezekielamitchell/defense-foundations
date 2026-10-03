#!/usr/bin/env python3
"""Repository-only watcher and loopback SSE server. No static file serving."""
from __future__ import annotations
import argparse
import copy
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
from pathlib import Path
import queue
import secrets
import sys
import threading
import time
sys.dont_write_bytecode=True
import build
import checks
import diff
import extract
import layout

ROOT=Path(__file__).resolve().parents[2]

def snapshot(root):
    root=Path(root).resolve(); paths={'tools/archmap/curated.json'}
    try:curated=json.loads((root/'tools/archmap/curated.json').read_text())
    except (OSError,ValueError):curated={}
    def walk(value):
        if isinstance(value,dict):
            if 'path' in value and 'anchor' in value:paths.add(value['path'])
            for k,v in value.items():
                if k=='owns':paths.update(extract.owned_files(root,v))
                else:walk(v)
        elif isinstance(value,list):
            for v in value:walk(v)
    walk(curated)
    # New/deleted receipts and validator inputs are watched even when no file exists yet.
    paths.update(p.relative_to(root).as_posix() for p in (root/'progress/proofs').glob('*.json') if p.resolve().is_relative_to(root))
    result={}
    for relative in sorted(paths):
        path=(root/relative).resolve()
        if not path.is_relative_to(root):continue
        try:s=path.stat();result[relative]=(s.st_mtime_ns,s.st_size)
        except OSError:result[relative]=None
    return result

class State:
    def __init__(self,root,watch=True,js=None):
        self.root=Path(root).resolve();self.token=secrets.token_urlsafe(32);self.session=secrets.token_hex(12)
        self.lock=threading.RLock();self.build_lock=threading.Lock();self.closed=threading.Event();self.clients=set();self.checking=False;self.queued=False;self.pending_trigger=[];self.last_scan=checks.now();self.pending=False;self.watch_error=None
        self.results=checks.run(self.root);self.model=layout.apply(extract.extract(self.root,results=self.results));self.js=build.bundle() if js is None else js
        self.thread=None
        if watch:self.thread=threading.Thread(target=self.watch,daemon=True,name='archmap-watch');self.thread.start()
    def current(self):
        with self.lock:return copy.deepcopy(self.model)
    def emit(self,name,data):
        event=(name,data)
        with self.lock:
            for client in list(self.clients):
                try:client.put_nowait(event)
                except queue.Full:
                    # Slow clients reconcile from the latest model, never a partial history.
                    while not client.empty():
                        try:client.get_nowait()
                        except queue.Empty:break
                    client.put_nowait(('reconcile',{'rev':self.model['meta']['rev']}))
    def rebuild(self,trigger):
        with self.build_lock:
            with self.lock:old=copy.deepcopy(self.model);results=copy.deepcopy(self.results)
            try:new=layout.apply(extract.extract(self.root,results=results),old)
            except (OSError,ValueError,KeyError) as exc:
                self.watch_error=checks.redact(str(exc),self.root);self.emit('model-error',{'message':self.watch_error});return
            new['meta']['rev']=old['meta']['rev']+1
            changes=diff.diff(old,new)
            with self.lock:self.model=new;self.watch_error=None;self.pending=False
            self.emit('model-patch',dict(rev=new['meta']['rev'],at=new['meta']['generated'],trigger=trigger,changes=changes,model=new))
    def request_checks(self,trigger=None):
        with self.lock:
            self.pending_trigger=list(trigger or [])
            if self.checking:self.queued=True;return
            self.checking=True
        threading.Thread(target=self.check_worker,daemon=True,name='archmap-checks').start()
    def check_worker(self):
        while not self.closed.is_set():
            with self.lock:trigger=list(self.pending_trigger);self.queued=False
            self.emit('checks-started',{'at':checks.now()})
            results=checks.run(self.root)
            with self.lock:self.results=results
            self.rebuild(trigger)
            self.emit('checks-finished',{'at':checks.now(),'results':results})
            with self.lock:
                if not self.queued:self.checking=False;break
    def watch(self):
        previous=snapshot(self.root);next_poll=time.monotonic()+1;last_change=None;changed=set();check_at=None;check_trigger=[];next_status=time.monotonic()
        while not self.closed.wait(.04):
            now=time.monotonic()
            if now>=next_poll:
                current=snapshot(self.root);next_poll=now+1;self.last_scan=checks.now()
                delta={p for p in previous.keys()|current.keys() if previous.get(p)!=current.get(p)}
                if delta:changed.update(delta);last_change=now;check_at=None;self.pending=True;self.emit('watch-status',self.watch_status())
                previous=current
            if now>=next_status:self.emit('watch-status',self.watch_status());next_status=now+5
            if last_change is not None and now-last_change>=.4:
                trigger=sorted(changed);changed.clear();last_change=None;self.rebuild(trigger);check_trigger=trigger;check_at=time.monotonic()+2
            if check_at is not None and now>=check_at:
                self.request_checks(check_trigger);check_at=None
    def watch_status(self):
        return dict(lastScan=self.last_scan,pending=self.pending,error=self.watch_error,checking=self.checking)
    def close(self):self.closed.set()

class Server(ThreadingHTTPServer):
    daemon_threads=True
    allow_reuse_address=True
    def __init__(self,address,state):
        if address[0]!='127.0.0.1':raise ValueError('Only 127.0.0.1 is permitted')
        self.state=state;super().__init__(address,Handler)

class Handler(BaseHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def log_message(self,*args):pass
    def allowed(self):
        port=self.server.server_address[1]
        if self.headers.get('Host') not in ('127.0.0.1:'+str(port),'localhost:'+str(port)):
            self.respond(403,{'error':'Host rejected'});return False
        return True
    def respond(self,code,body,kind='application/json; charset=utf-8'):
        data=(json.dumps(body,separators=(',',':')) if not isinstance(body,str) else body).encode()
        self.send_response(code);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Referrer-Policy','no-referrer');self.end_headers()
        try:self.wfile.write(data)
        except (BrokenPipeError,ConnectionResetError):pass
    def do_GET(self):
        if not self.allowed():return
        state=self.server.state
        if self.path=='/':
            model=state.current();self.respond(200,build.render(model,live=dict(rev=model['meta']['rev'],token=state.token,session=state.session),js=state.js),'text/html; charset=utf-8')
        elif self.path=='/api/health':self.respond(200,dict(ok=True,rev=state.current()['meta']['rev'],session=state.session,token=state.token,checking=state.checking,watch=state.watch_status()))
        elif self.path=='/api/model':self.respond(200,state.current())
        elif self.path=='/events':self.events()
        else:self.respond(404,{'error':'Not found'})
    def do_POST(self):
        if not self.allowed():return
        if self.path!='/api/run-checks':self.respond(404,{'error':'Not found'});return
        token=self.headers.get('X-Archmap-Token','')
        if not secrets.compare_digest(token,self.server.state.token):self.respond(403,{'error':'Token required'});return
        origin=self.headers.get('Origin')
        if origin and origin!='http://'+self.headers.get('Host',''):self.respond(403,{'error':'Origin rejected'});return
        if self.headers.get('Content-Length','0')!='0':self.respond(400,{'error':'No request body accepted'});self.close_connection=True;return
        self.server.state.request_checks();self.respond(202,{'status':'queued'})
    def events(self):
        self.send_response(200);self.send_header('Content-Type','text/event-stream');self.send_header('Cache-Control','no-cache');self.send_header('Connection','keep-alive');self.end_headers()
        state=self.server.state;client=queue.Queue(maxsize=24)
        with state.lock:state.clients.add(client)
        try:
            self.wfile.write(('event: connected\ndata: '+json.dumps({'rev':state.model['meta']['rev'],'session':state.session})+'\n\n').encode());self.wfile.flush()
            while not state.closed.is_set():
                try:name,data=client.get(timeout=15);payload='event: '+name+'\ndata: '+json.dumps(data,separators=(',',':'))+'\n\n'
                except queue.Empty:payload=': heartbeat\n\n'
                self.wfile.write(payload.encode());self.wfile.flush()
        except (BrokenPipeError,ConnectionResetError,TimeoutError):pass
        finally:
            with state.lock:state.clients.discard(client)

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--port',type=int,default=8765);p.add_argument('--host',default='127.0.0.1');args=p.parse_args()
    if args.host!='127.0.0.1':p.error('Only 127.0.0.1 is permitted')
    state=State(args.root);server=Server((args.host,args.port),state)
    print(json.dumps({'url':'http://127.0.0.1:'+str(server.server_address[1]),'root':str(args.root.resolve()),'status':'ready'}),flush=True)
    try:server.serve_forever(poll_interval=.1)
    except KeyboardInterrupt:pass
    finally:state.close();server.server_close()
if __name__=='__main__':main()
