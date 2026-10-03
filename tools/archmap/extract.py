"""Repository → anchored model. Python standard library; no private-vault reads."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
sys.dont_write_bytecode = True
import checks

ROOT=Path(__file__).resolve().parents[2]
EXCLUDED={'node_modules','.artifacts','__pycache__','.git','.venv','target'}

def safe_path(root,relative):
    path=(Path(root)/relative).resolve()
    if not path.is_relative_to(Path(root).resolve()): raise ValueError('Source escapes repository: '+relative)
    return path

def resolve_source(root,source):
    out=copy.deepcopy(source)
    try:
        path=safe_path(root,source['path']); text=path.read_text(); anchor=source['anchor']; span=source.get('span',1)
        if not anchor or not isinstance(span,int) or span<1: raise ValueError('Invalid anchor/span')
        matches=text.count(anchor)
        if not matches: raise ValueError('Anchor not found')
        first=text.index(anchor); line=text[:first].count('\n')+1; end=line+span-1
        if end>len(text.splitlines()): raise ValueError('Span exceeds file')
        out.update(lines=str(line) if span==1 else f'{line}-{end}',provenance='ok',
                   sha256=hashlib.sha256(text.encode()).hexdigest(),quote='\n'.join(text.splitlines()[line-1:min(end,line+11)])[:1000])
        if matches>1: out['warning']='Anchor matches more than once; first match selected'
    except (OSError,ValueError,KeyError) as exc: out.update(provenance='stale',error=str(exc),lines='?')
    return out

def owned_files(root,globs):
    root=Path(root).resolve(); found=set()
    for pattern in globs:
        if Path(pattern).is_absolute() or '..' in Path(pattern).parts: raise ValueError('Unsafe ownership glob')
        for path in root.glob(pattern):
            if path.is_file() and not EXCLUDED.intersection(path.relative_to(root).parts) and path.resolve().is_relative_to(root):
                found.add(path.relative_to(root).as_posix())
    return sorted(found)

def metric(root,files,globs):
    total=0
    for name in files:
        data=safe_path(root,name).read_bytes()
        if b'\x00' in data: continue
        try: total+=sum(bool(line.strip()) for line in data.decode('utf-8').splitlines())
        except UnicodeDecodeError: continue
    return dict(kind='lines',value=total,files=len(files),
                derivation='Non-blank UTF-8 lines in matched owned files; excludes binary, generated, dependency and build directories.',globs=globs)

def maturity(node,files,results,root):
    override=node.get('override')
    if override:
        if not override.get('reason') or not override.get('sources'): raise ValueError('Override needs reason and sources: '+node['id'])
        if override['maturity'] not in {'planned','stub','implemented','tested','deployed'}: raise ValueError('Invalid maturity override')
        return override['maturity'],override['reason']
    if node.get('deploymentProof'):
        if not node['deploymentProof'].get('sources'): raise ValueError('Deployment requires sourced proof')
        return 'deployed','Explicit deployment evidence is present.'
    bound=[r for r in results if r['id'] in node.get('checks',[])]
    qualified=[r for r in bound if r.get('ranAt') and (r.get('collected') or 0)>0 and (r.get('passed') or 0)>0]
    if qualified: return 'tested','Observed collected and passed tests: '+', '.join(r['id'] for r in qualified)+'. Failures remain visible separately.'
    signatures=node.get('stubSignatures',[])
    if files and signatures and all(resolve_source(root,x).get('provenance')=='ok' and (not x.get('exact') or safe_path(root,x['path']).read_text().strip()==x['anchor'].strip()) for x in signatures):
        return 'stub','The owned entry point still matches the anchored placeholder signature.'
    if files and not node.get('planningOnly'): return 'implemented','Owned source files exist; no qualifying bound test result was observed.'
    return 'planned','Planning documents only.' if node.get('planningOnly') else 'No owned implementation files match the configured globs.'

def blast(model,offline=()):
    dead=set(offline); starved=set(); edges=[e for e in model['edges'] if not e.get('blocked') and not e.get('feedback')]
    inputs={n['id']:[e for e in edges if e['to']==n['id']] for n in model['nodes']}
    changed=True
    while changed:
        changed=False
        for ident,ins in inputs.items():
            if ident in dead or not ins: continue
            primary=[e for e in ins if e['kind']=='data'] or [e for e in ins if e['kind']=='control'] or ins
            if all(e['from'] in dead for e in primary): starved.add(ident);dead.add(ident);changed=True
    degraded={ident for ident,ins in inputs.items() if ident not in dead and any(e['from'] in dead for e in ins)}
    return dict(offline=sorted(set(offline)),starved=sorted(starved),degraded=sorted(degraded))

def git(root,*args):
    p=subprocess.run(['git',*args],cwd=root,shell=False,timeout=60,capture_output=True,text=True)
    return p.stdout.strip() if p.returncode==0 else ''

def extract(root=ROOT,results=None,strict=False,generated=None):
    root=Path(root).resolve(); model=json.loads((root/'tools/archmap/curated.json').read_text())
    model=copy.deepcopy(model); results=checks.run(root) if results is None else copy.deepcopy(results)
    errors=[]; warnings=[]
    def anchor_tree(value):
        if isinstance(value,dict):
            if {'path','anchor'}<=value.keys():
                resolved=resolve_source(root,value)
                if resolved['provenance']=='stale': errors.append(resolved['path']+': '+resolved.get('error','stale'))
                if resolved.get('warning'): warnings.append(resolved['path']+': '+resolved['warning'])
                return resolved
            return {k:(v if k=='stubSignatures' else anchor_tree(v)) for k,v in value.items()}
        if isinstance(value,list): return [anchor_tree(v) for v in value]
        return value
    model=anchor_tree(model)
    for group in ('tiers','zones','nodes','edges','payloads','tour'):
        for item in model[group]:
            if not item.get('sources'): errors.append(f'{group}/{item["id"]}: missing sources')
            item['provenance']='stale' if any(s.get('provenance')=='stale' for s in item.get('sources',[])) else 'ok'
    for node in model['nodes']:
        files=owned_files(root,node.get('owns',[])); node['matchedFiles']=files
        node['metric']=metric(root,files,node.get('owns',[]))
        node['maturity'],node['maturityWhy']=maturity(node,files,results,root)
        node['height']=4 if node.get('external') else 8+10*math.log10(1+node['metric']['value'])
        node['checkRisk']=any(r.get('status') in ('fail','error') for r in results if r['id'] in node.get('checks',[]))
    status=git(root,'status','--porcelain')
    model['meta'].update(branch=git(root,'rev-parse','--abbrev-ref','HEAD'),commit=git(root,'rev-parse','HEAD'),
                         commitDate=git(root,'log','-1','--format=%cI'),dirtyCount=len(status.splitlines()),
                         generated=generated or checks.now(),rev=0,
                         derivations={'dirtyCount':'Number of records from git status --porcelain (untracked directories grouped).',
                                      'counts':'Array lengths and maturity grouping of the extracted model.',
                                      'commit':'git rev-parse HEAD','commitDate':'git log -1 --format=%cI'})
    model['checks']=results; model['receiptContracts']=checks.receipt_contracts(root)
    model['spofs']=[n['id'] for n in model['nodes'] if n['id']!='gate' and 'gate' in blast(model,[n['id']])['starved']]
    model['impact']={n['id']:len(blast(model,[n['id']])['starved']) for n in model['nodes']}
    unavailable=[n['id'] for n in model['nodes'] if n['maturity'] in ('planned','stub')]
    model['baselineBlast']=blast(model,unavailable)
    model['gateReady']=not ('gate' in model['baselineBlast']['starved'] or next(n for n in model['nodes'] if n['id']=='gate')['maturity']=='planned')
    model['risks']=[]
    byid={n['id']:n for n in model['nodes']}
    def risk(ident,text,rule,ids):
        sources=[]
        for nid in ids:
            for src in byid[nid]['sources']:
                if src not in sources:sources.append(src)
        model['risks'].append(dict(id=ident,text=text,derivedFrom=rule,sources=sources))
    if not model['gateReady']:risk('gate','The gate has no verified implementation path yet.','baseline-maturity-and-blast',['gate','receipts'])
    if not byid['receipts']['matchedFiles']:risk('receipts','No proof receipt JSON files exist.','receipt-file-count',['receipts'])
    stubs=[n['title'] for n in model['nodes'] if n['id'] in ('filestats','hellostats') and n['maturity']=='stub']
    if stubs:risk('stubs','Project 0 placeholders: '+', '.join(stubs)+'.','stub-signatures',['filestats','hellostats'])
    if byid['ci']['maturity']=='planned':risk('ci','CI exists only as a planned acceptance criterion.','ci-maturity',['ci'])
    if any(r.get('status')=='unavailable' for r in results):risk('authority','Private-authority checks are unavailable within the repository-only boundary. No cached test result is reused.','check-availability',['integrity','routeval'])
    inferred=[n for n in model['nodes'] if n.get('inferred')]
    if inferred:risk('inferred',str(len(inferred))+' nodes include an inference; their outlines are dashed.','inferred-node-count',[n['id'] for n in inferred])
    for node in model['nodes']:
        if node['provenance']=='stale':risk('stale-'+node['id'],node['title']+': stale source.','anchor-resolution',[node['id']])
        if node['checkRisk']:risk('check-'+node['id'],node['title']+': a bound check failed or errored.','observed-check-verdict',[node['id']])
    model['diagnostics']=dict(errors=errors,warnings=warnings)
    if strict and (errors or warnings): raise ValueError('\n'.join(errors+warnings))
    return model

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=ROOT);parser.add_argument('--strict',action='store_true')
    args=parser.parse_args()
    try:
        model=extract(args.root,strict=args.strict)
        print(json.dumps(dict(status='PASS',nodes=len(model['nodes']),edges=len(model['edges']),diagnostics=model['diagnostics'])))
    except (ValueError,OSError) as exc:print(str(exc),file=sys.stderr);raise SystemExit(1)
