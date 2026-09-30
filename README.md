# Defense Foundations

Learn programming from zero, then build reliable software, reproducible
simulations, bounded coordination and evidence you can explain.

**[Start here: your first lesson](curriculum/START_HERE.md)**

This repository is the educational implementation home. P0 is the active
phase. The private Aegis plan owns dates and reservations; this public
repository describes the learning route and the proof required to advance.

## Your route

Python and Rust foundations with shared fixtures → contracts and measurement
→ evaluation → reliable services → simulation/adapters → human authority
→ deterministic multi-agent coordination → assurance and capstone. AI agents,
battlefield AI, and warfare are parallel non-gate learning tracks during P0.

Computer vision, embedded hardware, navigation and reinforcement learning are
available depth modules. Choose them for a concrete need. No advanced model,
robot or course collection is required to begin.

- [Beginner guide](curriculum/START_HERE.md): Z0–Z9, first command and shared CLI contract.
- [Full competency route](curriculum/COMPETENCY_PATHWAY.md): prerequisites, projects and capacity rules.
- [Curriculum index](curriculum/README.md): every module and its status.
- [Resource spine](curriculum/RESOURCE_SPINE.md): one selected teaching source per competency.
- [Reset handoff](curriculum/RESET_HANDOFF.md): historical preparation and preservation rules.
- [Inspection and validation](curriculum/REFRESH_REVIEW.md): historical findings and observed checks.
- [Learning-material folders](learning-materials/README.md): exercises and retained references.
- [Proof receipts](progress/proofs/README.md): observed evidence, not calendar completion.
- [Competency timeline](TIMELINE.md), [issue criteria](docs/ISSUES.md), and [mobile view](mobile/README.md): public educational summaries; exact scheduling stays private.

## Autonomy capability map

| Capability | Modules | Output |
|---|---|---|
| Programming | P0 | Paired file-statistics CLI, tests and explanation |
| Contracts and evaluation | P1–P2 | Flagship I — Scenario and Evidence Harness |
| Runtime, simulation and authority | P4/P6/P8 | Flagship II — Bounded Rust Runtime |
| Coordination and assurance | P10/P11/P12 | Flagship III — Coordination and Assurance Testbed |
| Selected depth | P3/P5/P7/P9 | A measured perception, physical-interface, navigation or learned-policy adapter |

ROS 2 is one useful integration surface. Mission/task/policy contracts remain
independent of any simulator or middleware. The first coordination baseline is
scripted; reinforcement learning is an optional experiment.

## Project 0 baseline

Inspect the current Python and Rust implementations before claiming behavior.
Existing code and earlier Git history remain factual; the active period starts
without assuming retained fluency or granting duplicate credit.

```sh
# From the repository root:
python3 projects/file_stats/main.py
cargo test --locked --manifest-path projects/hello-stats/Cargo.toml
```

A greeting or zero-test exit is not gate evidence. Follow the beginner guide,
then prove one behavior at a time with observed output and meaningful tests.
Preserve unrelated work and historical evidence.

## Current public curriculum status

<!-- AEGIS:PHASE0_PROJECTION:START -->
> **Generated public curriculum projection — do not hand-edit this block.** Schema `aegis.phase0-public-projection.v1`.

**Current educational phase:** P0 is active; current-period work remains unverified. Later phases are not started. A course, reservation, checked task, or generated page is not implementation evidence.

**Core competency route:** P0 → P1 → P2 → P4 → P6 → P8 → P10 → P11 → P12. Optional depth: P3, P5, P7, P9. Python, Rust, AI agents, battlefield AI, and warfare are studied in parallel, with one primary teaching source per track.

**Project 0:** Python `projects/file_stats` and Rust `projects/hello-stats` must independently prove the same file-statistics contract on identical fixtures. Record the artifact, working directory, command, exit code, observed output, changed paths, verdict, blocker, and next command.

This public view contains no personal schedule. Use the private Aegis plan and Calendar for current reservations.

<!-- projection-json-sha256: cfccf5c07a3074f24d9f4ffa2770419619093b8b912c285a8afd19fb2af8cbcf -->
<!-- AEGIS:PHASE0_PROJECTION:END -->

The block above is publisher-owned. The private Aegis config and sealed
manifest own dates and counters. P0 is the only active phase; later phases
remain not started until evidence-backed promotion.

## Working rules

- Learn one concept, practice it, then demonstrate a small independent variation.
- Use one primary source per track and keep Project 0 as the gate-owned build.
- Keep original work, historical records and versioned evidence; no duplicate credit.
- Distinguish local tests, simulation, hardware and operational claims.
- Keep degree obligations, real capacity and recovery ahead of optional breadth.
- Educational work does not change any independently governed product's maturity or authority.

## Verification

```sh
python3 tools/validate_phase0_integrity.py
python3 tools/validate_curriculum_route.py
node --check mobile/app.js
node --check mobile/sw.js
git diff --check
```

A curriculum/document check is administrative validation, not learning proof.
