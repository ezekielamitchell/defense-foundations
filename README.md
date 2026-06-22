# Defense AI & Autonomy Curriculum

> A README-only curriculum index for an evidence-driven transition into defense-focused AI, edge perception, robotics, autonomy, and human-machine teaming. Runnable work lives in dedicated project repositories; this repository explains what to learn, when to learn it, and what proof unlocks the next gate.

## Current status

| Field | Value |
|---|---|
| Active phase | **P0 — Foundations** |
| Phase start (P0 Day 1) | **2026-06-22** |
| Six-week checkpoint | **2026-08-02** |
| Eight-week maximum gate | **2026-08-16** |
| Active model | Course-driven calendar, foundations-weighted |
| Date authority | Aegis Nexus `_Phase Config`, reconciled 2026-06-22 |

Foundations—Python, Rust, Linux, and Git—receive the primary weekly weight. A light OpenCV on-ramp may run in parallel, but advanced CV, ROS 2, edge, and agent work cannot displace foundation evidence.

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

## Operating rules

1. **Evidence over completion claims.** A course block counts only when it produces an artifact, measurement, note, or reproducible result in the appropriate project repository.
2. **Foundations gate the ramp.** Advanced material can slip; foundation confidence cannot be hand-waved.
3. **One primary source per week.** Finish or deliberately stop one source before adding another.
4. **No code belongs here.** This repository contains curriculum and study documentation only.
5. **Dates are not invented.** P0 and career milestones use hard dates; later phases remain duration- and evidence-gated until formally scheduled.
6. **Defense framing stays honest.** Report false positives, latency, resource budgets, failure modes, and limitations.

## Project evidence lives elsewhere

| Repository | Curriculum role |
|---|---|
| `project-aegis` | Flagship low-false-positive edge perception / GDARS lineage |
| `CASEset` | Gaze-estimation dataset and pipeline |
| `GUARDEN` | Distributed IoT and on-device detection |
| `computer-vision` | CV experiments and exercises |
| `hello-stats` | Early Rust/statistics reps |
| `rustlings` | Rust fundamentals drills |

---

Maintained alongside the Aegis Nexus vault. The vault is the private operating brain; this repository is the durable curriculum map.
