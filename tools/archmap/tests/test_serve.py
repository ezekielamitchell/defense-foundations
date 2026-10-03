import http.client
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import Mock
from support import ROOT,ART
import serve

class ServerTests(unittest.TestCase):
    def setUp(self):
        self.state=Mock(token='secret');self.state.current.return_value={'meta':{'rev':3}}
        self.server=serve.Server(('127.0.0.1',0),self.state);self.port=self.server.server_address[1]
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
    def tearDown(self):self.server.shutdown();self.server.server_close()
    def request(self,path='/',method='GET',headers=None):
        conn=http.client.HTTPConnection('127.0.0.1',self.port,timeout=3);conn.request(method,path,headers=headers or {});r=conn.getresponse();result=(r.status,dict(r.getheaders()),r.read());conn.close();return result
    def test_loopback_only(self):
        with self.assertRaises(ValueError):serve.Server(('0.0.0.0',0),self.state)
        self.assertEqual(self.server.server_address[0],'127.0.0.1')
    def test_bad_host_and_no_cors(self):
        code,headers,_=self.request('/api/model',headers={'Host':'evil.example'});self.assertEqual(code,403);self.assertNotIn('Access-Control-Allow-Origin',headers)
        self.assertEqual(self.request('/api/model',headers={'Host':'localhost:'+str(self.port)})[0],200)
    def test_token_guard(self):
        self.assertEqual(self.request('/api/run-checks','POST')[0],403)
        self.assertEqual(self.request('/api/run-checks','POST',{'X-Archmap-Token':'wrong'})[0],403)
        self.state.request_checks.assert_not_called()
        self.assertEqual(self.request('/api/run-checks','POST',{'X-Archmap-Token':'secret'})[0],202)
        self.state.request_checks.assert_called_once()
    def test_unknown_and_traversal(self):
        for path in ['/README.md','/../AGENTS.md','/%2e%2e/AGENTS.md','/api/model?path=README.md','/favicon.ico']:
            self.assertEqual(self.request(path)[0],404,path)
        self.assertEqual(self.request('/unknown','POST')[0],404)
    def test_cross_origin_post_rejected(self):
        self.assertEqual(self.request('/api/run-checks','POST',{'X-Archmap-Token':'secret','Origin':'https://evil.example'})[0],403)
    def test_model_json(self):
        code,_,body=self.request('/api/model');self.assertEqual(code,200);self.assertEqual(json.loads(body),{'meta':{'rev':3}})

class WatchTests(unittest.TestCase):
    def test_new_owned_file_and_outside_symlink(self):
        with tempfile.TemporaryDirectory(dir=ART) as d:
            root=Path(d);(root/'tools/archmap').mkdir(parents=True);(root/'progress/proofs').mkdir(parents=True)
            (root/'tools/archmap/curated.json').write_text(json.dumps({'nodes':[{'owns':['progress/proofs/*.json']}]}))
            before=serve.snapshot(root);(root/'progress/proofs/new.json').write_text('{}');after=serve.snapshot(root)
            self.assertNotEqual(before,after);self.assertIn('progress/proofs/new.json',after)
            (root/'progress/proofs/out.json').symlink_to(ROOT/'AGENTS.md');self.assertNotIn('progress/proofs/out.json',serve.snapshot(root))
