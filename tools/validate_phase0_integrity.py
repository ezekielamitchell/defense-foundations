#!/usr/bin/env python3
"""Validate generated Phase 0 projections and observed proof receipts.

This checker is read-only. It fails closed on source-hash drift, marker drift,
stale active boundary language, or evidence receipts that infer success from
schedule/task state, zero collected tests, or missing observed output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
DEFAULT_PROJECTION = REPOSITORY / "docs/aegis-phase0-projection.json"
DEFAULT_VAULT = Path("/Users/house/aegis nexus")
PROJECTION_SCHEMA = "aegis.phase0-projection.v1"
PROOF_SCHEMA = "phase0-proof.v1"
MANIFEST_SCHEMA_V5 = "AEGIS-PHASE0-FULL-RESET-5.0"
MARKER_START = "<!-- AEGIS:PHASE0_PROJECTION:START -->"
MARKER_END = "<!-- AEGIS:PHASE0_PROJECTION:END -->"
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")

PWA_FILES = ("mobile/app.js", "mobile/index.html", "mobile/sw.js")
FORBIDDEN_ACTIVE_TEXT = (
    "FINAL-2026-09-03-0000-PHASE0",
    "2026-09-03T00:00:00-07:00",
    "2026-09-03 at 00:00",
    "September 3 at 00:00",
    "October 29 final",
    "final capability decision is October 29",
    "final capability review Oct 29",
    "2026-10-29T23:25:00-07:00",
    "323 events",
    "323 Research occurrences",
    "36 optional",
    "six-minute Day 0",
    "six-minute cap",
    "final-20260903-0000",
    "paper 16:00–17:00",
    "Python 17:15–17:40",
    "Rust 17:55–18:20",
    "149 technical events",
    "146 language/agent stages",
    "agent is cut on 19 dates",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def parse_frontmatter(path: Path) -> dict[str, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"invalid frontmatter: {path}")
    end = text.index("\n---\n", 4)
    result: dict[str, str | None] = {}
    for raw in text[4:end].splitlines():
        if not raw or raw[0].isspace() or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        result[key.strip()] = value or None
    return result


def manifest_horizon(manifest: dict) -> str | None:
    if manifest.get("schema_version") in {MANIFEST_SCHEMA_V5, "AEGIS-PHASE0-FULL-RESET-6.0"}:
        return (manifest.get("date_window") or {}).get("cutoff") or (manifest.get("fixed_gates") or {}).get("horizon_cutoff")
    return manifest.get("horizon_end")


def effective_projection_source(vault: Path, config: dict, manifest: dict) -> tuple[dict, dict | None]:
    """Validate the sealed source before resolving its accepted schedule overlay.

    Reuse the operating authority's read-only validators rather than weakening
    count checks or interpreting an amendment a second way in this repository.
    The code location is fixed; projection data never selects executable code.
    Missing authority code or any broken approval/readback link fails closed.
    """
    scripts = str(DEFAULT_VAULT / "08_Assistant/scripts")
    sys.path.insert(0, scripts)
    try:
        from export_defense_foundations_projection import (
            effective_projection_source as derive_projection_source,
            projection_manifest_contract,
        )
        from schedule_exception import load_effective_manifest
    finally:
        sys.path.remove(scripts)

    summary, valid = projection_manifest_contract(manifest)
    if not valid:
        raise ValueError("sealed manifest contract failed: " + "; ".join(summary["errors"]))
    if not config.get("active_schedule_exception") and any(
        config.get(key) for key in ("active_schedule_exception_readback", "active_schedule_exception_readback_sha256")
    ):
        raise ValueError("schedule readback is configured without an active amendment")
    effective, exception = load_effective_manifest(vault, config, manifest, require_readback=True)
    effective, derived = derive_projection_source(effective, exception, summary)
    if not exception:
        return effective, None
    authority = {
        "path": str(config["active_schedule_exception"]),
        "sha256": str(config["active_schedule_exception_sha256"]),
        "readback_path": str(config.get("active_schedule_exception_readback") or ""),
        "readback_sha256": str(config.get("active_schedule_exception_readback_sha256") or ""),
        "base_event_count": summary["event_count"],
        "effective_event_count": derived["event_count"],
        "status": exception["status"],
        "readback_verified": exception.get("readback_verified") is True,
        "readback_observed_at": exception.get("readback_observed_at"),
    }
    return effective, authority


def validate_projection(projection: dict, projection_path: Path, vault: Path, repository: Path) -> list[str]:
    errors: list[str] = []
    if projection.get("schema_version") != PROJECTION_SCHEMA:
        errors.append("unsupported projection schema")
        return errors

    try:
        authority = projection["authority"]
        counts = projection["counts"]
        period = projection["period"]
        checkpoints = projection["checkpoints"]
        evidence = projection["evidence"]
        consumer = projection["consumer_contract"]
        config = parse_frontmatter(vault / authority["config_path"])
        manifest_path = vault / authority["manifest_path"]
        manifest = load_json(manifest_path)
    except (KeyError, TypeError, ValueError, OSError, json.JSONDecodeError) as exc:
        return [f"projection/source load failed: {exc}"]

    manifest_digest = sha256(manifest_path)
    if manifest_digest != authority.get("manifest_sha256"):
        errors.append("projection manifest hash does not match source bytes")
    if config.get("active_calendar_manifest_sha256") != manifest_digest:
        errors.append("phase config active manifest hash does not match source bytes")
    if authority.get("config_path") != "01_Daily/_Phase Config.md":
        errors.append("projection does not use the canonical phase config")
    if authority.get("manifest_path") != config.get("active_calendar_manifest"):
        errors.append("projection manifest path does not match phase config")
    source_horizon = manifest_horizon(manifest)
    comparisons = {
        "reset id": (authority.get("reset_id"), config.get("calendar_reset_id"), manifest.get("reset_id")),
        "boundary": (authority.get("boundary"), config.get("reset_cutover"), manifest.get("boundary")),
        "horizon": (authority.get("horizon_end"), config.get("manifest_horizon_cutoff"), source_horizon),
    }
    for label, values in comparisons.items():
        if len(set(values)) != 1:
            errors.append(f"projection/config/manifest {label} mismatch")

    if errors:
        return errors
    try:
        manifest, schedule_authority = effective_projection_source(vault, config, manifest)
    except (ImportError, KeyError, TypeError, ValueError, OSError) as exc:
        return [f"projection schedule authority failed: {exc}"]
    if authority.get("schedule_exception") != schedule_authority:
        errors.append("projection schedule amendment/readback authority mismatch")

    active_rows = [row for row in manifest.get("events", []) if row.get("active") is True]
    expected_counts = {
        "events": len(active_rows),
        "python": sum(row.get("lane") == "python" for row in active_rows),
        "rust": sum(row.get("lane") == "rust" for row in active_rows),
        "optional_agents": sum(row.get("lane") == "agents" for row in active_rows),
        "foundation_gates": sum(row.get("lane") == "pair" for row in active_rows),
        "papers": sum(row.get("kind") == "paper" for row in active_rows),
        "endr_daily": sum(row.get("load_bucket") == "endr" for row in active_rows),
        "company_reviews": sum(row.get("kind") == "company-review" for row in active_rows),
        "closeout_review_rows": sum(row.get("load_bucket") == "overhead" for row in active_rows),
    }
    is_v5 = manifest.get("schema_version") == MANIFEST_SCHEMA_V5
    is_v6 = manifest.get("schema_version") == "AEGIS-PHASE0-FULL-RESET-6.0"
    technical_stage_lanes = {"python", "rust", "project"} if is_v6 else {"python", "rust"} if is_v5 else {"python", "rust", "agents"}
    technical_dates = sorted({row.get("date") for row in active_rows if row.get("lane") in technical_stage_lanes})
    expected_counts.update(
        technical_dates=len(technical_dates),
        technical_events=sum(row.get("lane") in technical_stage_lanes | {"pair"} for row in active_rows),
        technical_stages=sum(row.get("lane") in technical_stage_lanes for row in active_rows),
    )
    if is_v5:
        expected_counts.update(
            project_blocks=sum(row.get("kind") == "project-block" for row in active_rows),
            course_studios=sum(row.get("kind") == "course-studio" for row in active_rows),
            academic_study_blocks=sum(row.get("load_bucket") == "academic" for row in active_rows),
            degree_class_occurrences=int((manifest.get("degree") or {}).get("class_occurrence_count") or 0),
            pair_cycles=len({row.get("pair_cycle_id") for row in active_rows if row.get("pair_cycle_id")}),
        )
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            errors.append(f"projection count drift: {key}")

    if period.get("start") != str(authority.get("boundary", ""))[:10] or period.get("end") != str(authority.get("horizon_end", ""))[:10]:
        errors.append("projection period does not match boundary/horizon")
    if checkpoints.get("final_capability") != str(authority.get("horizon_end", ""))[:10]:
        errors.append("final capability date does not match horizon date")
    if any(value != 0 for value in (evidence.get("current_counters") or {}).values()):
        errors.append("projection current counters are not zero")
    if evidence.get("schedule_is_evidence") is not False or evidence.get("task_state_is_evidence") is not False:
        errors.append("projection weakens the evidence firewall")
    if projection.get("technical_dates") != technical_dates:
        errors.append("projection technical date list drift")

    if manifest.get("schema_version") == MANIFEST_SCHEMA_V5:
        pairing = projection.get("pairing") or {}
        source_cycle_rows: dict[str, list[dict]] = {}
        source_date_cycles: dict[str, str] = {}
        for row in active_rows:
            if row.get("lane") not in {"python", "rust", "pair"}:
                continue
            cycle = str(row.get("pair_cycle_id") or "")
            if not cycle:
                errors.append(f"v5 technical row lacks pair_cycle_id: {row.get('planned_event_key')}")
                continue
            source_cycle_rows.setdefault(cycle, []).append(row)
            existing = source_date_cycles.setdefault(str(row.get("date")), cycle)
            if existing != cycle:
                errors.append(f"v5 technical date has multiple pair cycles: {row.get('date')}")
        projected_cycles = pairing.get("pair_cycles") or []
        projected_cycle_map = {
            row.get("pair_cycle_id"): row
            for row in projected_cycles
            if isinstance(row, dict) and row.get("pair_cycle_id")
        }
        if pairing.get("identity_model") != "weekly_pair_cycle_id":
            errors.append("v5 projection does not use weekly_pair_cycle_id")
        if pairing.get("technical_date_pair_cycles") != source_date_cycles:
            errors.append("v5 projection technical-date pair-cycle mapping drift")
        if set(projected_cycle_map) != set(source_cycle_rows):
            errors.append("v5 projection pair-cycle inventory drift")
        for cycle, cycle_rows in source_cycle_rows.items():
            projected = projected_cycle_map.get(cycle) or {}
            expected_cycle = {
                "dates": sorted({row.get("date") for row in cycle_rows}),
                "python_events": sum(row.get("lane") == "python" for row in cycle_rows),
                "rust_events": sum(row.get("lane") == "rust" for row in cycle_rows),
                "gate_events": sum(row.get("lane") == "pair" for row in cycle_rows),
            }
            if any(projected.get(key) != value for key, value in expected_cycle.items()):
                errors.append(f"v5 projection pair-cycle detail drift: {cycle}")
        if counts.get("optional_agents") != 0:
            errors.append("v5 projection contains a recurring agent lane")
        capacity = projection.get("capacity") or {}
        source_capacity = manifest.get("capacity") or {}
        source_buckets = source_capacity.get("research_minutes_by_bucket") or {}
        degree_class_minutes = int((manifest.get("degree") or {}).get("class_minutes") or 0)
        expected_capacity = {
            "gross_minutes": source_capacity.get("total_minutes"),
            "mission_minutes": int(source_capacity.get("total_minutes") or 0) - int(source_buckets.get("overhead") or 0),
            "foundation_minutes": source_buckets.get("gate_foundation"),
            "agent_minutes": 0,
            "paper_minutes": source_buckets.get("paper"),
            "endr_minutes": source_buckets.get("endr"),
            "academic_minutes": int(source_buckets.get("academic") or 0) + degree_class_minutes,
            "degree_class_minutes": degree_class_minutes,
            "company_review_minutes": source_buckets.get("endr-review"),
            "overhead_minutes": source_buckets.get("overhead"),
        }
        for key, expected in expected_capacity.items():
            if capacity.get(key) != expected:
                errors.append(f"v5 projection capacity drift: {key}")
        projected_weekly = capacity.get("weekly") or []
        source_weekly = source_capacity.get("weekly") or {}
        projected_weekly_map = {
            row.get("source_key"): row
            for row in projected_weekly
            if isinstance(row, dict) and row.get("source_key")
        }
        if set(projected_weekly_map) != set(source_weekly):
            errors.append("v5 projection weekly capacity row count drift")
        for source_key, source in source_weekly.items():
            row = projected_weekly_map.get(source_key) or {}
            week_window = source.get("date_window") or []
            if len(week_window) != 2:
                errors.append(f"v5 source weekly window invalid: {source_key}")
                week_window = [None, None]
            expected_week = {
                "start": week_window[0],
                "end": week_window[1],
                "gross_minutes": source.get("total_minutes"),
                "research_calendar_minutes": source.get("research_calendar_minutes"),
                "degree_class_minutes": source.get("degree_class_minutes"),
            }
            if any(row.get(key) != value for key, value in expected_week.items()):
                errors.append(f"v5 projection weekly capacity drift: {source_key}")
            if row.get("gross_minutes", 0) > source_capacity.get("weekly_ceiling_minutes", 0):
                errors.append(f"v5 projection weekly ceiling exceeded: {row.get('source_key')}")

    if manifest.get("schema_version") == "AEGIS-PHASE0-FULL-RESET-6.0":
        from export_defense_foundations_projection import build_projection, read_frontmatter
        expected_projection = build_projection(read_frontmatter(vault / "01_Daily/_Phase Config.md"), manifest, manifest_digest, root=vault)
        if projection != expected_projection:
            errors.append("v6 projection differs from validated beginner authority")
        if projection.get("pairing", {}).get("identity_model") != "beginner_checkpoint":
            errors.append("v6 projection introduced premature pair identity")
        if any(w.get("research_calendar_minutes", 99999) > 3120 for w in projection["capacity"]["weekly"]):
            errors.append("v6 projection consumes the reserved weekly margin")

    projection_digest = sha256(projection_path)
    marker_digest = f"projection-json-sha256: {projection_digest}"
    documents = consumer.get("documents") or []
    if len(documents) != len(set(documents)) or not documents:
        errors.append("projection consumer document list is empty or duplicated")
    for relative in [*documents, "docs/architecture.html"]:
        path = repository / relative
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"projection consumer unavailable: {relative}: {exc}")
            continue
        if text.count(MARKER_START) != 1 or text.count(MARKER_END) != 1:
            errors.append(f"projection marker count invalid: {relative}")
        if marker_digest not in text:
            errors.append(f"projection marker hash drift: {relative}")
        for stale in FORBIDDEN_ACTIVE_TEXT:
            if stale in text:
                errors.append(f"stale active projection in {relative}: {stale}")

    for relative in PWA_FILES:
        path = repository / relative
        text = path.read_text(encoding="utf-8")
        for stale in FORBIDDEN_ACTIVE_TEXT:
            if stale in text:
                errors.append(f"stale PWA projection in {relative}: {stale}")
    app = (repository / "mobile/app.js").read_text(encoding="utf-8")
    if "../docs/aegis-phase0-projection.json" not in app or "fetch(" not in app:
        errors.append("mobile app does not load the generated projection")
    if "setTaskComplete" in app or "taskKey(" in app:
        errors.append("mobile app still owns a task-completion store")
    if "localStorage.removeItem(storageKeys.notes)" not in app:
        errors.append("mobile quick-capture behavior is unavailable")
    sw = (repository / "mobile/sw.js").read_text(encoding="utf-8")
    projection_freshness_contract = (
        'PROJECTION_PATH = "/docs/aegis-phase0-projection.json"',
        "networkFirstProjection",
        "fetch(request)",
        "await cache.put(request, response.clone())",
        "const cached = await caches.match(request)",
        "url.pathname.endsWith(PROJECTION_PATH)",
    )
    if any(token not in sw for token in projection_freshness_contract):
        errors.append("mobile projection is not network-first with an offline fallback")
    return errors


def safe_artifact_path(value: str, repository: Path) -> Path | None:
    path = Path(value)
    if any(part == ".." for part in path.parts):
        return None
    candidate = (path if path.is_absolute() else repository / path).resolve()
    return candidate if candidate.is_relative_to(repository.resolve()) else None


def validate_proof(receipt: dict, projection: dict, repository: Path) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version",
        "reset_id",
        "date",
        "pair_slice_id",
        "artifact_paths",
        "command_results",
        "observed_output_digest",
        "test_count",
        "changed_paths",
        "verdict",
        "blocker",
        "course_resume_point",
        "next_command",
        "evidence_basis",
    }
    missing = sorted(required - set(receipt))
    if missing:
        return ["proof missing fields: " + ", ".join(missing)]
    unexpected = sorted(set(receipt) - required)
    if unexpected:
        errors.append("proof has unsupported fields: " + ", ".join(unexpected))
    if receipt.get("schema_version") != PROOF_SCHEMA:
        errors.append("unsupported proof schema")
    if receipt.get("reset_id") != projection.get("authority", {}).get("reset_id"):
        errors.append("proof reset id does not match active projection")
    try:
        proof_date = date.fromisoformat(str(receipt.get("date")))
        start = date.fromisoformat(projection["period"]["start"])
        end = date.fromisoformat(projection["period"]["end"])
        if not start <= proof_date <= end:
            errors.append("proof date is outside the active period")
    except (TypeError, ValueError, KeyError):
        errors.append("proof date is invalid")
        proof_date = None
    pairing = projection.get("pairing") or {}
    if pairing.get("identity_model") == "weekly_pair_cycle_id":
        expected_pair = (pairing.get("technical_date_pair_cycles") or {}).get(str(receipt.get("date")))
        if not expected_pair or receipt.get("pair_slice_id") != expected_pair:
            errors.append("proof pair_slice_id does not match the active weekly pair_cycle_id")
    elif pairing.get("identity_model") == "beginner_checkpoint":
        if receipt.get("pair_slice_id") is not None:
            errors.append("beginner proof must not invent a paired slice before prerequisites")
    else:
        expected_pair = f"P0-PAIR-{receipt.get('date')}"
        if receipt.get("pair_slice_id") != expected_pair:
            errors.append("proof pair_slice_id does not match its date")
    if receipt.get("date") not in projection.get("technical_dates", []):
        errors.append("proof date is not an active technical date")

    verdict = receipt.get("verdict")
    if verdict not in {"verified", "partial", "blocked", "unverified"}:
        errors.append("proof verdict is invalid")
    test_count = receipt.get("test_count")
    if not isinstance(test_count, int) or isinstance(test_count, bool) or test_count < 0:
        errors.append("proof test_count must be a non-negative integer")
    artifacts = receipt.get("artifact_paths")
    commands = receipt.get("command_results")
    changes = receipt.get("changed_paths")
    if not isinstance(artifacts, list) or not all(isinstance(item, str) and item for item in artifacts):
        errors.append("proof artifact_paths must be a list of non-empty paths")
        artifacts = []
    if not isinstance(changes, list) or not all(isinstance(item, str) and item for item in changes):
        errors.append("proof changed_paths must be a list of non-empty paths")
        changes = []
    for value in [*artifacts, *changes]:
        if safe_artifact_path(value, repository) is None:
            errors.append(f"proof path escapes its workspace: {value}")

    if not isinstance(commands, list):
        errors.append("proof command_results must be a list")
        commands = []
    for index, command in enumerate(commands):
        if not isinstance(command, dict):
            errors.append(f"proof command result {index} is not an object")
            continue
        command_fields = {"command", "working_directory", "exit_code", "expected_exit_code", "output_digest"}
        missing_command = sorted(command_fields - set(command))
        unexpected_command = sorted(set(command) - command_fields)
        if missing_command:
            errors.append(f"proof command result {index} missing fields: {', '.join(missing_command)}")
        if unexpected_command:
            errors.append(f"proof command result {index} has unsupported fields: {', '.join(unexpected_command)}")
        if not str(command.get("command") or "").strip():
            errors.append(f"proof command result {index} has no command")
        workdir = str(command.get("working_directory") or "")
        if not workdir.startswith("/"):
            errors.append(f"proof command result {index} working directory is not absolute")
        elif safe_artifact_path(workdir, repository) is None:
            errors.append(f"proof command result {index} working directory is outside the repository")
        if not isinstance(command.get("exit_code"), int) or not isinstance(command.get("expected_exit_code"), int):
            errors.append(f"proof command result {index} exit codes are invalid")
        elif command["exit_code"] != command["expected_exit_code"]:
            errors.append(f"proof command result {index} did not meet its expected exit code")
        if not DIGEST.fullmatch(str(command.get("output_digest") or "")):
            errors.append(f"proof command result {index} has no valid observed output digest")

    basis = receipt.get("evidence_basis")
    if not isinstance(basis, dict):
        errors.append("proof evidence_basis must be an object")
        basis = {}
    basis_fields = {"artifacts_observed", "commands_observed", "schedule_only", "task_state_only"}
    if isinstance(basis, dict):
        missing_basis = sorted(basis_fields - set(basis))
        unexpected_basis = sorted(set(basis) - basis_fields)
        if missing_basis:
            errors.append("proof evidence_basis missing fields: " + ", ".join(missing_basis))
        if unexpected_basis:
            errors.append("proof evidence_basis has unsupported fields: " + ", ".join(unexpected_basis))
    if basis.get("schedule_only") is not False or basis.get("task_state_only") is not False:
        errors.append("schedule/task state cannot be proof")
    if not str(receipt.get("next_command") or "").strip():
        errors.append("proof must end with one exact next command")

    if verdict == "verified":
        if not isinstance(test_count, int) or isinstance(test_count, bool) or test_count < 1:
            errors.append("verified proof requires at least one collected test")
        if not artifacts:
            errors.append("verified proof requires at least one artifact path")
        else:
            for value in artifacts:
                path = safe_artifact_path(value, repository)
                if path is not None and not path.exists():
                    errors.append(f"verified proof artifact does not exist: {value}")
        if not commands:
            errors.append("verified proof requires an observed command result")
        if not DIGEST.fullmatch(str(receipt.get("observed_output_digest") or "")):
            errors.append("verified proof requires a valid observed output digest")
        if receipt.get("blocker") is not None:
            errors.append("verified proof cannot retain a blocker")
        if basis.get("artifacts_observed") is not True or basis.get("commands_observed") is not True:
            errors.append("verified proof requires observed artifacts and commands")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projection", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--repository", type=Path, default=REPOSITORY)
    parser.add_argument("--proof", type=Path)
    args = parser.parse_args()

    projection = load_json(args.projection)
    errors = validate_projection(projection, args.projection, args.vault, args.repository)
    if args.proof:
        errors.extend(validate_proof(load_json(args.proof), projection, args.repository))
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
