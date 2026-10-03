import json
import unittest
from support import ROOT
from extract import extract

class Extraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.model=extract(ROOT,results=[],strict=True)
    def test_metrics_match_independent_count(self):
        for node in self.model['nodes']:
            count=0
            for path in node['matchedFiles']:
                count+=len([s for s in (ROOT/path).read_text().splitlines() if s.strip()])
            self.assertEqual(node['metric']['value'],count,node['id'])
            self.assertEqual(node['metric']['files'],len(node['matchedFiles']))
    def test_all_relations_resolve(self):
        nodes={n['id'] for n in self.model['nodes']};payloads={p['id'] for p in self.model['payloads']}
        for edge in self.model['edges']:
            self.assertIn(edge['from'],nodes);self.assertIn(edge['to'],nodes);self.assertIn(edge['payload'],payloads)
    def test_external_nodes_are_inferred_and_flat(self):
        for node in self.model['nodes']:
            if node.get('external'):
                self.assertTrue(node['inferred']);self.assertEqual(node['matchedFiles'],[]);self.assertEqual(node['height'],4)
