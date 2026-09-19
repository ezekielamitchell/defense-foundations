# P4 — Reliable Rust Services and Distributed Systems

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P1, P2

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P1 contract/replay and P2 evaluation; Rust errors/ownership/tests understood.

## Learn

Processes, TCP/UDP tradeoffs, async/tasks, channels, typed serialization, queue bounds, backpressure, deadlines, cancellation, retries, idempotency, event identity/order, stale state, persistence, restart and resource measurement.

## Build

Begin Flagship II: a Rust worker accepting synthetic bounded tasks over a typed interface and emitting attributable events. Start in one process, then separate processes only when needed. A model is an optional input; P3 is not required.

## Acceptance evidence

Malformed/oversized input, duplicate task, delayed message, queue overflow, restart, disconnect and shutdown. Measure p50/p95/p99 under declared load plus CPU/memory. Explain what happens to acknowledged/in-flight work after failure.

## Source and scope

Tokio tutorial, Serde and standard-library docs. DDIA is a targeted reliability/distributed-data reference after the basic service works.

**Defer:** Custom cryptography, consensus algorithms, Kubernetes, Python/Rust FFI and mandatory hardware. Local results are not edge-hardware benchmarks.

## Next

P6. Select P5 only for a named physical interface need.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
