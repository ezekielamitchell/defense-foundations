# P10 — Multi-Agent Coordination Under Degraded Communications

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P4, P6, P8

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P4 reliable runtime, P6 deterministic single-agent simulation and P8 authority tests. No RL prerequisite.

## Learn

Capability matching, task ownership, acknowledgements, retries/deduplication, deadlines, epochs/leases, causal ordering, partial views, bandwidth, partitions and reconciliation. Choose conservative stop/hold when authority or exclusive ownership is uncertain.

## Build

Begin Flagship III with two to four simulated agents and two capability types in inspection-plus-relay. Compare static assignments, centralized greedy allocation and one bounded coordination alternative on identical scenarios.

## Acceptance evidence

Delay, drop, duplication, reordering, stale state, partition, reconnection and one node failure. Measure completed eligible tasks, duplicate/conflicting execution, policy violations, reassignment/recovery, bandwidth and resource use. Define exactly what can resume after recovery.

## Source and scope

Existing runtime contracts, DDIA sections and Lamport's event-ordering paper after prerequisite concepts. Algorithm libraries are optional.

**Defer:** MAPPO/QMIX, physical swarms and Byzantine-tolerance claims. Do not promise progress and exclusive task ownership through every partition; state the chosen tradeoff.

## Next

P11 final assurance review, then P12. A simpler baseline winning is a useful documented result.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
