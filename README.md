# Defense Foundations

> The single educational-code and curriculum repo for Phase 0 foundations: Python, Rust, Linux, Git, README quality, tests, and small runnable CLIs. This repo holds the active curriculum map, learning materials, Rustlings work, and current foundation code.

## Current status

| Field | Value |
|---|---|
| Active phase | **P0 — Foundations** |
| Phase start (P0 Day 0/1) | **2026-07-14** |
| Week 0 partial ramp | **2026-07-14 through 2026-07-19** |
| Gate clock / first full week | **2026-07-20 through 2026-07-26** |
| Six-week checkpoint | **2026-08-30** |
| Eight-week maximum gate | **2026-09-13** |
| Active model | Course-driven calendar, foundations-weighted |
| Date authority | Aegis Nexus `01_Daily/_Phase Config.md` (sole hard-date authority) |

Foundations—Python, Rust, Rustlings, Linux shell, Git/GitHub, tests, README quality, and small CLIs—are the only active curriculum lane. There is no parallel CV, robotics, edge, or agent on-ramp during P0. Later material remains reference-only and undated until an explicit gate promotion.

## Repository map

- [Timeline](TIMELINE.md) — projection of the vault date authority, the Week 0–8 plan, and held career/KL constraints.
- [Curriculum](curriculum/README.md) — the 13 phases, category groupings, dependencies, and gate rules.
- [Learning materials](learning-materials/README.md) — individual course/resource folders grouped by learning focus.
- [Research queue](research/README.md) — paper backlogs grouped by technical domain.
- [Progress](progress/README.md) — status and evidence conventions for maintaining this index.
- [Mobile PWA](mobile/) — phone-friendly dashboard for P0 status, weekly tasks, evidence links, and quick capture notes.
- [hello-stats](projects/hello-stats/) — current Rust Project 0 stub/WIP; not yet a verified stats CLI.
- [file_stats](projects/file_stats/) — current Python Project 0 stub/WIP; not yet a verified stats CLI.

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
4. **Educational code belongs here.** Phase 0 CLIs, Rustlings work, and course exercises live in this repo unless a project graduates into its own portfolio repository.
5. **The vault owns dates.** Aegis Nexus `01_Daily/_Phase Config.md` is the sole hard-date authority. This repository mirrors it; later phases remain undated until explicit promotion.
6. **Defense framing stays honest.** Report false positives, latency, resource budgets, failure modes, and limitations.
7. **Autonomy Systems Integration.** Every major portfolio artifact integrates at least two domains—perception, edge AI, robotics/ROS 2, distributed systems, agents, mission planning, or human-machine teaming. A model in a notebook is not the unit of work; an integrated system is. This rule exists to prevent isolated projects and to force systems thinking, because that is what the target role and a future founder actually need. See [Portfolio integration](#portfolio-integration).
8. **Evidence is interview-grade.** Prefer deployed systems, benchmarks, simulations, telemetry, evaluation frameworks, design documents, and demo videos over course completion, paper summaries, or one-off notebooks. The bar is defined in [Progress](progress/README.md#interview-grade-evidence).

## Project evidence lives here

| Path | Curriculum role |
|---|---|
| `projects/hello-stats/` | Rust half of Project 0 — current stub/WIP; no test suite found. |
| `projects/file_stats/` | Python half of Project 0 — current greeting stub; no test suite found. |
| `learning-materials/01-foundations/rustlings/` | Rust fundamentals drills; current exercise `if2`, with 15 exercises recorded complete. |
| `learning-materials/` | Course exercises and support materials by phase. |

Separate portfolio repositories such as `project-aegis`, `CASEset`, `GUARDEN`, and `computer-vision` remain their own repos. `defense-foundations-lab` is retired; current foundation curriculum/code work routes here.

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

## Project 0 — current baseline, not a completion claim

The intended deliverable is still a paired Python/Rust file-statistics CLI with file and stdin input, clean failures, tests, reproducible commands, and a comparison note. The active paths were re-scaffolded after the earlier root implementations were deleted, so current state must not inherit the old “shipped” claim.

| Artifact | Observed 2026-07-14 state |
|---|---|
| `projects/file_stats/main.py` | Six-line greeting stub. Running it prints `Hello from file-stats!`. |
| `projects/file_stats/README.md` | Empty scaffold. |
| `projects/file_stats/tests/` | No suite found. |
| `projects/hello-stats/src/main.rs` | User WIP that currently prints a greeting and multiplication result; it does not implement file statistics. |
| Rust tests | No `#[test]` functions found. |
| Rustlings | `.rustlings-state.txt` records `if2` as current and 15 exercises complete. |

Earlier deleted root CLIs remain valid historical evidence in Git history, but they are not the current implementation.

### Current smoke commands

From the repository root:

```sh
python3 projects/file_stats/main.py
cargo run --locked --manifest-path projects/hello-stats/Cargo.toml
```

Observed output shape:

```text
Hello from file-stats!
Hello, world! : 30
```

These commands prove only that the stubs execute. They do not prove argument parsing, file/stdin I/O, error handling, or tests.

### Current limitations

- Neither active path implements the Project 0 problem statement.
- No active Python or Rust test suite exists.
- The Rust source and generated `Cargo.lock` contain unrelated user WIP and must remain untouched by documentation resets.
- Reset administration is not curriculum evidence.

### Next bounded improvement

Resume Rustlings from its real state before claiming a new batch:

```sh
cd learning-materials/01-foundations/rustlings
rustlings run if2
```

---

Maintained alongside the Aegis Nexus vault. The vault is the private operating brain; this repository is the durable curriculum map.
