import unittest
from support import ROOT
import extract, layout


class Routing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = layout.apply(extract.extract(ROOT, results=[], strict=True))

    def test_routes_clear_every_module(self):
        for edge in self.model['edges']:
            points = [edge['sourcePort'], *edge['route'], edge['targetPort']]
            for a, b in zip(points, points[1:]):
                self.assertTrue(a[0] == b[0] or a[1] == b[1], edge['id'])
                for node in self.model['nodes']:
                    p = node['position']
                    left, right = p['x']-p['width']/2, p['x']+p['width']/2
                    top, bottom = p['z']-p['depth']/2, p['z']+p['depth']/2
                    intersects = (left < a[0] < right and max(min(a[1], b[1]), top) < min(max(a[1], b[1]), bottom)) if a[0] == b[0] else (top < a[1] < bottom and max(min(a[0], b[0]), left) < min(max(a[0], b[0]), right))
                    self.assertFalse(intersects, (edge['id'], node['id'], a, b))

    def test_ports_are_distinct_and_on_their_module(self):
        for node in self.model['nodes']:
            p = node['position']
            for direction, port, sign in [('from', 'sourcePort', 1), ('to', 'targetPort', -1)]:
                ports = [tuple(e[port]) for e in self.model['edges'] if e[direction] == node['id']]
                self.assertEqual(len(ports), len(set(ports)))
                for x, z in ports:
                    self.assertLess(abs(x-p['x']), p['width']/2)
                    self.assertEqual(z, p['z']+sign*p['depth']/2)
