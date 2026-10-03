"""Deterministic rectilinear routing around module footprints, with shared gutters."""
import heapq
import math

def route(model):
    nodes={n['id']:n for n in model['nodes']};pad=18
    boxes=[(p['x']-p['width']/2-pad,p['z']-p['depth']/2-pad,p['x']+p['width']/2+pad,p['z']+p['depth']/2+pad) for p in (n['position'] for n in model['nodes'])]
    xs=set();zs=set();ends={};main={'projection','policy','learner','filestats','hellostats','commands','receipts','integrity','gate'}
    for x0,z0,x1,z1 in boxes:xs.update([x0,x1]);zs.update([z0,z1])
    # Stable fan-out ports keep wires individually inspectable at the module boundary.
    for e in model['edges']:
        a=nodes[e['from']]['position'];b=nodes[e['to']]['position']
        outs=sorted(x['id'] for x in model['edges'] if x['from']==e['from']);ins=sorted(x['id'] for x in model['edges'] if x['to']==e['to'])
        sx=a['x']+(outs.index(e['id'])-(len(outs)-1)/2)*7;tx=b['x']+(ins.index(e['id'])-(len(ins)-1)/2)*7
        sy=a['z']+a['depth']/2+pad;ty=b['z']-b['depth']/2-pad
        ends[e['id']]=((sx,sy),(tx,ty));xs.update([sx,tx]);zs.update([sy,ty]);e['primary']=e['from'] in main and e['to'] in main
    xs.update([min(xs)-42,max(xs)+42]);zs.update([min(zs)-42,max(zs)+42]);xs=sorted(xs);zs=sorted(zs)
    # Mid-gutter rails are shared intentionally; crossings incur a routing penalty.
    xs=sorted(set(xs+[(a+b)/2 for a,b in zip(xs,xs[1:]) if b-a>70]));zs=sorted(set(zs+[(a+b)/2 for a,b in zip(zs,zs[1:]) if b-a>65]))
    nx=len(xs);nz=len(zs);valid={};adj={};used={}
    def blocked(x,z):return any(a+1e-6<x<c-1e-6 and b+1e-6<z<d-1e-6 for a,b,c,d in boxes)
    for j,z in enumerate(zs):
        for i,x in enumerate(xs):valid[(i,j)]=not blocked(x,z)
    for (i,j),ok in valid.items():
        if not ok:continue
        neighbors=[]
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            q=(i+di,j+dj)
            if valid.get(q) and not blocked((xs[i]+xs[q[0]])/2,(zs[j]+zs[q[1]])/2):neighbors.append((q,abs(xs[i]-xs[q[0]])+abs(zs[j]-zs[q[1]]),0 if di else 1))
        adj[(i,j)]=neighbors
    for e in sorted(model['edges'],key=lambda e:(not e['primary'],bool(e.get('blocked')),e['id'])):
        start,end=ends[e['id']];s=(xs.index(start[0]),zs.index(start[1]));t=(xs.index(end[0]),zs.index(end[1]));initial=(s,1);queue=[(0,0,s,1)];cost={initial:0};parent={};goal=None
        while queue:
            _,g,p,direction=heapq.heappop(queue)
            if g!=cost.get((p,direction)):continue
            if p==t:goal=(p,direction);break
            for q,length,newdir in adj.get(p,[]):
                segment=tuple(sorted((p,q)));value=g+length+(32 if direction!=newdir else 0)+used.get(segment,0)*length*.035
                state=(q,newdir)
                if value<cost.get(state,math.inf):
                    cost[state]=value;parent[state]=(p,direction);h=abs(xs[q[0]]-end[0])+abs(zs[q[1]]-end[1]);heapq.heappush(queue,(value+h,value,q,newdir))
        if goal is None:raise ValueError('No obstacle-free route for '+e['id'])
        points=[];state=goal
        while True:
            p,d=state;points.append([xs[p[0]],zs[p[1]]])
            if state==initial:break
            prior=parent[state];seg=tuple(sorted((p,prior[0])));used[seg]=used.get(seg,0)+1;state=prior
        points.reverse();clean=[]
        for p in points:
            if len(clean)>=2 and ((clean[-2][0]==clean[-1][0]==p[0]) or (clean[-2][1]==clean[-1][1]==p[1])):clean[-1]=p
            else:clean.append(p)
        e['route']=clean
        e['sourcePort']=[start[0],nodes[e['from']]['position']['z']+nodes[e['from']]['position']['depth']/2]
        e['targetPort']=[end[0],nodes[e['to']]['position']['z']-nodes[e['to']]['position']['depth']/2]
