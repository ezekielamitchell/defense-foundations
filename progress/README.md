# Progress and Evidence

P0 is active; current-period Foundation work remains unverified. The private
Aegis authority owns the reset boundary and evidence ledger. This public
page describes proof standards and historical context only.


The Aegis Nexus vault remains the day-to-day private evidence ledger. This repository records public curriculum status and durable links, not daily personal logs.

## Status vocabulary

- `not started` — reference material only; no completion claim.
- `scheduled overlay` — time is reserved for a bounded specialization, but no artifact or completion is implied.
- `in progress` — explicitly promoted and receiving scheduled time.
- `gate review` — planned material is paused while evidence is checked.
- `complete` — exit criteria are backed by artifacts and measurements.
- `extended` — the gate was not met and a written extension exists.

## Evidence standard

Valid evidence includes a runnable project, command transcript, test result, benchmark, experiment table, demo recording, technical note, or README with reproducible instructions. Watching a course is not evidence by itself.

## Interview-grade evidence

The test for any artifact is whether it survives an autonomy-engineering interview at Anduril, Shield AI, Saronic, Scout AI, or Palantir Mission Autonomy. Course completion proves attendance; systems prove capability.

| Weak (attendance) | Strong (capability) |
|---|---|
| Course completion certificate | Deployed or fielded system |
| Paper summary | Benchmark with baselines |
| One-off notebook experiment | Simulation with seeds and ablations |
| "It works on my machine" | Telemetry from a long-lived service |
| Screenshot of a result | Evaluation framework others can run |
| Verbal description of an idea | Design document and demo video |

**Defense-specific bar.** A perception, edge, or autonomy artifact is not interview-grade until it can speak to all five of these, in writing:

1. **Latency** — end-to-end budget, where the time goes, and what is real-time.
2. **Failure modes** — what breaks the system and how it degrades, not just the happy path.
3. **False positives** — per-class or per-operating-point rates, and why the chosen threshold is defensible.
4. **Resource usage** — memory, power, and compute on the actual target device.
5. **Tradeoffs** — the accuracy/latency/cost choices made and the alternatives rejected.

This is the same honesty required by README operating rule 6; the difference is that interview-grade evidence makes those numbers reproducible by someone else.

## Current phase

<!-- AEGIS:PHASE0_PROJECTION:START -->
> **Generated public curriculum projection — do not hand-edit this block.** Schema `aegis.phase0-public-projection.v1`.

**Current educational phase:** P0 is active; current-period work remains unverified. Later phases are not started. A course, reservation, checked task, or generated page is not implementation evidence.

**Core competency route:** P0 → P1 → P2 → P4 → P6 → P8 → P10 → P11 → P12. Optional depth: P3, P5, P7, P9. Python, Rust, AI agents, battlefield AI, and warfare are studied in parallel, with one primary teaching source per track.

**Project 0:** Python `projects/file_stats` and Rust `projects/hello-stats` must independently prove the same file-statistics contract on identical fixtures. Record the artifact, working directory, command, exit code, observed output, changed paths, verdict, blocker, and next command.

This public view contains no personal schedule. Use the private Aegis plan and Calendar for current reservations.

Historical work remains factual, but the current-period Foundation proof count is zero.

<!-- projection-json-sha256: cfccf5c07a3074f24d9f4ffa2770419619093b8b912c285a8afd19fb2af8cbcf -->
<!-- AEGIS:PHASE0_PROJECTION:END -->

## Update routine

1. Update hard dates in Aegis Nexus `_Phase Config` first.
2. Reconcile [TIMELINE.md](../TIMELINE.md).
3. Change phase status only after a gate review.
4. Link public evidence; do not copy sensitive vault notes into this repository.
5. Record limitations and failed attempts alongside successful results.
6. Keep P1–P12 undated until explicit promotion. Optional bounded agent work and daily research remain non-gate through the current horizon; no generic sampler or standalone course event may be invented.
