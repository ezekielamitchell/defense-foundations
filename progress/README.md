# Progress and Evidence

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

P0 reset Day 0 and the gate clock begin **2026-08-09 at 16:00 America/Los_Angeles**. Week 1 is Aug 9 only; Week 2 begins Monday Aug 10. The six-week minimum gate remains **2026-08-30** and the eight-week maximum gate remains **2026-09-13**. Aegis Nexus `01_Daily/_Phase Config.md` is the sole hard-date authority; see [the P0 phase README](../curriculum/phases/00-foundations/README.md) for the checklist.

Work before 2026-08-09 at 16:00 remains audit-valid history but is excluded from every restarted denominator. The Phase 0 artifact is the **paired file-statistics CLI**: `projects/file_stats` (Python) and `projects/hello-stats` (Rust). Both are currently stubs/WIP and must be re-verified. Rustlings state is preserved (`if2`, 15 historical completions), but active credit is 0/50. Hugging Face and every P0-authorized Udemy/O’Reilly course also restart at 0%.

Reset administration, planning, dashboard edits, and Calendar work are not curriculum evidence.

endr founder/company work is tracked in endr and Aegis, not in this ledger. It cannot satisfy or delay a P0 gate.

DD #78's agent overlay has a separate evidence boundary: agent notes, course work, and bounded tool prototypes belong to the Agent Engineering Sprint tracker and never satisfy the P0 foundation gate. The same boundary applies to the daily research paper and the weekly OpenCV sampler.

**Evidence source rule:** `.github/` does not exist in this repository yet. Until the CI workflow is created (a Week 4 task), cite **local check/test output** with the exact command line. A GitHub Actions run URL may only be cited once the workflow is committed.

## Update routine

1. Update hard dates in Aegis Nexus `_Phase Config` first.
2. Reconcile [TIMELINE.md](../TIMELINE.md).
3. Change phase status only after a gate review.
4. Link public evidence; do not copy sensitive vault notes into this repository.
5. Record limitations and failed attempts alongside successful results.
6. Keep P1–P12 undated until explicit promotion; the only current specialization exceptions are DD #78's three non-gate overlays through 2026-09-13 — the weekly Hugging Face Agents block, the weekly OpenCV sampler, and the daily research paper.
