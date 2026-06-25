# Defense AI & Autonomy Curriculum

> A README-only curriculum index for an evidence-driven transition into autonomous defense systems engineering: perception, edge AI, robotics middleware (ROS 2), distributed systems and telemetry, multi-agent coordination, mission planning, and human-machine teaming, assembled into the autonomy stack rather than studied in isolation. Runnable work lives in dedicated project repositories; this repository explains what to learn, when to learn it, and what proof unlocks the next gate.

## Current status

| Field | Value |
|---|---|
| Active phase | **P0 — Foundations** |
| Phase start (P0 Day 1) | **2026-06-22** |
| Six-week checkpoint | **2026-08-02** |
| Eight-week maximum gate | **2026-08-16** |
| Active model | Course-driven calendar, foundations-weighted |
| Date authority | Aegis Nexus `_Phase Config`, reconciled 2026-06-22 |

Foundations—Python, Rust, Linux, and Git—receive the primary weekly weight. They are the base layer of the autonomy stack: every capability above them—perception, edge inference, ROS 2 middleware, distributed telemetry, multi-agent coordination, mission planning, and human-machine teaming—is ultimately built and debugged in these tools. A light OpenCV on-ramp may run in parallel, but advanced CV, ROS 2, edge, and agent work cannot displace foundation evidence.

## Repository map

- [Timeline](TIMELINE.md) — authoritative hard dates, monthly ramp, Phase 0 weekly plan, and post-graduation window.
- [Curriculum](curriculum/README.md) — the 13 phases, category groupings, dependencies, and gate rules.
- [Learning materials](learning-materials/README.md) — individual course/resource folders grouped by learning focus.
- [Research queue](research/README.md) — paper backlogs grouped by technical domain.
- [Progress](progress/README.md) — status and evidence conventions for maintaining this index.

## Phase map

| Phase | Focus | Duration | Status |
|---|---|---:|---|
| [P0](curriculum/phases/00-foundations/README.md) | Python, Rust, Linux, Git | 6–8 weeks | **in progress** |
| [P1](curriculum/phases/01-math-linux-git/README.md) | Math and engineering discipline | 8–10 weeks | not started |
| [P2](curriculum/phases/02-core-ml/README.md) | Classical ML and honest evaluation | 8–10 weeks | not started |
| [P3](curriculum/phases/03-computer-vision-deep-learning/README.md) | OpenCV, PyTorch, CNNs | 10–12 weeks | not started |
| [P4](curriculum/phases/04-rust-systems/README.md) | Production Rust systems | 8–10 weeks | not started |
| [P5](curriculum/phases/05-robotics-embedded/README.md) | Robotics and embedded systems | 10–12 weeks | not started |
| [P6](curriculum/phases/06-edge-ai-deployment/README.md) | Model optimization and edge deployment | 8–10 weeks | not started |
| [P7](curriculum/phases/07-transformers/README.md) | Transformers and foundation models | 10–12 weeks | not started |
| [P8](curriculum/phases/08-ros2-sensor-fusion/README.md) | ROS 2, SLAM, sensor fusion | 10–12 weeks | not started |
| [P9](curriculum/phases/09-multi-agent-swarm/README.md) | RL, MARL, and swarms | 8–10 weeks | not started |
| [P10](curriculum/phases/10-gaze-hmt/README.md) | Gaze estimation and HMT | 6–8 weeks | not started |
| [P11](curriculum/phases/11-doctrine-ethics/README.md) | Doctrine, policy, and ethics | 4–6 weeks, parallel | not started |
| [P12](curriculum/phases/12-research-capstone/README.md) | Research specialization | ongoing | not started |

The [Agent Engineering Sprint](curriculum/modules/agent-engineering-sprint/README.md) is a bounded specialization module, not a numbered phase.

## Autonomy capability map

The phase numbers above are an execution order; this map is the *capability* order they assemble into. Each layer is load-bearing for the one above it, which is why foundations gate the ramp. The goal of the whole curriculum is the capstone layer: an integrated autonomous system, not a stack of isolated models.

| Layer | Capabilities | Where it is built |
|---|---|---|
| **Foundation** | Python, Rust, Linux, Git | [P0](curriculum/phases/00-foundations/README.md)–[P1](curriculum/phases/01-math-linux-git/README.md) |
| **Systems** | C++, networking, distributed systems, telemetry | [P4](curriculum/phases/04-rust-systems/README.md) · [C/C++ support](learning-materials/14-interview-support/README.md) |
| **Perception** | Computer vision, tracking, sensor fusion | [P2](curriculum/phases/02-core-ml/README.md)–[P3](curriculum/phases/03-computer-vision-deep-learning/README.md) · [P6](curriculum/phases/06-edge-ai-deployment/README.md) · [P8](curriculum/phases/08-ros2-sensor-fusion/README.md) |
| **Agents** | Tool use, planning, memory, orchestration | [Agent Engineering Sprint](curriculum/modules/agent-engineering-sprint/README.md) |
| **Robotics** | ROS 2, simulation, navigation, embodiment | [P5](curriculum/phases/05-robotics-embedded/README.md) · [P8](curriculum/phases/08-ros2-sensor-fusion/README.md) |
| **Autonomy** | Mission planning, human-machine teaming, multi-agent systems | [P9](curriculum/phases/09-multi-agent-swarm/README.md)–[P10](curriculum/phases/10-gaze-hmt/README.md) |
| **Capstone** | Integrated autonomous system | [P12](curriculum/phases/12-research-capstone/README.md) |

ROS 2 sits at the center of this stack, not at its edge: it is the middleware that carries perception into navigation, distributed telemetry into mission logic, and agent decisions back out to embodied actuators. Distributed systems and mission planning are not support skills below the autonomy layer—they *are* the autonomy layer once more than one platform is in the field.

## Operating rules

1. **Evidence over completion claims.** A course block counts only when it produces an artifact, measurement, note, or reproducible result in the appropriate project repository.
2. **Foundations gate the ramp.** Advanced material can slip; foundation confidence cannot be hand-waved.
3. **One primary source per week.** Finish or deliberately stop one source before adding another.
4. **No code belongs here.** This repository contains curriculum and study documentation only.
5. **Dates are not invented.** P0 and career milestones use hard dates; later phases remain duration- and evidence-gated until formally scheduled.
6. **Defense framing stays honest.** Report false positives, latency, resource budgets, failure modes, and limitations.
7. **Autonomy Systems Integration.** Every major portfolio artifact integrates at least two domains—perception, edge AI, robotics/ROS 2, distributed systems, agents, mission planning, or human-machine teaming. A model in a notebook is not the unit of work; an integrated system is. This rule exists to prevent isolated projects and to force systems thinking, because that is what the target role and a future founder actually need. See [Portfolio integration](#portfolio-integration).
8. **Evidence is interview-grade.** Prefer deployed systems, benchmarks, simulations, telemetry, evaluation frameworks, design documents, and demo videos over course completion, paper summaries, or one-off notebooks. The bar is defined in [Progress](progress/README.md#interview-grade-evidence).

## Project evidence lives elsewhere

| Repository | Curriculum role |
|---|---|
| `project-aegis` | Flagship low-false-positive edge perception / GDARS lineage |
| `CASEset` | Gaze-estimation dataset and pipeline |
| `GUARDEN` | Distributed IoT and on-device detection |
| `computer-vision` | CV experiments and exercises |
| `hello-stats` | Early Rust/statistics reps |
| `rustlings` | Rust fundamentals drills |

### Portfolio integration

Per operating rule 7, each flagship artifact is judged by the domains it joins, not the single model inside it. These are the integration targets the portfolio builds toward; a project earns its place by crossing at least two of them.

| Artifact | Integrated domains | Status |
|---|---|---|
| `CASEset` | Computer vision + human-machine teaming | existing |
| `project-aegis` | Computer vision + edge AI | existing |
| Distributed Mesh Telemetry Fabric | Distributed systems + robotics | target |
| Mission Planning Console | Agents + human-machine teaming + mission planning | target |
| ROS 2 Recon Platform | Robotics + perception | target |
| ISR Assistant | Agents + computer vision + mission planning | target |

---

Maintained alongside the Aegis Nexus vault. The vault is the private operating brain; this repository is the durable curriculum map.
