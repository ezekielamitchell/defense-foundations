from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = ROOT / "tools/validate_phase0_integrity.py"
SPEC = importlib.util.spec_from_file_location("phase0_integrity", MODULE_PATH)
assert SPEC and SPEC.loader
integrity = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(integrity)


class Phase0ProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Proof checks need private identities; the public JSON deliberately
        # contains no dates, native IDs, or current-period pairing map.
        cls.projection, _, _ = integrity.current_private_and_public_projection(integrity.DEFAULT_VAULT)

    def receipt(self):
        digest = "sha256:" + "a" * 64
        proof_date = self.projection["technical_dates"][0]
        pairing = self.projection.get("pairing") or {}
        pair_identity = (
            (pairing.get("technical_date_pair_cycles") or {}).get(proof_date)
            if pairing.get("identity_model") == "weekly_pair_cycle_id"
            else None if pairing.get("identity_model") == "beginner_checkpoint"
            else f"P0-PAIR-{proof_date}"
        )
        return {
            "schema_version": "phase0-proof.v1",
            "reset_id": self.projection["authority"]["reset_id"],
            "date": proof_date,
            "pair_slice_id": pair_identity,
            "artifact_paths": ["README.md"],
            "command_results": [
                {
                    "command": "python3 -m unittest tests/test_phase0_integrity.py",
                    "working_directory": str(ROOT),
                    "exit_code": 0,
                    "expected_exit_code": 0,
                    "output_digest": digest,
                }
            ],
            "observed_output_digest": digest,
            "test_count": 1,
            "changed_paths": ["README.md"],
            "verdict": "verified",
            "blocker": None,
            "course_resume_point": None,
            "next_command": f'cd "{ROOT}" && git status --short',
            "evidence_basis": {
                "artifacts_observed": True,
                "commands_observed": True,
                "schedule_only": False,
                "task_state_only": False,
            },
        }

    def test_verified_receipt_with_observed_test_passes(self):
        self.assertEqual(integrity.validate_proof(self.receipt(), self.projection, ROOT), [])

    def test_beginner_receipt_cannot_invent_pairing(self):
        projection = copy.deepcopy(self.projection)
        projection["pairing"] = {"identity_model": "beginner_checkpoint"}
        receipt = self.receipt()
        receipt["pair_slice_id"] = "P0-PAIR-INVENTED"
        self.assertIn("beginner proof must not invent a paired slice before prerequisites",
                      integrity.validate_proof(receipt, projection, ROOT))

    def test_zero_test_verified_receipt_is_rejected(self):
        receipt = self.receipt()
        receipt["test_count"] = 0
        errors = integrity.validate_proof(receipt, self.projection, ROOT)
        self.assertIn("verified proof requires at least one collected test", errors)

    def test_missing_output_verified_receipt_is_rejected(self):
        receipt = self.receipt()
        receipt["observed_output_digest"] = None
        receipt["command_results"][0]["output_digest"] = ""
        errors = integrity.validate_proof(receipt, self.projection, ROOT)
        self.assertTrue(any("output digest" in error for error in errors))

    def test_schedule_only_verified_receipt_is_rejected(self):
        receipt = self.receipt()
        receipt["evidence_basis"]["schedule_only"] = True
        errors = integrity.validate_proof(receipt, self.projection, ROOT)
        self.assertIn("schedule/task state cannot be proof", errors)

    def test_unverified_zero_test_receipt_is_allowed(self):
        receipt = self.receipt()
        receipt.update(
            verdict="unverified",
            artifact_paths=[],
            command_results=[],
            observed_output_digest=None,
            test_count=0,
            blocker="tests have not been written",
        )
        receipt["evidence_basis"].update(artifacts_observed=False, commands_observed=False)
        self.assertEqual(integrity.validate_proof(receipt, self.projection, ROOT), [])

    def test_verified_receipt_cannot_escape_repository(self):
        receipt = self.receipt()
        receipt["artifact_paths"] = ["../outside.txt"]
        errors = integrity.validate_proof(receipt, self.projection, ROOT)
        self.assertTrue(any("escapes its workspace" in error for error in errors))

    def test_unknown_receipt_field_is_rejected(self):
        receipt = self.receipt()
        receipt["calendar_complete"] = True
        errors = integrity.validate_proof(receipt, self.projection, ROOT)
        self.assertTrue(any("unsupported fields" in error for error in errors))

    def test_weekly_pair_cycle_identity_is_accepted_through_legacy_proof_field(self):
        projection = copy.deepcopy(self.projection)
        proof_date = projection["technical_dates"][0]
        cycle = "P0-PAIR-CYCLE-TEST"
        projection["pairing"] = {
            "identity_model": "weekly_pair_cycle_id",
            "technical_date_pair_cycles": {proof_date: cycle},
            "pair_cycles": [{"pair_cycle_id": cycle, "dates": [proof_date]}],
        }
        receipt = self.receipt()
        receipt["pair_slice_id"] = cycle
        self.assertEqual(integrity.validate_proof(receipt, projection, ROOT), [])

        receipt["pair_slice_id"] = f"P0-PAIR-{proof_date}"
        errors = integrity.validate_proof(receipt, projection, ROOT)
        self.assertIn("proof pair_slice_id does not match the active weekly pair_cycle_id", errors)


class ProjectionMarkerTests(unittest.TestCase):
    def test_current_public_projection_matches_private_authority_without_private_fields(self):
        path = ROOT / "docs/aegis-phase0-projection.json"
        projection = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(projection["schema_version"], integrity.PUBLIC_PROJECTION_SCHEMA)
        self.assertEqual(integrity.validate_projection(projection, path, integrity.DEFAULT_VAULT, ROOT), [])

        tampered = copy.deepcopy(projection)
        tampered["source"]["schedule"] = "/Users/private/calendar"
        self.assertIn(
            "public projection differs from validated private authority's allowlist",
            integrity.validate_projection(tampered, path, integrity.DEFAULT_VAULT, ROOT),
        )

    def test_marker_hash_drift_is_detectable(self):
        payload = b'{"schema_version":"aegis.phase0-projection.v1"}\n'
        digest = integrity.hashlib.sha256(payload).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            projection = root / "projection.json"
            projection.write_bytes(payload)
            consumer = root / "consumer.md"
            consumer.write_text(
                f"{integrity.MARKER_START}\n<!-- projection-json-sha256: {digest} -->\n{integrity.MARKER_END}\n"
            )
            self.assertIn(f"projection-json-sha256: {digest}", consumer.read_text())
            projection.write_bytes(payload + b" ")
            self.assertNotIn(f"projection-json-sha256: {integrity.sha256(projection)}", consumer.read_text())

    def test_real_v5_projection_source_passes_integrity_contract(self):
        exporter_path = integrity.DEFAULT_VAULT / "08_Assistant/scripts/export_defense_foundations_projection.py"
        exporter_spec = importlib.util.spec_from_file_location("phase0_projection_export_test", exporter_path)
        assert exporter_spec and exporter_spec.loader
        exporter = importlib.util.module_from_spec(exporter_spec)
        exporter_spec.loader.exec_module(exporter)
        manifest_path = integrity.DEFAULT_VAULT / "08_Assistant/manifests/2026-09-05 0000 Phase 0 Full Reset Manifest.json"
        manifest_bytes = manifest_path.read_bytes()
        manifest = json.loads(manifest_bytes)
        digest = integrity.hashlib.sha256(manifest_bytes).hexdigest()
        rows = manifest["events"]
        technical_dates = sorted({row["date"] for row in rows if row["lane"] in {"python", "rust"}})
        launch = manifest["capacity"]["weekly"]["launch"]["date_window"]
        first_week = manifest["fixed_gates"]["first_full_week"]
        review = manifest["fixed_gates"]["final_capability_review"]
        config = {
            "active_calendar_manifest": "manifest.json",
            "active_calendar_manifest_sha256": digest,
            "calendar_reset_id": manifest["reset_id"],
            "reset_cutover": manifest["boundary"],
            "manifest_horizon_cutoff": manifest["date_window"]["cutoff"],
            "active_calendar_event_count": len(rows),
            "technical_day_count": len(technical_dates),
            "python_daily_block_count": sum(row["lane"] == "python" for row in rows),
            "rust_daily_block_count": sum(row["lane"] == "rust" for row in rows),
            "agent_harness_daily_block_count": 0,
            "launch_window_start": launch[0],
            "launch_window_end": launch[1],
            "first_full_week_start": first_week[0],
            "first_full_week_end": first_week[1],
            "final_capability_review_window": f"{exporter.clock(review[0])}-{exporter.clock(review[1])}",
        }
        projection = exporter.build_projection(config, manifest, digest)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            vault = root / "vault"
            repository = root / "repository"
            (vault / "01_Daily").mkdir(parents=True)
            (vault / "manifest.json").write_bytes(manifest_bytes)
            (vault / "01_Daily/_Phase Config.md").write_text(
                "---\n"
                f"calendar_reset_id: {manifest['reset_id']}\n"
                f"reset_cutover: {manifest['boundary']}\n"
                f"manifest_horizon_cutoff: {manifest['date_window']['cutoff']}\n"
                "active_calendar_manifest: manifest.json\n"
                f"active_calendar_manifest_sha256: {digest}\n"
                "---\n",
                encoding="utf-8",
            )
            projection_path = repository / "docs/aegis-phase0-projection.json"
            projection_path.parent.mkdir(parents=True)
            payload = (json.dumps(projection, indent=2, ensure_ascii=False) + "\n").encode()
            projection_path.write_bytes(payload)
            marker_digest = integrity.hashlib.sha256(payload).hexdigest()
            marker = (
                f"{integrity.MARKER_START}\n"
                f"<!-- projection-json-sha256: {marker_digest} -->\n"
                f"{integrity.MARKER_END}\n"
            )
            for relative in [*projection["consumer_contract"]["documents"], "docs/architecture.html"]:
                path = repository / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(marker, encoding="utf-8")
            (repository / "mobile/app.js").write_text(
                '../docs/aegis-phase0-projection.json\nfetch("")\nlocalStorage.removeItem(storageKeys.notes)\n',
                encoding="utf-8",
            )
            (repository / "mobile/index.html").write_text("", encoding="utf-8")
            (repository / "mobile/sw.js").write_text(
                'PROJECTION_PATH = "/docs/aegis-phase0-projection.json"\n'
                "networkFirstProjection\nfetch(request)\nawait cache.put(request, response.clone())\n"
                "const cached = await caches.match(request)\nurl.pathname.endsWith(PROJECTION_PATH)\n",
                encoding="utf-8",
            )
            self.assertEqual(
                integrity.validate_projection(projection, projection_path, vault, repository),
                [],
            )


class ProjectionScheduleAuthorityTests(unittest.TestCase):
    """Use the preserved accepted v2 chain; never edit active source files."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.vault = Path(self.tmp.name)
        prefix = "08_Assistant/manifests/2026-09-08 0000 "
        names = {
            "manifest": prefix + "Phase 0 Full Reset Manifest.json",
            "amendment": prefix + "Week Reflow Amendment.json",
            "readback": prefix + "Week Reflow Readback.json",
            "proposal": prefix + "Week Reflow Proposal.json",
            "approval": prefix + "Week Reflow Approval.json",
        }
        self.paths = names
        for relative in names.values():
            path = self.vault / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((integrity.DEFAULT_VAULT / relative).read_bytes())
        self.manifest = integrity.load_json(self.vault / names["manifest"])
        self.config = {}
        for key, name in (
            ("active_calendar_manifest", "manifest"),
            ("active_schedule_exception", "amendment"),
            ("active_schedule_exception_readback", "readback"),
        ):
            self.config[key] = names[name]
            self.config[key + "_sha256"] = integrity.sha256(self.vault / names[name])

    def load(self):
        return integrity.effective_projection_source(self.vault, self.config, self.manifest)

    def reseal(self, name, payload):
        path = self.vault / self.paths[name]
        path.write_text(json.dumps(payload), encoding="utf-8")
        return {"path": self.paths[name], "sha256": integrity.sha256(path)}

    def test_real_accepted_chain_preserves_base_and_validates_effective_totals(self):
        before = copy.deepcopy(self.manifest)
        effective, authority = integrity.effective_projection_source(
            integrity.DEFAULT_VAULT, self.config, self.manifest
        )
        self.assertEqual(self.manifest, before)
        self.assertEqual(len(self.manifest["events"]), 253)
        self.assertEqual(len(effective["events"]), 254)
        self.assertEqual(effective["current_period_truth"], before["current_period_truth"])
        self.assertEqual(effective["fixed_gates"], before["fixed_gates"])
        self.assertEqual(effective["endr"], before["endr"])
        self.assertEqual(effective["capacity"]["total_minutes"], 26495)
        self.assertEqual(authority["base_event_count"], 253)
        self.assertEqual(authority["effective_event_count"], 254)
        self.assertTrue(authority["readback_verified"])
        self.assertEqual(authority["sha256"], self.config["active_schedule_exception_sha256"])
        self.assertEqual(authority["readback_sha256"], self.config["active_schedule_exception_readback_sha256"])

    def test_tampered_amendment_or_readback_bytes_fail_closed(self):
        for name in ("amendment", "readback"):
            with self.subTest(name=name):
                path = self.vault / self.paths[name]
                original = path.read_bytes()
                path.write_bytes(original + b" ")
                with self.assertRaisesRegex(ValueError, "hash"):
                    self.load()
                path.write_bytes(original)

    def test_partial_amendment_configuration_fails_closed(self):
        self.config.pop("active_schedule_exception_sha256")
        with self.assertRaisesRegex(ValueError, "partially configured"):
            self.load()

    def test_missing_accepted_readback_is_not_treated_as_a_prepared_plan(self):
        self.config.pop("active_schedule_exception_readback")
        self.config.pop("active_schedule_exception_readback_sha256")
        with self.assertRaisesRegex(ValueError, "activation requires"):
            self.load()

    def test_orphan_readback_cannot_silently_restore_the_baseline(self):
        self.config.pop("active_schedule_exception")
        self.config.pop("active_schedule_exception_sha256")
        with self.assertRaisesRegex(ValueError, "without an active amendment"):
            self.load()

    def test_rehashed_but_unapproved_amendment_is_rejected(self):
        approval = integrity.load_json(self.vault / self.paths["approval"])
        approval["status"] = "PREPARED"
        amendment = integrity.load_json(self.vault / self.paths["amendment"])
        amendment["approval"] = self.reseal("approval", approval)
        link = self.reseal("amendment", amendment)
        self.config["active_schedule_exception_sha256"] = link["sha256"]
        with self.assertRaisesRegex(ValueError, "approval"):
            self.load()

    def test_rehashed_operation_not_in_approved_proposal_is_rejected(self):
        amendment = integrity.load_json(self.vault / self.paths["amendment"])
        amendment["operations"][0]["after_fields"]["title"] = "Unapproved title"
        link = self.reseal("amendment", amendment)
        self.config["active_schedule_exception_sha256"] = link["sha256"]
        with self.assertRaisesRegex(ValueError, "exact approved proposal"):
            self.load()

    def test_sealed_manifest_contract_is_checked_before_the_overlay(self):
        self.manifest["current_period_truth"]["foundation_evidence"] = 1
        with self.assertRaisesRegex(ValueError, "sealed manifest contract"):
            self.load()

    def test_active_projection_retains_all_integrity_checks(self):
        path = ROOT / "docs/aegis-phase0-projection.json"
        projection = integrity.load_json(path)
        self.assertEqual(integrity.validate_projection(projection, path, integrity.DEFAULT_VAULT, ROOT), [])
        # The public artifact has no binding, counts, native IDs, or dates. The
        # validator derives it afresh from the validated private authority.
        for mutation in ("phase", "evidence", "source"):
            changed = copy.deepcopy(projection)
            if mutation == "phase":
                changed["phase"]["active"] = "P1"
            elif mutation == "evidence":
                changed["evidence"]["verified_current_period_foundation_work"] = 1
            else:
                changed["source"]["schedule"] = "an invented public schedule"
            with self.subTest(mutation=mutation):
                errors = integrity.validate_projection(changed, path, integrity.DEFAULT_VAULT, ROOT)
                self.assertIn("public projection differs from validated private authority's allowlist", errors)


if __name__ == "__main__":
    unittest.main()
