# P6 — Deterministic Simulation and Adapter Integration

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P4

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P4 recoverable worker with stable schemas and resource bounds.

## Learn

Simulation time vs wall time, seeded scenarios, event ordering, task-state transitions, non-learning baselines, fault profiles, replay equivalence and separation of model/policy/adapter. For a ROS adapter learn topics/services/actions, QoS, lifecycle, timestamps and frames.

## Build

A tiny Python discrete-event inspection simulation driving the Rust worker through a replaceable adapter. Compare an in-memory reference adapter with a second process/transport adapter. Add one ROS 2 adapter when the robotics integration goal warrants it.

## Acceptance evidence

Same scenario/config/seed gives equivalent decisions; fault injection produces expected safe state; both adapters preserve contract behavior; latency/time semantics and nondeterministic fields are declared.

## Source and scope

Python standard-library reference first. ROS 2 tutorials for the chosen adapter. Choose one supported simulator/distro pairing at activation; no requirement to master Gazebo, Webots and PX4 together.

**Defer:** SLAM, physical dynamics fidelity, photorealism and learned planning. A seeded run alone does not prove all behavior deterministic.

## Next

P8. P7 is an optional navigation specialization, not a coordination prerequisite.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
