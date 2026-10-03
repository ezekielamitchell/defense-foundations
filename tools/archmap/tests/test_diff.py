import copy
import unittest
from support import ROOT
import diff

class DiffTests(unittest.TestCase):
    def test_identical_is_empty(self):
        m={'nodes':[{'id':'a','metric':{'value':1}}],'meta':{'rev':1}}
        self.assertEqual(diff.diff(m,m),[])
    def test_minimal_metric_and_roundtrip(self):
        a={'nodes':[{'id':'a','metric':{'value':1},'height':4,'sources':[1]}],'meta':{'rev':1}}
        b=copy.deepcopy(a);b['nodes'][0]['metric']['value']=2
        patch=diff.diff(a,b);self.assertEqual(len(patch),1);self.assertEqual(patch[0]['op'],'node.metric');self.assertEqual(diff.apply(a,patch),b)
    def test_add_remove_reorder_and_optional_fields(self):
        a={'nodes':[{'id':'a','old':1},{'id':'b'},{'id':'c'}],'meta':{'rev':1},'old':1}
        b={'nodes':[{'id':'c','new':1},{'id':'d'},{'id':'a'}],'meta':{'rev':2},'new':[1,2]}
        self.assertEqual(diff.apply(a,diff.diff(a,b)),b)
    def test_every_root_field(self):
        a={'nodes':[],'edges':[],'checks':[],'risks':[],'receiptContracts':[]}
        b={'nodes':[{'id':'n'}],'edges':[{'id':'e','from':'n'}],'checks':[{'id':'x','passed':7}], 'risks':[{'id':'r'}],'receiptContracts':[{'path':'a','status':'FAIL'}]}
        self.assertEqual(diff.apply(a,diff.diff(a,b)),b)
