"""Complete field-level patches. Arrays of graph objects are addressed by identity."""
from __future__ import annotations
import copy
COLLECTIONS={'nodes':'node','edges':'edge','payloads':'payload','tour':'tour','zones':'zone','tiers':'tier','checks':'check','risks':'risk'}
MISSING=object()

def diff(old,new):
    changes=[]
    for key in sorted(old.keys()|new.keys()):
        a,b=old.get(key,MISSING),new.get(key,MISSING)
        if a==b:continue
        if key in COLLECTIONS and isinstance(a,list) and isinstance(b,list):
            prefix=COLLECTIONS[key];aa={x['id']:x for x in a};bb={x['id']:x for x in b}
            for ident in sorted(aa.keys()-bb.keys()):changes.append(dict(op=prefix+'.remove',collection=key,id=ident,**{'from':aa[ident],'to':None}))
            for index,item in enumerate(b):
                ident=item['id']
                if ident not in aa:changes.append(dict(op=prefix+'.add',collection=key,id=ident,index=index,**{'from':None,'to':item}));continue
                for field in sorted(aa[ident].keys()|item.keys()):
                    x,y=aa[ident].get(field,MISSING),item.get(field,MISSING)
                    if x!=y:changes.append(dict(op=prefix+'.'+field,collection=key,id=ident,field=field,remove=y is MISSING,**{'from':None if x is MISSING else x,'to':None if y is MISSING else y}))
            simulated=[x['id'] for x in a if x['id'] in bb]
            for index,item in enumerate(b):
                if item['id'] not in aa:simulated.insert(index,item['id'])
            if simulated!=[x['id'] for x in b]:changes.append(dict(op=prefix+'.order',collection=key,**{'from':simulated,'to':[x['id'] for x in b]}))
        else:changes.append(dict(op='model.'+key,key=key,remove=b is MISSING,**{'from':None if a is MISSING else a,'to':None if b is MISSING else b}))
    return copy.deepcopy(changes)

def apply(old,changes):
    model=copy.deepcopy(old)
    for c in changes:
        if 'key' in c:
            if c.get('remove'):model.pop(c['key'],None)
            else:model[c['key']]=copy.deepcopy(c['to'])
            continue
        items=model[c['collection']]
        if c['op'].endswith('.remove'):items[:]=[i for i in items if i['id']!=c['id']]
        elif c['op'].endswith('.add'):items.insert(c['index'],copy.deepcopy(c['to']))
        elif c['op'].endswith('.order'):
            by={x['id']:x for x in items};items[:]=[by[i] for i in c['to']]
        else:
            item=next(i for i in items if i['id']==c['id'])
            if c.get('remove'):item.pop(c['field'],None)
            else:item[c['field']]=copy.deepcopy(c['to'])
    return model
