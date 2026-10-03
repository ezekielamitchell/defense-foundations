import json
import tempfile
import unittest
from pathlib import Path
from support import ROOT,ARCH,ART
from extract import resolve_source,extract

class Anchors(unittest.TestCase):
    def test_real_sources_resolve_strictly(self):
        model=extract(ROOT,results=[],strict=True)
        for group in ('tiers','zones','nodes','edges','payloads','tour'):
            for item in model[group]:
                self.assertTrue(item['sources'])
                self.assertEqual(item['provenance'],'ok')
    def test_missing_ambiguous_and_invalid_span(self):
        with tempfile.TemporaryDirectory(dir=ART) as tmp:
            root=Path(tmp);(root/'x').write_text('unique\nrepeat\nrepeat\n')
            for src in ({'path':'missing','anchor':'a'}, {'path':'x','anchor':'absent'}, {'path':'x','anchor':'unique','span':5}):
                self.assertEqual(resolve_source(root,src)['provenance'],'stale')
            self.assertIn('warning',resolve_source(root,{'path':'x','anchor':'repeat'}))
            self.assertEqual(resolve_source(root,{'path':'x','anchor':'unique','span':2})['lines'],'1-2')
    def test_source_cannot_escape_root(self):
        self.assertEqual(resolve_source(ROOT,{'path':'../outside','anchor':'x'})['provenance'],'stale')
