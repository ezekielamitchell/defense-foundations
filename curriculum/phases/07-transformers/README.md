# P7 — State Estimation and Navigation

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** optional depth · **Prerequisites:** P6

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P6 simulation; demonstrate coordinate transforms, vectors/matrices, covariance and units.

## Learn

Choose one estimator and one sensor setup. Frames, synchronization, observability, uncertainty, drift, noise/dropout and recovery; introduce SLAM/Nav2 only for the chosen scenario.

## Build

A bounded estimation/navigation adapter with known synthetic ground truth; preserve the core task and evidence interfaces.

## Acceptance evidence

Nominal and dropout cases, trajectory/estimation error, uncertainty interpretation, stale/frame-mismatched inputs and recovery. Every GPS-denied statement names conditions and duration.

## Source and scope

The chosen estimator/package's official documentation and original method; targeted MIT linear-algebra lessons as needed.

**Defer:** All EKF/UKF/VIO/SLAM methods at once; real-world GPS-denied performance claims.

## Next

Return measured state and uncertainty to the core testbed; no automatic hardware progression.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
