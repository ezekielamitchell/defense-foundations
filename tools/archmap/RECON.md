# Architecture map v3 — Phase 1 recon checkpoint

PHASE 1: Recon [blocked]

Changed: `tools/archmap/seed_model.json`, `tools/archmap/recon_report.json`, `tools/archmap/RECON.md`.

Evidence: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v tests.test_beginner_policy` → exit 0; 7 collected, 7 passed, 0 failed, 0 errored. Additional observed checks appear below.

Findings: the seed's `route` and `routeval` states cannot remain `tested` under the requested v3 rules and whitelist. See `tools/validate_curriculum_route.py:86-111` and `docs/architecture/CODEX_PROMPT.md:314,333-337`.

Open: Phase 1's semantic review is incomplete. Structural citation checks are complete. Phase 2 and all implementation phases have not started. The check whitelist also conflicts with the repository-only access/no-write rules.

Next: wait at the explicit stop point in `docs/architecture/CODEX_PROMPT.md:1024`. On continuation, settle the check restrictions, finish semantic verification, then create the anchored curated model.

## Why this phase stopped

Section 14.1 requires a stop when any maturity claim is wrong. The current map calls the curriculum route and route validator `tested`. Their seed evidence cites the inline `--self-test` cases. The whitelisted route command does not include that flag; the script only calls `self_test` when the flag is set. No unittest observation is bound to those nodes. A normal validator success cannot meet section 6.4's requirement for a check that collected and passed at least one test.

This is a v3 classification incompatibility. It does not establish that the historical self-tests never ran. The proposed v3 state is `implemented` until an allowed bound test observation qualifies, or an explicit sourced override is recorded.

## Discrepancy table

| Seed or brief claim | Current source/evidence | Required treatment |
|---|---|---|
| `route` and `routeval` are tested | `tools/validate_curriculum_route.py:104-110` runs the negative cases only with `--self-test`; whitelist omits it. | Derive implemented under the specified rules; do not carry the old state forward. |
| `beginner` is tested | 7 beginner tests passed now, but `CODEX_PROMPT.md:336` binds that unit check only to `policyval`. The standalone beginner command has no collected tests. | Follow the exact binding, or explicitly revise it before deriving maturity. |
| `projection` and `integrity` can retain tested from the old snapshot | Their bound unit check requires the private vault and writes temporary fixture files (`tests/test_phase0_integrity.py:138-159,236-252`). It was not run. | Mark the current result unavailable; do not copy old pass/error counts. |
| `syntax` is implemented | The seed lists no owned files and describes commands only. Section 6.4 rule 6 yields planned without an override. | Define ownership or a sourced override; do not silently special-case it. |
| External course platforms are not inferred | Seed `courses` belongs to `z-outside`; section 6.4 requires outside nodes to be inferred. | Mark inferred. |
| “Six inputs converge on the learner” | The seed has 7 incoming learner edges (`docs/architecture/index.html:562-563`). | Derive the count from the graph. |
| Existing page includes orbit, Rotate and Plan view | Controls at `docs/architecture/index.html:29-36` omit those views; camera at line 860 contains scale/translation only. | Build these as new features. |
| Every item has sources | Nodes, edges and payloads have sources; tiers, zones and all 8 tour stops do not. Risks are unsourced prose fields. | Complete provenance in curated data. |

## Citation audit

The immutable JSON seed is semantically identical to the current embedded `MODEL`: 34 nodes, 54 edges, 21 payloads and 8 tour stops. Values were preserved without reclassification.

- 189 source occurrences, representing 149 unique citation strings.
- 188 occurrences have existing repository files and valid line ranges.
- One citation has an existing file but no line range: `learning-materials/01-foundations/ultimate-rust-crash-course/ch07_invaders_project/notes.md`.
- No missing paths and no out-of-range spans.
- 14 occurrence-level anchor candidates match more than once and need more specific content anchors.
- These are structural results. They do not mean every claim is semantically verified; the required stop interrupted that review.

`recon_report.json` records every source occurrence, its initial anchor candidate, span and match count. It also records the starting Git status and protected-file SHA-256 values.

## Checks actually run

All commands used the repository root as cwd, `shell=False`, a 60-second timeout and `PYTHONDONTWRITEBYTECODE=1`.

| Command | Exit | Observed result |
|---|---:|---|
| `python3 tools/validate_beginner_policy.py` | 0 | PASS; test counts not applicable. |
| `python3 -m unittest -v tests.test_beginner_policy` | 0 | 7 collected, 7 passed, 0 failed, 0 errored. |
| `node --check mobile/app.js` | 0 | No syntax errors. |
| `node --check mobile/sw.js` | 0 | No syntax errors. |
| `git diff --check` | 0 | No whitespace errors in the tracked diff. |

The beginner validator and test source were inspected before execution. The tests mutate in-memory dictionaries and read repository files; they do not create fixture files.

## Checks not run

| Command | Source-level reason |
|---|---|
| `python3 tools/validate_phase0_integrity.py` | Reads private config and manifest at `tools/validate_phase0_integrity.py:145-147`; imports private code at lines 96-105 and 308-310. |
| `python3 tools/validate_curriculum_route.py` | Iterates both repository paths and private vault paths, then reads them at `tools/validate_curriculum_route.py:44-58`. |
| `python3 -m unittest -v tests.test_phase0_integrity` | Reads/imports private authority at `tests/test_phase0_integrity.py:152-159,236-252` and writes temporary fixtures at lines 138-149. |

No claim that the vault is absent was made. Its contents were not accessed. Prior “10 passed, 10 errored” results have not been reused.

Project 0 execution, full semantic verification, strict extraction, browser checks, live checks, first-frame timing and frame-time measurement were not run during this stopped phase.

## Preservation and precedence

Starting branch: `codex/aegis-beginner-reset-2026-09-19`; HEAD `2e13798e4fdc3bc2e476ab6938e0c5cd261066b3`; starting dirty status: 80 entries from `git status --short`.

Final status comparison adds only `?? tools/archmap/`; no starting status entry was removed. The five deleted Invaders audio paths remain deleted. The current map, protected `docs/architecture.html`, prompt and projection JSON are all byte-identical to their starting SHA-256 values. No Git write command ran.

The standing endr routing instructions supplied with AGENTS required reading the two endr governance/routing instruction files. That was the only instruction-read exception to the repository boundary, following the brief's explicit AGENTS precedence. No private Aegis vault contents were read. The explicit output destinations keep the technical deliverables in this repository.

## Continuation proposal

Keep the private-vault boundary. Correct maturity using the stated rules, mark excluded checks as unavailable, and use a repository-contained observation path for any additional checks. The exact whitelist currently cannot satisfy all requested checks without violating the boundary; a change to that requirement needs an explicit continuation decision. Do not modify the original validators or protected projection consumer.

Files written in this phase:

- `tools/archmap/seed_model.json`
- `tools/archmap/recon_report.json`
- `tools/archmap/RECON.md`


## Continuation

The user subsequently requested full completion and a vector-like 3D space. The v3 implementation continues this checkpoint with current source-derived maturity, explicit unavailable checks and repository-only receipt-contract observations. The immutable seed and original audit remain above for provenance. See `README.md` and `VERIFICATION.md` for the completed implementation and final observed results.
