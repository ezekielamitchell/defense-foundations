# P8 — Human Authority and Bounded Agent Interfaces

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P6

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P6 single-agent simulation and attributable task/event contract.

## Learn

Mission/task envelopes, capability limits, policy version/expiry, approval, acknowledgement, pause/cancel/abort, lost-link response, independent policy checks and clear operator feedback. Distinguish deterministic software agents from LLM agents.

## Build

Complete Flagship II with a simple operator CLI/status view controlling only the simulated runtime. A rule-based planner is enough. Optional LLM suggestions use typed outputs and cannot alter the deterministic authority boundary.

## Acceptance evidence

Missing/expired authority, stale approval, invalid peer, duplicate command, pause/resume/abort, lost link and malformed suggestions. Record accepted/refused commands, reason codes and the policy version. If an LLM is used, include prompt-injection/refusal tests.

## Source and scope

The local interface/state-machine specification and chosen tool's docs. HMT measurements use a defined task; no human-study claim without actual study design and evidence.

**Defer:** Gaze, RAG/MCP frameworks, multi-agent LLM orchestration, elaborate dashboards and consequential physical actions.

## Next

P10 with P4/P6 proof. Gaze and learned planners remain optional.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
