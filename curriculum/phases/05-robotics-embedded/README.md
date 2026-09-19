# P5 — Embedded and Physical Interfaces

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** optional depth · **Prerequisites:** P4

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P4 bounded runtime and a concrete reason to use a physical interface.

## Learn

One bus/interface, timing, resource limits, sensor calibration, microcontroller basics and safe-state behavior. Use UART or one other justified interface before learning every protocol.

## Build

A bench-safe sensor or simulator adapter for the same typed runtime contract. Use existing equipment or a faithful substitute before purchasing hardware.

## Acceptance evidence

Build/run provenance, timing/resource observations, malformed/stale/dropout input and a deliberate safe response. Distinguish simulation from actual named-hardware evidence.

## Source and scope

Vendor documentation and Embedded Rust Book only for the chosen target.

**Defer:** Live vehicles, actuator authority, custom boards and multiple hardware platforms are outside this learning slice.

## Next

Return the adapter to Flagship II/III. This branch is not mandatory for the simulated capstone.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
