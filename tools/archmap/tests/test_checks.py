import subprocess
import unittest
from unittest.mock import patch
from support import ROOT
import checks

class Checks(unittest.TestCase):
    def test_unknown_command_is_rejected(self):
        with self.assertRaises(ValueError):checks.run(ROOT,['unregistered'])
    def test_exact_whitelist_shell_false_and_no_duration_stored(self):
        with patch('checks.subprocess.run',return_value=subprocess.CompletedProcess([],0,'','Ran 3 tests in 1.23s\nOK')) as mock:
            result=checks.run(ROOT,['unit-beginner'])[0]
            self.assertEqual(mock.call_args.args[0],checks.COMMANDS['unit-beginner'])
            self.assertFalse(mock.call_args.kwargs['shell']);self.assertEqual(mock.call_args.kwargs['timeout'],60)
            self.assertEqual(mock.call_args.kwargs['env']['PYTHONDONTWRITEBYTECODE'],'1')
            self.assertEqual(result['passed'],3)
            self.assertNotIn('duration',result);self.assertNotIn('output',result)
    def test_outside_paths_redacted(self):
        value=checks.redact('File "/Users/name/private vault/x.py", line 9\n/home/name/code.py failed\n'+str(ROOT)+'/README.md',ROOT)
        self.assertNotIn('/Users',value);self.assertNotIn('/home',value);self.assertIn('<repo>/README.md',value)
    def test_private_checks_never_execute(self):
        with patch('checks.subprocess.run') as mock:
            result=checks.run(ROOT,list(checks.UNAVAILABLE))
            mock.assert_not_called();self.assertTrue(all(x['status']=='unavailable' for x in result))
    def test_counts_include_failures_and_errors(self):
        self.assertEqual(checks.parse_tests('Ran 8 tests\nFAILED (failures=2, errors=1, skipped=1)'),dict(collected=8,passed=4,failed=2,errored=1))
    def test_malformed_receipts_are_observations_not_crashes(self):
        import json
        from pathlib import Path
        import tempfile
        from support import ART
        with tempfile.TemporaryDirectory(dir=ART) as d:
            root=Path(d);(root/'tools').mkdir();(root/'docs').mkdir();(root/'progress/proofs').mkdir(parents=True)
            (root/'tools/validate_phase0_integrity.py').write_bytes((ROOT/'tools/validate_phase0_integrity.py').read_bytes())
            (root/'docs/aegis-phase0-projection.json').write_bytes((ROOT/'docs/aegis-phase0-projection.json').read_bytes())
            (root/'docs/phase0-proof.schema.json').write_bytes((ROOT/'docs/phase0-proof.schema.json').read_bytes())
            (root/'progress/proofs/array.json').write_text('[]')
            (root/'progress/proofs/bad.json').write_text('{')
            result=checks.receipt_contracts(root);self.assertEqual([r['status'] for r in result],['FAIL','FAIL'])
            self.assertIn('JSON object',result[0]['errors'][0])
    def test_well_shaped_receipt_is_unavailable_without_private_authority(self):
        import json
        from pathlib import Path
        import tempfile
        from support import ART
        with tempfile.TemporaryDirectory(dir=ART) as d:
            root=Path(d);(root/'docs').mkdir();(root/'progress/proofs').mkdir(parents=True)
            (root/'docs/phase0-proof.schema.json').write_bytes((ROOT/'docs/phase0-proof.schema.json').read_bytes())
            receipt={
                'schema_version':'phase0-proof.v1','reset_id':'synthetic',
                'date':'2000-01-01','pair_slice_id':None,'artifact_paths':[],
                'command_results':[],'observed_output_digest':None,
                'test_count':0,'changed_paths':[],'verdict':'unverified',
                'blocker':'Synthetic fixture','course_resume_point':None,
                'next_command':'python3 --version',
                'evidence_basis':{'artifacts_observed':False,'commands_observed':False,
                                  'schedule_only':False,'task_state_only':False},
            }
            path=root/'progress/proofs/example.json';path.write_text(json.dumps(receipt))
            result=checks.receipt_contracts(root)
            self.assertEqual(result[0]['status'],'UNAVAILABLE')
            self.assertIn('private active reset identity',result[0]['reason'])
            receipt['artifact_paths']=['../outside'];path.write_text(json.dumps(receipt))
            result=checks.receipt_contracts(root)
            self.assertEqual(result[0]['status'],'FAIL')
            self.assertIn('escapes repository',result[0]['errors'][0])
