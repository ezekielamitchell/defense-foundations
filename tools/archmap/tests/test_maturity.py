import tempfile
import unittest
from pathlib import Path
from support import ROOT,ART
from extract import maturity

class Maturity(unittest.TestCase):
    def test_no_files_is_planned_and_documents_can_be_planning_only(self):
        self.assertEqual(maturity({'id':'x'},[],[],ROOT)[0],'planned')
        self.assertEqual(maturity({'id':'x','planningOnly':True},['README.md'],[],ROOT)[0],'planned')
    def test_implemented(self):
        self.assertEqual(maturity({'id':'x'},['README.md'],[],ROOT)[0],'implemented')
    def test_zero_tests_is_not_tested(self):
        node={'id':'x','checks':['test']}
        result={'id':'test','ranAt':'observed','collected':0,'passed':0,'exitCode':0}
        self.assertEqual(maturity(node,['README.md'],[result],ROOT)[0],'implemented')
    def test_tested_needs_observation_and_bound_pass(self):
        node={'id':'x','checks':['test']}
        result={'id':'test','ranAt':'observed','collected':3,'passed':1,'failed':2}
        self.assertEqual(maturity(node,['x'],[result],ROOT)[0],'tested')
        result['ranAt']=None
        self.assertEqual(maturity(node,['x'],[result],ROOT)[0],'implemented')
    def test_override_needs_reason_and_source(self):
        with self.assertRaises(ValueError):maturity({'id':'x','override':{'maturity':'tested'}},[],[],ROOT)
        self.assertEqual(maturity({'id':'x','override':{'maturity':'implemented','reason':'human role','sources':[{'path':'AGENTS.md'}]}},[],[],ROOT)[0],'implemented')
    def test_deployed_needs_explicit_source(self):
        with self.assertRaises(ValueError):maturity({'id':'x','deploymentProof':{'reason':'claim'}},[],[],ROOT)
        self.assertEqual(maturity({'id':'x','deploymentProof':{'sources':[{'path':'README.md'}]}},[],[],ROOT)[0],'deployed')
    def test_placeholder_signature_stops_matching_after_implementation_changes(self):
        with tempfile.TemporaryDirectory(dir=ART) as tmp:
            root=Path(tmp);path=root/'main.py';path.write_text('print("hello")\n')
            node={'id':'x','stubSignatures':[{'path':'main.py','anchor':'print("hello")','exact':True}]}
            self.assertEqual(maturity(node,['main.py'],[],root)[0],'stub')
            path.write_text('print("hello")\nprint("real work")\n')
            self.assertEqual(maturity(node,['main.py'],[],root)[0],'implemented')
