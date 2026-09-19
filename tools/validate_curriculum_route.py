#!/usr/bin/env python3
"""Read-only checks for the prepared curriculum, separate from reset authority."""
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT = Path('/Users/house/aegis nexus')


def validate(data: dict, check_files: bool = True) -> list[str]:
    errors: list[str] = []
    phases = data.get('phases', [])
    ids = [p.get('id') for p in phases]
    expected = {f'P{i}' for i in range(13)}
    if len(ids) != 13 or set(ids) != expected:
        return ['phase IDs must be exactly P0 through P12, once each']
    by_id = {p['id']: p for p in phases}
    if data.get('active_phase') != 'P0':
        errors.append('only P0 may be active')
    if data.get('activation') not in {'curriculum-prepared-reset-not-executed', 'curriculum-active-schedule-in-private-authority'}:
        errors.append('route must not claim reset activation')
    core = [f'P{n}' for n in data.get('core_order', [])]
    optional = [f'P{n}' for n in data.get('optional_modules', [])]
    if len(set(core + optional)) != 13 or set(core + optional) != expected or set(core) & set(optional):
        errors.append('core and optional modules must partition all 13 IDs')
    if len(core) != len(set(core)) or len(optional) != len(set(optional)):
        errors.append('duplicate route entry')
    for p in phases:
        pid = p['id']
        if p.get('status') != ('active-proof-unverified' if pid == 'P0' else 'not-started'):
            errors.append(f'{pid}: invalid activation/completion claim')
        if p.get('role') != ('core' if pid in core else 'optional'):
            errors.append(f'{pid}: role and route disagree')
        for dep in p.get('prerequisites', []):
            if dep not in expected:
                errors.append(f'{pid}: unknown prerequisite {dep}')
            elif pid in core and (dep not in core or core.index(dep) >= core.index(pid)):
                errors.append(f'{pid}: core prerequisite is optional or out of order')
        if check_files:
            for key, base in [('repository_path', ROOT), ('vault_path', VAULT)]:
                relative = Path(p.get(key, ''))
                if relative.is_absolute() or '..' in relative.parts:
                    errors.append(f'{pid}: unsafe {key}')
                    continue
                path = base / relative
                if not path.is_file():
                    errors.append(f'{pid}: missing {key}')
                    continue
                text = path.read_text()
                if pid != 'P0' and p['title'] not in text:
                    errors.append(f'{pid}: title differs in {key}')
                if pid != 'P0' and not re.search(r'not[- ]started', text):
                    errors.append(f'{pid}: future status missing in {key}')
    visiting: set[str] = set()
    visited: set[str] = set()

    def walk(pid: str) -> None:
        if pid in visiting:
            errors.append('cyclic prerequisites')
            return
        if pid in visited:
            return
        visiting.add(pid)
        for dep in by_id[pid].get('prerequisites', []):
            if dep in by_id:
                walk(dep)
        visiting.remove(pid)
        visited.add(pid)

    for pid in ids:
        walk(pid)
    if 'P9' in by_id['P10'].get('prerequisites', []):
        errors.append('RL must not gate deterministic coordination')
    if check_files:
        for name in ['START_HERE.md', 'COMPETENCY_PATHWAY.md', 'RESOURCE_SPINE.md', 'RESET_HANDOFF.md', 'REFRESH_REVIEW.md']:
            if not (ROOT / 'curriculum' / name).is_file():
                errors.append(f'missing curriculum guide: {name}')
    return errors


def self_test(data: dict) -> None:
    assert not validate(data, False)
    changes = [
        lambda d: d['phases'][1]['prerequisites'].append('P12'),
        lambda d: d['phases'][10]['prerequisites'].append('P9'),
        lambda d: d['phases'][3].update(status='complete'),
        lambda d: d.update(active_phase='P4'),
        lambda d: d['phases'].pop(),
        lambda d: d.update(activation='reset-complete'),
    ]
    for change in changes:
        broken = copy.deepcopy(data)
        change(broken)
        assert validate(broken, False), 'invalid route was accepted'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    route = json.loads((ROOT / 'curriculum/route-v2.json').read_text())
    if args.self_test:
        self_test(route)
    findings = validate(route)
    print(json.dumps({'status': 'FAIL' if findings else 'PASS', 'errors': findings, 'negative_cases': 6 if args.self_test else 0}, indent=2))
    raise SystemExit(bool(findings))
