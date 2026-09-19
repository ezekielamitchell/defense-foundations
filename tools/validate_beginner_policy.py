#!/usr/bin/env python3
"""Validate the beginner policy and optional initial-session drafts.

This read-only check does not verify capacity, learner proof, external state,
or reset activation. The private reset contract must verify those separately.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY_PATH = ROOT / "curriculum/beginner-policy-v1.json"
REQUIRED = {
    "schema_version": "defense-foundations.beginner-policy.v1",
    "status": "authorized-policy-awaiting-schedule",
    "active_phase": "P0",
    "initial_checkpoint": "Z0",
    "active_builds": ["project-0"],
    "replacement_teaching_sources": ["cs50p"],
    "guided_instruction_allowed": True,
    "reading_percentage_cap": None,
    "daily_paper_quota": 0,
    "agent_framework_obligation": False,
    "rust_prerequisites": [f"Z{i}" for i in range(6)],
    "paired_work_prerequisites": [f"Z{i}" for i in range(8)],
    "pair_identity_after_prerequisites": "weekly_pair_cycle_id",
    "independent_proof_per_language": True,
    "initial_learning_credit": 0,
    "advancement_requires": "observed-learner-proof",
    "date_based_advancement": False,
    "automatic_reset_after_missed_work": False,
    "catch_up_debt": False,
    "review_horizon_means": "review-deadline-not-completion-guarantee",
    "capacity_requires": "current-user-confirmed-constraints",
    "default_weekly_hours": None,
    "historical_evidence_preserved": True,
    "company_gates_independent": True,
    "schedule_authority": "private-aegis-approved-manifest",
    "runtime_activation": False,
}
CARD_FIELDS = ("source", "workspace", "first_action", "done_when", "artifact",
               "log", "verify", "resume")


def validate_policy(policy: object) -> list[str]:
    if not isinstance(policy, dict):
        return ["policy must be an object"]
    errors = []
    expected_keys = set(REQUIRED) | {"active_teaching_sources"}
    if set(policy) != expected_keys:
        errors.append("policy fields differ from the registered v1 contract")
    for key, value in REQUIRED.items():
        if type(policy.get(key)) is not type(value) or policy.get(key) != value:
            errors.append(f"{key}: violates the beginner policy")
    if policy.get("active_teaching_sources") not in (
        ["python-crash-course-3e"], ["cs50p"],
    ):
        errors.append("choose PCC or CS50P as one primary teaching source")
    return errors


def validate_initial_sessions(policy: object, sessions: object) -> list[str]:
    """Validate Z0 Foundation drafts only; never infer advancement from dates."""
    errors = validate_policy(policy)
    if errors:
        return errors
    if not isinstance(sessions, list):
        return ["initial sessions must be an array"]
    keys = set()
    for index, row in enumerate(sessions):
        prefix = f"initial session {index}"
        if not isinstance(row, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        key = row.get("planned_key")
        if not isinstance(key, str) or not key.strip() or key in keys:
            errors.append(f"{prefix}: missing or duplicate stable identity")
        else:
            keys.add(key)
        if row.get("language") != "python" or row.get("checkpoint") != "Z0":
            errors.append(f"{prefix}: initial work must begin at Python Z0")
        if row.get("pair_cycle_id") is not None:
            errors.append(f"{prefix}: paired work requires later learner proof")
        if row.get("source") not in policy["active_teaching_sources"]:
            errors.append(f"{prefix}: source differs from the single primary source")
        if row.get("status") != "scheduled_unverified" or row.get("gate_evidence") is not False:
            errors.append(f"{prefix}: a reservation cannot award learning evidence")
        for field in CARD_FIELDS:
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(f"{prefix}: missing action-card field {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--initial-sessions", type=Path)
    args = parser.parse_args()
    try:
        policy = json.loads(args.policy.read_text())
        errors = (validate_initial_sessions(policy, json.loads(args.initial_sessions.read_text()))
                  if args.initial_sessions else validate_policy(policy))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors,
                      "scope": "beginner-policy-only", "reset_activated": False}, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
