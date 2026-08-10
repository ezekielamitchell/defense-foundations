# Phase 0 — Local Issue Ledger

Local issue ledger for Phase 0. **These are not GitHub issues** and no GitHub issue number is implied or invented. The IDs below are the exact `P0-W*` labels referenced by the validated Phase 0 calendar manifest, so an issue ID in a calendar block resolves here.

| Field | Value |
|---|---|
| Repository | `defense-foundations`, branch `main` |
| Phase | P0 — Engineering Foundation Gate |
| Window | 2026-08-09 16:00 → 2026-09-13 |
| Date authority | Aegis Nexus `01_Daily/_Phase Config.md` (DD #85) |
| Source | `00_Inbox/2026-08-09 Phase 0 Hard Reset Calendar Manifest.json` |
| Issue count | **57** |

## Conventions

- **ID format:** `P0-W<week>-<track>`. Track codes: `D0` Day 0 · `P`/`P2` Python · `R`/`R1`/`R2` Rust · `L`/`L1` Linux/Git/CI · `V` verification · `C` paired comparison · `CV` OpenCV sampler · `HF` Hugging Face agent sampler. A bare `P0-W<n>` is that week's operations/review issue.
- **Sub-issues** may be numbered under a parent, e.g. `P0-W2-R-01`.
- **Status values:** `not-started` · `in-progress` · `blocked` · `done` · `superseded-historical`.
- **Gate credit:** only issues marked `yes` contribute to the P0 foundation gate. Sampler and operations issues never do.
- **Evidence before CI exists:** `.github/` does not exist in this repository yet. Cite **local check/test output** with the exact command line. A GitHub Actions run URL may only be cited after the workflow is committed (`P0-W4-L`).
- **Do not mark an issue `done` without its acceptance test passing.** A calendar block elapsing is not completion.

## The Phase 0 artifact

A paired **file-statistics** CLI:

- **Python:** `projects/file_stats` — `pyproject.toml` exists and declares pytest + ruff with `testpaths = ["tests"]`; `tests/` does not exist yet and `main.py` is a greeting stub.
- **Rust:** `projects/hello-stats` — `Cargo.toml` exists (edition 2024) with an empty `[dependencies]`; `src/main.rs` is greeting WIP with no tests.

## Issues

> **A20 boundary:** The five `P0-W1*` entries immediately below are retained only to resolve the five elapsed Research-calendar events preserved before the 2026-08-09 16:00 cutover. They are superseded history, earn zero A20 credit, and are not active work. Active foundation execution begins with `P0-W2*` on 2026-08-10.

### `P0-W1-D0`

| Field | Value |
|---|---|
| **Week** | 1 (A20 cutover 2026-08-09; first foundation build is Week 2 on 2026-08-10) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | bootstrap the paired repository and the Python typed-CLI contract |
| **Acceptance test** | `uv run pytest` collects and passes at least one test; valid-path and missing-path both run from the command line |
| **Evidence** | commit hash, two fixtures, first passing test, and the exact command transcript |
| **Dependencies** | P0 reset boundary at 18:00 and local Python toolchain |
| **Counts toward P0 gate** | yes |
| **Status** | `superseded-historical` |

### `P0-W1-R1`

| Field | Value |
|---|---|
| **Week** | 1 (first scheduled 2026-08-07) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | bootstrap the paired repository and the Python typed-CLI contract |
| **Acceptance test** | `cargo build` and `cargo test` both succeed and `--help` prints the documented flags |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `superseded-historical` |

### `P0-W1-L1`

| Field | Value |
|---|---|
| **Week** | 1 (first scheduled 2026-08-07) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | bootstrap the paired repository and the Python typed-CLI contract |
| **Acceptance test** | the branch diff is reviewable and the shell transcript is saved in the repository |
| **Evidence** | branch name, diff output, transcript file, and CI stub commit |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `superseded-historical` |

### `P0-W1`

| Field | Value |
|---|---|
| **Week** | 1 (first scheduled 2026-08-07) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `superseded-historical` |

### `P0-W1-C`

| Field | Value |
|---|---|
| **Week** | 1 (first scheduled 2026-08-08) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | bootstrap the paired repository and the Python typed-CLI contract |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `superseded-historical` |

### `P0-W2-R`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-10) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | `cargo test` passes and `clippy`/`rustfmt` report no new findings |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-10) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W2-P`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-11) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | `pytest` passes and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2-CV`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-11) |
| **Class** | `[SAMPLER-CV]` |
| **Project** | `sampler (non-gate)` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | valid fixture round-trips and a non-image path is rejected with a typed error |
| **Evidence** | small script, test fixture, timing note, and one limitations line |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W2-R2`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-12) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | `cargo test` passes and the typed error path is covered by at least one test |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures; Rustlings progress recorded separately from the historical course |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2-L`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-12) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | the branch diff is reviewable and the CI/check command output is recorded |
| **Evidence** | branch diff, local check output, and the shell transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2-P2`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-13) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | `pytest` passes for every malformed fixture and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, fixture list, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2-HF`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-13) |
| **Class** | `[SAMPLER-HF-AGENT]` |
| **Project** | `learning-materials/12-agent-engineering/hugging-face-agents-course` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | tool returns a typed record for a valid note path, raises a typed error for a missing path, and its docstring states it performs no writes and no network access |
| **Evidence** | tool source, typed signature, deterministic test input, malformed-input test, full trace file, and one line stating what the tool is NOT authorized to do |
| **Dependencies** | Existing P0 Python toolchain; the tool operates on local Aegis notes, test logs, or telemetry fixtures only - never on consequential data |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W2-V`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-14) |
| **Class** | `[P0-VERIFY]` |
| **Project** | `both projects` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | at least one targeted test or check is added or improved and its raw output is saved |
| **Evidence** | test result, structured error/log sample, diff inspection, and the issue update |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W2-C`

| Field | Value |
|---|---|
| **Week** | 2 (first scheduled 2026-08-15) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | complete the Rust CLI happy path and the Python validation surface |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-R`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-17) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | `cargo test` passes and `clippy`/`rustfmt` report no new findings |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-17) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W3-P`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-18) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | `pytest` passes and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-CV`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-18) |
| **Class** | `[SAMPLER-CV]` |
| **Project** | `sampler (non-gate)` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | frame count matches the source and the timing log has one row per frame |
| **Evidence** | small script, test fixture, timing note, and one limitations line |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W3-R2`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-19) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | `cargo test` passes and the typed error path is covered by at least one test |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures; Rustlings progress recorded separately from the historical course |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-L`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-19) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | the branch diff is reviewable and the CI/check command output is recorded |
| **Evidence** | branch diff, local check output, and the shell transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-P2`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-20) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | `pytest` passes for every malformed fixture and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, fixture list, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-HF`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-20) |
| **Class** | `[SAMPLER-HF-AGENT]` |
| **Project** | `learning-materials/12-agent-engineering/hugging-face-agents-course` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | a fixed input produces a byte-identical trace across two runs and the loop halts at the documented maximum step count |
| **Evidence** | tool source, typed signature, deterministic test input, malformed-input test, full trace file, and one line stating what the tool is NOT authorized to do |
| **Dependencies** | Existing P0 Python toolchain; the tool operates on local Aegis notes, test logs, or telemetry fixtures only - never on consequential data |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W3-V`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-21) |
| **Class** | `[P0-VERIFY]` |
| **Project** | `both projects` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | at least one targeted test or check is added or improved and its raw output is saved |
| **Evidence** | test result, structured error/log sample, diff inspection, and the issue update |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W3-C`

| Field | Value |
|---|---|
| **Week** | 3 (first scheduled 2026-08-22) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | reconcile the Python/Rust output contract and add schema-validation cases |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-R`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-24) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | `cargo test` passes and `clippy`/`rustfmt` report no new findings |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-24) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W4-P`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-25) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | `pytest` passes and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-CV`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-25) |
| **Class** | `[SAMPLER-CV]` |
| **Project** | `sampler (non-gate)` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | the emitted record is deterministic for a fixed fixture and is explicitly marked non-gate sampler output |
| **Evidence** | small script, test fixture, timing note, and one limitations line |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W4-R2`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-26) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | `cargo test` passes and the typed error path is covered by at least one test |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures; Rustlings progress recorded separately from the historical course |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-L`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-26) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | the branch diff is reviewable and the CI/check command output is recorded |
| **Evidence** | branch diff, GitHub Actions run URL, and the shell transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-P2`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-27) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | `pytest` passes for every malformed fixture and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, fixture list, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-HF`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-27) |
| **Class** | `[SAMPLER-HF-AGENT]` |
| **Project** | `learning-materials/12-agent-engineering/hugging-face-agents-course` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | replaying a saved trace reproduces every observation, and a malformed trace record is rejected with a typed error rather than being partially applied |
| **Evidence** | tool source, typed signature, deterministic test input, malformed-input test, full trace file, and one line stating what the tool is NOT authorized to do |
| **Dependencies** | Existing P0 Python toolchain; the tool operates on local Aegis notes, test logs, or telemetry fixtures only - never on consequential data |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W4-V`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-28) |
| **Class** | `[P0-VERIFY]` |
| **Project** | `both projects` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | at least one targeted test or check is added or improved and its raw output is saved |
| **Evidence** | test result, structured error/log sample, diff inspection, and the issue update |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W4-C`

| Field | Value |
|---|---|
| **Week** | 4 (first scheduled 2026-08-29) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | harden malformed-input behavior, CI checks, and deterministic replay |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-R`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-08-31) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | `cargo test` passes and `clippy`/`rustfmt` report no new findings |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-08-31) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W5-P`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-01) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | `pytest` passes and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-CV`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-01) |
| **Class** | `[SAMPLER-CV]` |
| **Project** | `sampler (non-gate)` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | the pipeline is deterministic on a fixed fixture and the timing note records p50 over 10 runs |
| **Evidence** | small script, test fixture, timing note, and one limitations line |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W5-R2`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-02) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | `cargo test` passes and the typed error path is covered by at least one test |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures; Rustlings progress recorded separately from the historical course |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-L`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-02) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | the branch diff is reviewable and the CI/check command output is recorded |
| **Evidence** | branch diff, GitHub Actions run URL, and the shell transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-P2`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-03) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | `pytest` passes for every malformed fixture and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, fixture list, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-HF`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-03) |
| **Class** | `[SAMPLER-HF-AGENT]` |
| **Project** | `learning-materials/12-agent-engineering/hugging-face-agents-course` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | the run completes within the documented step budget, the saved trace names every tool call, and the permission list contains no write or network capability |
| **Evidence** | tool source, typed signature, deterministic test input, malformed-input test, full trace file, and one line stating what the tool is NOT authorized to do |
| **Dependencies** | Existing P0 Python toolchain; the tool operates on local Aegis notes, test logs, or telemetry fixtures only - never on consequential data |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W5-V`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-04) |
| **Class** | `[P0-VERIFY]` |
| **Project** | `both projects` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | at least one targeted test or check is added or improved and its raw output is saved |
| **Evidence** | test result, structured error/log sample, diff inspection, and the issue update |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W5-C`

| Field | Value |
|---|---|
| **Week** | 5 (first scheduled 2026-09-05) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | prove cold-run recreation, benchmark both CLIs, and close minimum-gate gaps |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-R`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-07) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | `cargo test` passes and `clippy`/`rustfmt` report no new findings |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-07) |
| **Class** | `[OPS]` |
| **Project** | `repo-wide` |
| **Objective** | daily evidence closeout |
| **Acceptance test** | the evidence row names a command/test result, a commit/diff, and an exact next action |
| **Evidence** | dated evidence row and next-action note |
| **Dependencies** | same-day build, verification, and sampler results |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W6-P`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-08) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | `pytest` passes and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-CV`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-08) |
| **Class** | `[SAMPLER-CV]` |
| **Project** | `sampler (non-gate)` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | both malformed fixtures are rejected and the limitations line is written into the sampler README |
| **Evidence** | small script, test fixture, timing note, and one limitations line |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W6-R2`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-09) |
| **Class** | `[P0-RUST]` |
| **Project** | `projects/hello-stats` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | `cargo test` passes and the typed error path is covered by at least one test |
| **Evidence** | commit hash, `cargo test` output, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures; Rustlings progress recorded separately from the historical course |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-L`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-09) |
| **Class** | `[P0-LINUX/GIT/CI]` |
| **Project** | `repo-wide` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | the branch diff is reviewable and the CI/check command output is recorded |
| **Evidence** | branch diff, GitHub Actions run URL, and the shell transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-P2`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-10) |
| **Class** | `[P0-PYTHON]` |
| **Project** | `projects/file_stats` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | `pytest` passes for every malformed fixture and `ruff` reports no new findings |
| **Evidence** | commit hash, `pytest` output, fixture list, and the exact command transcript |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-HF`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-10) |
| **Class** | `[SAMPLER-HF-AGENT]` |
| **Project** | `learning-materials/12-agent-engineering/hugging-face-agents-course` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | the harness reports a completeness rate, a violation count of zero on the clean fixture, and a non-zero violation count on the adversarial fixture |
| **Evidence** | tool source, typed signature, deterministic test input, malformed-input test, full trace file, and one line stating what the tool is NOT authorized to do |
| **Dependencies** | Existing P0 Python toolchain; the tool operates on local Aegis notes, test logs, or telemetry fixtures only - never on consequential data |
| **Counts toward P0 gate** | no — non-gate overlay/ops |
| **Status** | `not-started` |

### `P0-W6-V`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-11) |
| **Class** | `[P0-VERIFY]` |
| **Project** | `both projects` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | at least one targeted test or check is added or improved and its raw output is saved |
| **Evidence** | test result, structured error/log sample, diff inspection, and the issue update |
| **Dependencies** | P0 repository baseline, local Python/Rust toolchains, versioned fixtures |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-W6-C`

| Field | Value |
|---|---|
| **Week** | 6 (first scheduled 2026-09-12) |
| **Class** | `[P0-COMPARE]` |
| **Project** | `both projects` |
| **Objective** | remediate remaining gate evidence and assemble the maximum-gate decision package |
| **Acceptance test** | the comparison note identifies one correct boundary for Python and one justified Rust ownership candidate, each backed by an observation rather than an opinion |
| **Evidence** | comparison table, benchmark observations, cross-language fixtures, and README update |
| **Dependencies** | passing or intentionally failing fixtures from the current week |
| **Counts toward P0 gate** | yes |
| **Status** | `not-started` |

### `P0-GATE-6W`

| Field | Value |
|---|---|
| **Date** | 2026-08-30 |
| **Class** | `[P0][GATE]` |
| **Project** | `repo-wide` |
| **Objective** | issue the written minimum-gate decision without promoting P1 automatically |
| **Acceptance test** | every Phase 0 exit-gate line has `PASS`, `PARTIAL PASS`, or `REMEDIATION REQUIRED`, with an evidence path or named recovery block |
| **Evidence** | dated decision entry and per-line evidence paths in the Aegis Phase 0 evidence package |
| **Dependencies** | only fresh A20 proof; Rustlings first-50 state recorded; sampler, agent, endr, and research evidence excluded |
| **Counts toward P0 gate** | no — evaluates the gate rather than supplying artifact credit |
| **Status** | `not-started` |

### `P0-GATE-8W`

| Field | Value |
|---|---|
| **Date** | 2026-09-13 |
| **Class** | `[P0][GATE]` |
| **Project** | `repo-wide` |
| **Objective** | issue the maximum-gate decision and a separately authorized promotion or extension record |
| **Acceptance test** | the record says `P0 PASSED` or `P0 EXTENDED`, identifies all evidence or remaining lines, and does not activate P1 by date alone |
| **Evidence** | maximum-gate decision, evidence-package index, and separate promotion or extension record |
| **Dependencies** | independently recreatable A20 artifacts and an explicit decision; sampler, agent, endr, and research evidence excluded |
| **Counts toward P0 gate** | no — evaluates the gate rather than supplying artifact credit |
| **Status** | `not-started` |
