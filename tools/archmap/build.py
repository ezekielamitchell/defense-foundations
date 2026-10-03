#!/usr/bin/env python3
"""Build an offline single-file map. Generated data and static assets are inline."""
from __future__ import annotations
import argparse
import base64
import copy
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
sys.dont_write_bytecode=True
import extract
import layout

ARCH=Path(__file__).resolve().parent
ROOT=ARCH.parents[1]

def bundle():
    output=ARCH/'.artifacts/bundle.js';output.parent.mkdir(exist_ok=True)
    executable=ARCH/'node_modules/.bin/esbuild'
    if not executable.exists():raise RuntimeError('Run npm install --prefix tools/archmap before building.')
    p=subprocess.run([str(executable),str(ARCH/'web/main.js'),'--bundle','--format=iife','--minify','--legal-comments=inline','--target=es2020','--outfile='+str(output)],cwd=ARCH,shell=False,capture_output=True,text=True)
    if p.returncode:raise RuntimeError(p.stderr)
    license_text=(ARCH/'vendor/THREE-LICENSE.txt').read_text()
    return '/*!\n'+license_text+'\n*/\n'+output.read_text()

def render(model,live=None,js=None):
    template=(ARCH/'web/template.html').read_text();style=(ARCH/'web/style.css').read_text()
    fonts=[]
    manifest=ARCH/'vendor/fonts/manifest.json'
    if manifest.exists():
        for font in json.loads(manifest.read_text())['fonts']:
            data=base64.b64encode((manifest.parent/font['file']).read_bytes()).decode()
            extra='unicode-range:U+300C-300D;' if font['family']=='endr-brackets' else ''
            fonts.append('@font-face{font-family:"'+font['family']+'";font-weight:'+str(font['weight'])+';font-display:swap;src:url(data:font/woff2;base64,'+data+') format("woff2");'+extra+'}')
    payload=json.dumps(model,sort_keys=True,separators=(',',':'),ensure_ascii=False).replace('<','\\u003c')
    boot='window.__ARCHMAP_MODEL__='+payload+';'
    if live:boot+='window.__ARCHMAP_LIVE__='+json.dumps(live)+';'
    return template.replace('/*__STYLE__*/','\n'.join(fonts)+'\n'+style).replace('/*__BOOT__*/',boot).replace('/*__SCRIPT__*/',(js if js is not None else bundle()).replace('</script','<\\/script'))

def normalized(html):
    # Observation instants are provenance, not semantic build changes.
    return re.sub(r'"(?:generated|ranAt)":"[^"]*"',lambda m:m[0].split(':')[0]+':"<observation-time>"',html)

def build(root=ROOT,strict=False,check=False):
    root=Path(root).resolve();model=layout.apply(extract.extract(root,strict=strict));html=render(model)
    target=root/'docs/architecture/index.html'
    if check:
        equal=target.exists() and normalized(target.read_text())==normalized(html)
        print('CURRENT' if equal else 'STALE');return 0 if equal else 1
    target.write_text(html)
    print(json.dumps(dict(status='BUILT',bytes=len(html.encode()),nodes=len(model['nodes']),edges=len(model['edges']))));return 0

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--strict',action='store_true');parser.add_argument('--check',action='store_true');parser.add_argument('--watch',action='store_true');parser.add_argument('--root',type=Path,default=ROOT)
    args=parser.parse_args()
    try:
        code=build(args.root,args.strict,args.check)
        if args.watch:
            from serve import snapshot
            last=snapshot(args.root)
            while True:
                time.sleep(1);current=snapshot(args.root)
                if current!=last:build(args.root,args.strict);last=current
        raise SystemExit(code)
    except (ValueError,OSError,RuntimeError) as exc:print(str(exc),file=sys.stderr);raise SystemExit(1)
