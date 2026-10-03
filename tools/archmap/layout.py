"""Deterministic layered board. Content changes never affect x/z placement."""
from __future__ import annotations
import copy
import hashlib
import json
import routing

CW,RH,GUTTER=255,150,75

def topology(model):
    return json.dumps({'nodes':sorted((n['id'],n['zone'],n.get('primary',False),n.get('pin',{})) for n in model['nodes']),
                       'edges':sorted((e['id'],e['from'],e['to'],bool(e.get('feedback')),bool(e.get('blocked'))) for e in model['edges'])},sort_keys=True)

def apply(model,previous=None):
    prior={n['id']:n for n in previous['nodes']} if previous else {}
    model=copy.deepcopy(model); nodes={n['id']:n for n in model['nodes']}; zones={z['id']:z for z in model['zones']}
    edges=[e for e in model['edges'] if not e.get('blocked') and not e.get('feedback')]
    incoming={i:[] for i in nodes};outgoing={i:[] for i in nodes}
    for e in edges:incoming[e['to']].append(e['from']);outgoing[e['from']].append(e['to'])
    ranks={}; pending=set(nodes)
    while pending:
        ready=sorted(i for i in pending if all(p in ranks for p in incoming[i]))
        if not ready:raise ValueError('Non-feedback cycle in architecture graph')
        for i in ready:
            floor=prior.get(i,{}).get('position',{}).get('rank',0)
            ranks[i]=max(floor,max((ranks[p]+1 for p in incoming[i]),default=0));pending.remove(i)
    for i,n in nodes.items():ranks[i]=max(ranks[i],n.get('pin',{}).get('rank',0))
    rows={r:sorted(i for i in nodes if ranks[i]==r) for r in sorted(set(ranks.values()))}
    order={i:k for r,row in rows.items() for k,i in enumerate(row)}
    for sweep in range(24):
        down=sweep%2==0
        for rank in sorted(rows,reverse=not down):
            peers=incoming if down else outgoing
            def bary(i):
                values=[order[p] for p in peers[i]]
                return (nodes[i].get('pin',{}).get('order',sum(values)/len(values) if values else order[i]),i)
            rows[rank].sort(key=bary)
            for k,i in enumerate(rows[rank]):order[i]=k
    # Reserve additional rows at zone transitions so plates retain a true gutter.
    breaks=set()
    for lane in range(3):
        lanezones=sorted([z for z in model['zones'] if z['lane']==lane],key=lambda z:(min(ranks[i] for i in z['nodes'] if i in nodes),z['id']))
        for z in lanezones[1:]:breaks.add(min(ranks[i] for i in z['nodes'] if i in nodes))
    ypos={r:r*RH+sum(90 for b in breaks if b<=r) for r in rows}
    cols=[max(base,max((sum(zones[nodes[i]['zone']]['lane']==lane for i in row) for row in rows.values()),default=0)) for lane,base in enumerate([3,3,1])]
    starts=[0,cols[0]*CW+GUTTER,(cols[0]+cols[1])*CW+2*GUTTER]
    for rank,row in rows.items():
        for lane in range(3):
            ids=[i for i in row if zones[nodes[i]['zone']]['lane']==lane]
            if previous:ids.sort(key=lambda i:(prior.get(i,{}).get('position',{}).get('order',999),order[i],i))
            reserved={prior[i]['position']['order'] for i in ids if i in prior and prior[i]['position']['rank']==rank}
            used=set()
            for sequential,i in enumerate(ids):
                if i in prior and prior[i]['position']['rank']==rank:j=prior[i]['position']['order']
                else:j=next(k for k in range(len(ids)+len(reserved)+1) if k not in reserved and k not in used)
                used.add(j)
                node=nodes[i];width=148*(1.5 if node.get('primary') else 1);depth=68*(1.5 if node.get('primary') else 1)
                x=starts[lane]+(j if len(ids)>1 else (cols[lane]-1)/2)*CW
                node['position']=dict(x=x,z=ypos[rank],rank=rank,order=j,width=width,depth=depth)
                if previous and i in prior and prior[i]['zone']==node['zone'] and prior[i]['position']['rank']==rank:
                    old=prior[i]['position'];node['position'].update(x=old['x'],z=old['z'],order=old['order'])
    topo=hashlib.sha256(topology(model).encode()).hexdigest()
    if previous and previous.get('layout',{}).get('topology')==topo:
        old={n['id']:n['position'] for n in previous['nodes']}
        for i,node in nodes.items():node['position']=copy.deepcopy(old[i])
    for zone in model['zones']:
        ns=[nodes[i] for i in zone['nodes'] if i in nodes]
        zone['plate']={
            'x0':min(n['position']['x']-n['position']['width']/2 for n in ns)-24,
            'x1':max(n['position']['x']+n['position']['width']/2 for n in ns)+24,
            'z0':min(n['position']['z']-n['position']['depth']/2 for n in ns)-46,
            'z1':max(n['position']['z']+n['position']['depth']/2 for n in ns)+24,
        }
    # Ensure a gutter even when primary footprints increase plate bounds.
    for lane in range(3):
        zs=sorted((z for z in model['zones'] if z['lane']==lane),key=lambda z:z['plate']['z0'])
        for prev,z in zip(zs,zs[1:]):
            delta=max(0,prev['plate']['z1']+GUTTER-z['plate']['z0'])
            if delta:
                for i in z['nodes']:
                    if i in nodes:nodes[i]['position']['z']+=delta
                z['plate']['z0']+=delta;z['plate']['z1']+=delta
    routing.route(model)
    ps=[z['plate'] for z in model['zones']]
    model['layout']=dict(topology=topo,column=CW,rank=RH,gutter=GUTTER,sweeps=24,
                         bounds=dict(x0=min(p['x0'] for p in ps)-60,x1=max(p['x1'] for p in ps)+60,z0=min(p['z0'] for p in ps)-35,z1=max(p['z1'] for p in ps)+45))
    return model
