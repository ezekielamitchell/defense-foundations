import copy
import json
import unittest
from support import ROOT
import extract,layout

class Layout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.model=extract.extract(ROOT,results=[],strict=True)
    def test_byte_deterministic(self):
        self.assertEqual(json.dumps(layout.apply(self.model),sort_keys=True),json.dumps(layout.apply(self.model),sort_keys=True))
    def test_content_changes_move_nothing(self):
        first=layout.apply(self.model); changed=copy.deepcopy(self.model);changed['nodes'][0]['height']+=50;changed['nodes'][0]['maturity']='planned'
        next_model=layout.apply(changed,first)
        self.assertEqual([n['position'] for n in first['nodes']],[n['position'] for n in next_model['nodes']])
    def test_plates_do_not_overlap(self):
        plates=[z['plate'] for z in layout.apply(self.model)['zones']]
        for i,a in enumerate(plates):
            for b in plates[i+1:]:self.assertTrue(a['x1']<=b['x0'] or b['x1']<=a['x0'] or a['z1']<=b['z0'] or b['z1']<=a['z0'],(a,b))
    def test_removed_edge_keeps_existing_coordinates(self):
        first=layout.apply(self.model);changed=copy.deepcopy(self.model);changed['edges']=[e for e in changed['edges'] if e['id']!='e-auth-exp']
        updated=layout.apply(changed,first)
        self.assertEqual([n['position'] for n in first['nodes']],[n['position'] for n in updated['nodes']])
    def test_added_dependency_only_moves_required_ranks(self):
        first=layout.apply(self.model);changed=copy.deepcopy(self.model)
        # A new dependency from the later gate to a source would be a real cycle.
        changed['edges'].append(dict(id='cycle',**{'from':'gate','to':'authority'},kind='data',blocked=False,feedback=False))
        with self.assertRaises(ValueError):layout.apply(changed,first)
