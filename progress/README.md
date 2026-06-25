# Progress and Evidence

The Aegis Nexus vault remains the day-to-day private evidence ledger. This repository records public curriculum status and durable links, not daily personal logs.

## Status vocabulary

- `not started` — reference material only; no completion claim.
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

P0 began **2026-06-22** (Day 1 re-anchored from the 2026-06-21 Sunday kickoff that did not occur; start-only shift, gates held). Its six-week checkpoint is **2026-08-02** and its eight-week maximum gate is **2026-08-16**. See [the P0 phase README](../curriculum/phases/00-foundations/README.md) for the checklist.

## Update routine

1. Update hard dates in Aegis Nexus `_Phase Config` first.
2. Reconcile [TIMELINE.md](../TIMELINE.md).
3. Change phase status only after a gate review.
4. Link public evidence; do not copy sensitive vault notes into this repository.
5. Record limitations and failed attempts alongside successful results.
