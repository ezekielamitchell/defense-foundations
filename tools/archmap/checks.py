"""Audited, fixed commands. No shell; private-authority checks remain unavailable."""
from __future__ import annotations
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess

COMMANDS = {
    'integrity': ['python3', 'tools/validate_phase0_integrity.py'],
    'route': ['python3', 'tools/validate_curriculum_route.py'],
    'beginner': ['python3', 'tools/validate_beginner_policy.py'],
    'unit-beginner': ['python3', '-m', 'unittest', '-v', 'tests.test_beginner_policy'],
    'unit-integrity': ['python3', '-m', 'unittest', '-v', 'tests.test_phase0_integrity'],
    'node-app': ['node', '--check', 'mobile/app.js'],
    'node-sw': ['node', '--check', 'mobile/sw.js'],
    'diff-check': ['git', 'diff', '--check'],
}
UNAVAILABLE = {
    'integrity': 'Unavailable: the command reads private authority and imports outside-repository code.',
    'route': 'Unavailable: the command reads phase documents in the private vault.',
    'unit-integrity': 'Unavailable: the suite reads the private vault and writes temporary fixtures.',
}
BINDINGS = {'integrity':['integrity','unit-integrity'], 'routeval':['route'],
            'route':['route'], 'policyval':['beginner','unit-beginner'],
            'beginner':['beginner'], 'projection':['unit-integrity'],
            'mobile':['node-app','node-sw'], 'syntax':['diff-check']}

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')

def redact(text, root):
    text = text.replace(str(Path(root).resolve()), '<repo>')
    # Quoted traceback filenames may contain spaces; handle them before tokens.
    text = re.sub(r'([\"\'])/(?!<repo>)[^\"\'\n]+\1', '"<outside-repo>"', text)
    text = re.sub(r'(?<![\w:])/(?:Users|home|tmp|var|private|usr|opt|Library|System)(?:/[^\s\"\'<>:,;\)\]]*)*', '<outside-repo>', text)
    text = re.sub(r'Ran (\d+) tests? in [\d.]+s', r'Ran \1 tests', text)
    return text

def parse_tests(output):
    match = re.search(r'Ran (\d+) tests?', output)
    if not match: return dict(collected=None, passed=None, failed=None, errored=None)
    count = int(match[1])
    def num(name):
        m = re.search(r'\b'+name+r'=(\d+)', output)
        return int(m[1]) if m else 0
    failed, errored, skipped = num('failures'), num('errors'), num('skipped')
    return dict(collected=count, passed=max(0,count-failed-errored-skipped), failed=failed, errored=errored)

def run(root, ids=None):
    results = []
    for ident in (ids if ids is not None else COMMANDS):
        if ident not in COMMANDS: raise ValueError('Unregistered check: '+ident)
        item = dict(id=ident,command=COMMANDS[ident],ranAt=None,exitCode=None,
                    collected=None,passed=None,failed=None,errored=None,firstFailure=None)
        if ident in UNAVAILABLE:
            item.update(status='unavailable',reason=UNAVAILABLE[ident]); results.append(item); continue
        item['ranAt'] = now()
        try:
            p = subprocess.run(COMMANDS[ident], cwd=Path(root), shell=False, timeout=60,
                               env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),
                               text=True,capture_output=True)
            output = redact(p.stdout+'\n'+p.stderr,root)
            item.update(exitCode=p.returncode,status='pass' if p.returncode==0 else 'fail',**parse_tests(output))
            if p.returncode:
                important = next((line for line in output.splitlines() if re.search(r'^(ERROR|FAIL|Error|SyntaxError|AssertionError)',line)),output.strip())
                item['firstFailure'] = important[:300]
        except (subprocess.TimeoutExpired,OSError) as exc:
            item.update(status='error',firstFailure=redact(str(exc),root)[:300])
        results.append(item)
    return results

def receipt_contracts(root):
    """Preflight local receipt shape without claiming a proof verdict.

    The public educational projection deliberately omits reset identity,
    technical dates and pair cycles. Passing it to validate_proof would make
    every legitimate private receipt appear to fail. Full proof validation
    remains unavailable in this repository-only map.
    """
    root = Path(root).resolve()
    schema = json.loads((root/'docs/phase0-proof.schema.json').read_text())
    required = set(schema['required'])
    expected_version = schema['properties']['schema_version']['const']
    unavailable = 'Full proof verification needs private active reset identity and technical-date pairing.'
    results=[]
    for path in sorted((root/'progress/proofs').glob('*.json')):
        if not path.resolve().is_relative_to(root): continue
        try:
            receipt=json.loads(path.read_text())
            if not isinstance(receipt,dict): raise ValueError('Receipt must be a JSON object')
            errors=[]
            missing=sorted(required-set(receipt))
            unexpected=sorted(set(receipt)-set(schema['properties']))
            if missing: errors.append('proof missing fields: '+', '.join(missing))
            if unexpected: errors.append('proof has unsupported fields: '+', '.join(unexpected))
            if receipt.get('schema_version')!=expected_version: errors.append('unsupported proof schema')
            # Reject escapes without reading artifact contents. Identity and
            # evidence checks still require the canonical private validator.
            for field in ('artifact_paths','changed_paths'):
                values=receipt.get(field,[])
                if field in receipt and (not isinstance(values,list) or not all(isinstance(value,str) and value for value in values)):
                    errors.append('proof '+field+' must be a list of non-empty paths')
                elif isinstance(values,list):
                    for value in values:
                        if isinstance(value,str) and not (root/value).resolve().is_relative_to(root):
                            errors.append('Receipt path escapes repository')
        except (ValueError,TypeError,KeyError,OSError) as exc: errors=[str(exc)]
        results.append(dict(path=path.relative_to(root).as_posix(),status='FAIL' if errors else 'UNAVAILABLE',
                            errors=[redact(str(e),root) for e in errors],
                            reason=None if errors else unavailable,
                            scope='structural preflight only; no proof verdict'))
    return results
