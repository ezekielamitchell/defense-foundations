# Defense Autonomy Competency Pathway — v2

**Evidence-led route for a very beginner starting point.** This replaces the
old perception-first, fixed-duration teaching plan. It does not move private
dates, award evidence, or start a later phase.

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
| P0 | Programming foundations: parallel Python/Rust, shell, Git, tests | None; start at the first unproved skill | Main route; active phase, learner proof unverified |
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

Private Aegis authority may reserve daily paper reading. This route adds no
second quota and does not presume advanced methods are already understood.
Use an existing paper block to record its question, method, result and one
limitation; a reading note is not Project 0 implementation proof.

## Relative weekly outcomes within the current learning period

These are **relative sequence cards**, not calendar dates, deadlines, completed
work or automatic promotion. The private schedule may move or repeat a card
around classes, company work and actual prerequisites. P0 alone stays active
through this planning sequence; agent, AI and warfare/law outputs are separate
introductory study. The final review asks what the evidence supports, even if
that answer is to continue P0.

| Relative week | Bounded outcome | Check before advancing that strand |
|---|---|---|
| 1 | Start Python, Rust and agent-loop basics together using the [first-week cards](FOUNDATIONS_FAST_TRACK.md). Take one bounded AI/warfare reading only in an existing block. | Explain a changed Python function, a Rust compiler result and a synthetic agent stop rule; list gaps honestly. |
| 2 | Practice Python values/functions/collections and Rust types/references; trace the agent's allowed actions. | Handle changed and empty inputs in each language; reject an agent action outside its allowlist. |
| 3 | Read a small UTF-8 file in Python and Rust with deliberate missing-file behavior. | Show observed success and failure paths independently; no cross-language parity claim yet. |
| 4 | Introduce a real collected Python test and simple CLI input; test a Rust pure function and ordinary error. | Show at least one relevant test collected in each language, including a deliberate failing-then-fixed case. |
| 5 | Implement the next file/stdin slice in Rust and compare a first shared fixture only if both inputs work independently. | State expected counts before running; investigate any mismatch instead of hiding it. |
| 6 | Extend Project 0 to empty, newline, Unicode and invalid-input fixtures. | Compare both CLIs on identical fixtures and record exact commands, outputs, exit codes and limitations. |
| 7 | Make README examples reproducible; practice basic shell/Git, Python lint and Rust formatting/Clippy. | A new reader can run a documented example; checks report their actual collected work. |
| 8 | Attempt a clean-environment/Linux run and an actual CI check if available. | Distinguish local macOS output, Linux output and CI run status; repair a specific gap. |
| 9 | Revisit the oldest P0 gap; separately trace a bounded synthetic agent tool request. | The agent trace includes refusal, cancellation or a stop limit; it earns no P0 credit. |
| 10 | Learn introductory evaluation vocabulary using a tiny synthetic baseline and an AI limitation source. | Name the baseline, input scope, failure case and what cannot be inferred; do not claim P2 credit. |
| 11 | Compare a selected warfare doctrine passage, a humanitarian-law concept and a sourced AI-human-control claim. | Label source type, contested assumption and uncertainty; produce no operational plan or legal conclusion. |
| 12 | Use one existing paper/article reading to formulate a bounded reproducible test question. | Separate what the source reports from what a local educational experiment actually showed. |
| 13 | Reproduce a small unfamiliar Project 0 variation without copying; close the oldest remaining test or explanation gap. | Repeat exact commands with changed input and explain the observed result. |
| 14 | Audit P0 evidence and conduct a capability review. | Promote only after the independently reproduced P0 gate and an explicit authorized decision; otherwise continue the named gap. |

## Time and capacity

There is no credible fixed finish date from the information currently
available. The historical 18–24-month envelope and old 6–10-hour example are
not promises or current capacity rules. Exact focused hours and the parallel
track allocation come from private Aegis authority after protected classes,
company commitments and personal capacity are accounted for.

If a weekly card cannot be completed, preserve its exact resume point and
repeat the unmet skill in the next available block. Do not compress the same
syllabus into a shorter week or accumulate catch-up debt. Review actual output
and availability rather than making course completion a deadline.

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
This route does not change code, historical completion, personal goals,
company gates, Calendar/Todoist, automations, or published dashboards.
