# Defense Autonomy Competency Pathway — v2

**Prepared 2026-09-19 for a complete beginner.** This replaces the old
perception-first, 18–24-month teaching plan. It does not activate the user's
planned reset, move dates, award evidence, or start a later phase.

Start with [Start Here](START_HERE.md). Use [Resource Spine](RESOURCE_SPINE.md)
for the selected sources and [Reset Handoff](RESET_HANDOFF.md) for activation.

## Target capability

Build reliable Python and Rust software, model bounded tasks, run reproducible
simulations, coordinate unlike software agents under failures, preserve human
control, and explain the results. This supports both systems/autonomy engineering
work and the competence relevant to endr's vendor-neutral mission-autonomy
direction. An educational testbed remains separate from endr's company product,
ownership clearance and evidence gates.

The attached strategic research report is contextual input. Its assurance/runtime
emphasis informs this route; its market claims and proposed product names have
not been adopted as company authority.

## Prerequisites, not numerical order

P0–P12 are stable module IDs. Their existing paths remain compatibility links.
Numbers no longer imply a requirement to complete all thirteen sequentially.

**Main route:** P0 → P1 → P2 → P4 → P6 → P8 → P10 → P11 → P12.

P11 practices start with the first testable artifact; its full review follows
integration. P3, P5, P7 and P9 are selectable depth modules. Choose one when the
artifact or a concrete role requires it. Choosing no specialization is valid for
the first coordination capstone. None is currently active.

| ID | Competency | Entry proof | Role / status |
|---|---|---|---|
| P0 | Programming from zero: parallel Python/Rust, shell, Git, tests | None; start at Z0 | Main route; active phase, learner proof unverified |
| P1 | Contracts, data handling, measurement and replay | P0 gate | Main route; not started |
| P2 | Quantitative reasoning and trustworthy evaluation | P1; algebra/probability checkpoint | Main route; not started |
| P3 | Computer vision and deep learning | P2; vectors/gradients checkpoint | Optional depth; not started |
| P4 | Reliable Rust services and distributed-systems basics | P1 and P2 | Main route; not started |
| P5 | Embedded and physical interfaces | P4; named physical-interface need | Optional depth; not started |
| P6 | Deterministic simulation and adapter integration | P4 | Main route; not started |
| P7 | State estimation, SLAM and navigation | P6; frames/linear-algebra checkpoint | Optional depth; not started |
| P8 | Human authority and bounded agent interfaces | P6 | Main route; not started |
| P9 | Reinforcement learning and decision experiments | P2 and P6; MDP/probability checkpoint | Optional depth; not started |
| P10 | Deterministic multi-agent coordination under degraded communications | P4, P6 and P8; P9 is not required | Main route; not started |
| P11 | Integrated assurance, security and test/evaluation | P10 for final package; practices throughout | Main route; not started |
| P12 | Reproducible capstone and technical communication | P10 and P11; selected branch evidence if used | Main route; not started |

No automatic parallel activation. Finish a bounded module/output before adding
another. Degree work may teach overlapping concepts, but coursework ownership
and actual learning evidence must be checked before reusing an artifact.

## Three connected flagships

| Flagship | Build | Contribution and acceptance |
|---|---|---|
| I — Scenario and Evidence Harness | P1–P2; extend at P6 | Typed synthetic records, reference baseline, versioned inputs, seeded fault profiles, run manifests, metrics and replay comparison |
| II — Bounded Rust Runtime | P4–P8 | Validated task lifecycle, bounded queues, deadlines, health, recovery, policy checks, adapter boundary, operator intervention and attributable events |
| III — Coordination and Assurance Testbed | P10–P12 | Two to four synthetic agents of two capability types; scripted/centralized baseline, partitions and recovery, no conflicting execution, evidence report and outside reproduction |

Existing flagship-note filenames preserve their old perception-oriented names
for link compatibility. Their revised specifications control; neither old file
names nor new designs imply implementation.

Use one modest scenario such as simulated inspection plus relay, with synthetic
observations and no real vehicle control. Perception, navigation and learned
policies can later supply richer inputs behind the same interfaces. They do not
need to be invented before task coordination can be studied.

The 23 supporting project specs form a menu. Keep their IDs/history, select at
most one relevant extension, and do not create 23 separate obligations.
Project 0 remains the only active curriculum build.

## Math and computer-science foundations

Build these explicitly rather than assuming a computer-engineering degree means
they are already fluent:

- P0: arithmetic, units, Boolean logic, loops, functions, basic collections.
- P1: complexity intuition, arrays/maps/sets/queues, parsing, state machines,
  processes/files, deterministic ordering and reproducible randomness.
- P2: algebra, functions/plots, descriptive statistics, conditional probability,
  sampling, held-out evaluation, uncertainty and calibration.
- P4/P10: network failure semantics, partial ordering, retries/idempotency,
  stale state, leases/epochs, partitions and reconciliation.
- Branches: vectors/matrices/gradients for P3; coordinate transforms and
  covariance for P7; expectations, MDPs and reward design for P9.

Each checkpoint uses a small calculation and a runnable example. Pause for a
targeted prerequisite lesson if either cannot be explained. Advanced mathematics
and a long interview-problem grind are not entry requirements for Z0.

C++ is a later adapter literacy option: read a small component, build it with
CMake, inspect it with a debugger/sanitizer, and make one tested change when an
integration requires it. It is not a third beginner language or a P1 blocker.

## Scope control and learning method

One primary source per active track. Learn a concept, practice it, apply it to the
current artifact, and return later for a recall check. A beginner may need guided
examples before being able to name an engineering issue. That is legitimate
instruction; passive viewing alone is not competency evidence.

Use synthetic inputs and existing machines first. Hardware, cloud GPUs,
container orchestration, multiple simulators, Python/Rust FFI, agent frameworks,
and sophisticated crypto are introduced only for an evidenced requirement.
For networking/security, use maintained libraries and document limits rather
than inventing protocols with unsupported security claims.

Do not require a daily advanced paper during the next beginner reset.
Suggested research starts as an optional short, relevant explanation; full
papers enter when P2/P6 skills make methods and results interpretable.
The currently scheduled paper lane is unchanged until the reset reconciles it.

## Time and capacity

There is no credible fixed finish date from the information currently available.
The prior 18–24 months is historical planning context, not the revised promise.
A zero-start route can take longer, especially alongside degree and company work.

For the later reset, start from actual free capacity after degree obligations,
company commitments and personal commitments. A provisional learning budget of
The former **6–10 focused hours/week** example is historical. Actual capacity and the parallel track allocation are defined by current Aegis authority, not this pathway.
For example, four 60-minute sessions plus one 2-hour practice/review block is
six hours. Expand only after two representative weeks show it is sustainable.

At three or four hours, continue a smaller slice and extend the route; at zero,
save the resume point. Do not compress the same syllabus into every capacity
level. Review actual output and availability rather than accumulating catch-up
debt. Existing authoritative schedules are unchanged by this recommendation.

## Promotion and career use

Advance only when you can reproduce the artifact, explain its design, show a
failure and recovery, and name its limitations. Run a small unfamiliar variation
without a full solution in front of you. Dates and certificates do not promote.

After P0/P1, describe demonstrated foundational software skills. After Flagships
I/II, consider relevant software, testing, systems and integration opportunities
based on real role requirements. After III, describe the exact simulated
coordination result. Employment applications need not wait for every elective
or the full capstone; no phase guarantees a job or endr readiness.

## Authority and preservation

Aegis's Phase Map owns this curriculum interpretation; this file is its
repository companion. _Phase Config and its sealed manifest still own the
current dates, counters and reservations. Later phases remain not started.
This preparation does not change code, historical completion, personal goals,
company gates, Calendar/Todoist, automations, or published dashboards.
