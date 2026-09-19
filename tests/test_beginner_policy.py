import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("beginner_policy", ROOT / "tools/validate_beginner_policy.py")
policy_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(policy_module)


class BeginnerPolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads((ROOT / "curriculum/beginner-policy-v1.json").read_text())
        self.session = {
            "planned_key": "z0-first-session", "language": "python", "checkpoint": "Z0",
            "source": "python-crash-course-3e", "workspace": "existing repository",
            "first_action": "Find and run the greeting script", "done_when": "Explain one changed output",
            "artifact": "own script change", "log": "dated learning record",
            "verify": "Compare output with prediction", "resume": "Reopen Chapter 1 and saved script",
            "status": "scheduled_unverified", "gate_evidence": False,
        }

    def test_current_policy_and_initial_card_pass(self):
        self.assertEqual(policy_module.validate_initial_sessions(self.policy, [self.session]), [])

    def test_replacement_source_is_allowed_but_concurrent_sources_are_not(self):
        self.policy["active_teaching_sources"] = ["cs50p"]
        self.session["source"] = "cs50p"
        self.assertEqual(policy_module.validate_initial_sessions(self.policy, [self.session]), [])
        self.policy["active_teaching_sources"].append("python-crash-course-3e")
        self.assertTrue(policy_module.validate_policy(self.policy))

    def test_old_quotas_and_assumed_capacity_are_rejected(self):
        for key, value in (("daily_paper_quota", 1), ("reading_percentage_cap", 25),
                           ("default_weekly_hours", 60), ("default_weekly_hours", 8),
                           ("agent_framework_obligation", True)):
            with self.subTest(key=key, value=value):
                altered = copy.deepcopy(self.policy)
                altered[key] = value
                self.assertTrue(policy_module.validate_policy(altered))

    def test_early_rust_pairing_and_advancement_are_rejected(self):
        for changes in ({"language": "rust"}, {"checkpoint": "Z1"},
                        {"pair_cycle_id": "week-one"}, {"gate_evidence": True},
                        {"status": "complete"}):
            with self.subTest(changes=changes):
                row = self.session | changes
                self.assertTrue(policy_module.validate_initial_sessions(self.policy, [row]))

    def test_prerequisite_and_history_bypasses_are_rejected(self):
        for key, value in (("rust_prerequisites", ["Z0"]), ("paired_work_prerequisites", ["Z5"]),
                           ("initial_learning_credit", 1), ("runtime_activation", True),
                           ("historical_evidence_preserved", False), ("company_gates_independent", False),
                           ("automatic_reset_after_missed_work", True), ("catch_up_debt", True)):
            with self.subTest(key=key):
                altered = self.policy | {key: value}
                self.assertTrue(policy_module.validate_policy(altered))

    def test_duplicate_id_and_missing_resume_are_rejected(self):
        self.assertTrue(policy_module.validate_initial_sessions(self.policy, [self.session, self.session]))
        del self.session["resume"]
        self.assertTrue(policy_module.validate_initial_sessions(self.policy, [self.session]))

    def test_malformed_data_fails_closed(self):
        for policy in (None, [], {}, self.policy | {"initial_learning_credit": False},
                       self.policy | {"unregistered_override": True}):
            with self.subTest(policy=policy):
                self.assertTrue(policy_module.validate_policy(policy))
        self.assertTrue(policy_module.validate_initial_sessions(self.policy, {}))
        self.assertTrue(policy_module.validate_initial_sessions(self.policy, [None]))


if __name__ == "__main__":
    unittest.main()
