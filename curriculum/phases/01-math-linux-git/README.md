# P1 — Contracts, Measurement and Replay

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P0

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P0 paired CLI, basic tests and shell/Git proof.

## Learn

JSON/CSV and typed records, schema versions, units/timestamps, validation, state machines, arrays/maps/queues, complexity intuition, processes/files, seeded randomness, unit/integration/property tests, CI, logging and profiling.

## Build

Begin Flagship I with a synthetic inspection-event reader and replay harness. Use one schema shared by Python and Rust, golden fixtures, source/config hashes and a small reproducible event trace. Link Projects 1/2/5 only for the portion needed.

## Acceptance evidence

Reject missing, malformed and incompatible records; show same-input decision-trace equivalence; inject one fault; record a benchmark with method and environment; clean-run instructions and a CI job that actually executes meaningful tests.

## Source and scope

Python standard library, pytest and Cargo docs; official schema/serialization documentation for the chosen format.

**Defer:** A C++ course, microservices, complex databases, hardware and ML are not prerequisites. Add a native-language slice only when a later adapter needs it.

## Next

P2, then P4. Build test/authority habits now; P11 later consolidates them.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
