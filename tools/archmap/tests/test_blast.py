import json
import unittest
from support import ROOT
from extract import blast

def reference(model,offline):
    dead=set(offline)
    for _ in model['nodes']:
        next_dead=set(dead)
        for node in model['nodes']:
            ins=[e for e in model['edges'] if e['to']==node['id'] and not e.get('blocked') and not e.get('feedback')]
            for kind in ('data','control',None):
                chosen=[e for e in ins if kind is None or e['kind']==kind]
                if chosen:
                    if set(e['from'] for e in chosen)<=dead:next_dead.add(node['id'])
                    break
        dead=next_dead
    return sorted(dead-set(offline))

class Blast(unittest.TestCase):
    def test_real_graph_and_spof_against_independent_synchronous_reference(self):
        model=json.loads((ROOT/'tools/archmap/curated.json').read_text())
        for n in model['nodes']:
            self.assertEqual(blast(model,[n['id']])['starved'],reference(model,[n['id']]),n['id'])
    def test_three_synthetic_graphs(self):
        for edges in [
            [('a','b','data',False,False),('b','c','data',False,False)],
            [('a','c','data',False,False),('b','c','data',False,False)],
            [('a','b','control',False,False),('b','c','data',True,False),('c','a','data',False,True)]]:
            model={'nodes':[{'id':x} for x in 'abc'],'edges':[dict(zip(('from','to','kind','blocked','feedback'),e)) for e in edges]}
            for offline in [['a'],['b'],['a','b']]:self.assertEqual(blast(model,offline)['starved'],reference(model,offline))
    def test_one_surviving_data_input_prevents_starvation(self):
        model={'nodes':[{'id':x} for x in 'abc'],'edges':[{'from':x,'to':'c','kind':'data'} for x in 'ab']}
        self.assertEqual(blast(model,['a'])['starved'],[])
        self.assertEqual(blast(model,['a'])['degraded'],['c'])
