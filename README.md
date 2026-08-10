# Defense Foundations

> The single educational-code and curriculum repo for Phase 0 foundations: Python, Rust, Linux, Git, README quality, tests, and small runnable CLIs, with a bounded AI-agent learning overlay. This repo holds the active curriculum map, learning materials, Rustlings work, and current foundation code.

## Current status

| Field | Value |
|---|---|
| Active phase | **P0 — Engineering Foundation Gate** |
| Phase start (P0 Day 0) | **2026-08-09 at 16:00 America/Los_Angeles** |
| Gate clock / condensed Week 1 | **2026-08-09 only** |
| First full Monday–Sunday week (Week 2) | **2026-08-10 through 2026-08-16** |
| Six-week minimum gate | **2026-08-30** |
| Eight-week maximum gate | **2026-09-13** |
| Active model | Portfolio-first, evidence-gated. One dominant artifact per day. |
| Operating envelope | Mon–Fri 09:30–23:00; Sat 09:30–18:15; Sun 09:30–18:00 America/Los_Angeles, with 15-minute cross-domain transitions |
| Protected daily | sleep 00:00–04:30; gym 05:00–06:15; breakfast 07:00–08:00; lunch 12:00–13:00; dinner 18:30–20:00 |
| Reset ID | `A20-2026-08-09-complete-hard-reset` |
| Date authority | Aegis Nexus `01_Daily/_Phase Config.md` (sole hard-date authority), DD #85 |

Foundations—Python, Rust, Rustlings, Linux shell, Git/GitHub, tests, CI, README quality, and small CLIs—are primary and control the P0 gate. The daily workflow is **Primary Build → Support Work → Research → Weekly Sampler**. There is no daily Python lane, Rust lane, CV lane, agent lane, or paper lane; support work attaches to the day's dominant artifact. There is no parallel CV, robotics, edge, or multi-agent/autonomy on-ramp. P1–P12 remain reference-only, not started, and undated until explicit promotion.

Two **non-gate overlays** run alongside foundations (Aegis Nexus DD #85/#78):

- **Hugging Face AI Agents Course** — at most **two linked blocks per full week**: a 90-minute COURSE and up to 120-minute LAB, consuming the existing deterministic-sampler allocation. It creates no fifth lane and no new percentage bucket. Scope is tools, messages, Thought → Action → Observation, ReAct, and typed bounded read-only tools. LangGraph depth, RAG, MCP production work, LlamaIndex depth, the GAIA project, fine-tuning, and multi-agent orchestration are **deferred to later phases**.
- **Daily research paper** — one named paper, 60 minutes, 08:00–09:00, on the Research calendar, with the note written to the vault.

Neither overlay earns gate credit. Approximate weekly allocation is Rust ~34–35%, Python ~32–33%, Linux/Git/CI ~15%, OpenCV sampler ≤9%, HF-agent/deterministic sampler ≤9%.

The 2026-08-09 16:00 reset also restarts the bounded **endr company-execution lane** at two hours daily, scope-cut around protected commitments. Company work, founder decisions, product discovery, and endr repositories are not curriculum evidence and do not satisfy or move a P0 gate. All active P0 course progress—including Hugging Face and the P0-authorized Udemy/O’Reilly routes—starts at 0%.

## Repository map

- [Timeline](TIMELINE.md) — projection of the vault date authority, the Week 1–8 plan, and held career/KL constraints.
- [Curriculum](curriculum/README.md) — the 13 phases, category groupings, dependencies, and gate rules.
- [Learning materials](learning-materials/README.md) — individual course/resource folders grouped by learning focus.
- [Research queue](research/README.md) — paper backlogs grouped by technical domain.
- [Progress](progress/README.md) — status and evidence conventions for maintaining this index.
- [Mobile PWA](mobile/) — phone-friendly dashboard for P0 status, weekly tasks, evidence links, and quick capture notes.
- [Issue ledger](docs/ISSUES.md) — local `P0-W*` issue IDs referenced by the Phase 0 calendar.
- [file_stats](projects/file_stats/) — **Python half of the paired Phase 0 file-statistics CLI**; currently a greeting stub with no `tests/`.
- [hello-stats](projects/hello-stats/) — **Rust half of the paired Phase 0 file-statistics CLI**; currently greeting WIP with empty `[dependencies]` and no tests.

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

The [Agent Engineering Sprint](curriculum/modules/agent-engineering-sprint/README.md) is a bounded specialization module scheduled across P0, not a numbered phase and not a completion claim.

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
9. **Overlay proof stays separate.** Agent-course and Aegis Research Agent artifacts belong to the Agent Engineering Sprint tracker/repo and never count toward the Python/Rust/Linux/Git P0 exit gate.

## Project evidence lives here

| Path | Curriculum role |
|---|---|
| `projects/hello-stats/` | Rust half of Project 0 — current stub/WIP; no test suite found. |
| `projects/file_stats/` | Python half of Project 0 — current greeting stub; no test suite found. |
| `learning-materials/01-foundations/rustlings/` | Rust fundamentals drills; file state is `if2` with 15 historical completions, while active reset credit is 0/50. |
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

| Artifact | Reset baseline observed through 2026-07-16 |
|---|---|
| `projects/file_stats/main.py` | Six-line greeting stub. Running it prints `Hello from file-stats!`. |
| `projects/file_stats/README.md` | Empty scaffold. |
| `projects/file_stats/tests/` | No suite found. |
| `projects/hello-stats/src/main.rs` | User WIP that currently prints a greeting and multiplication result; it does not implement file statistics. |
| Rust tests | No `#[test]` functions found. |
| Rustlings | `.rustlings-state.txt` records historical state `if2` and 15 prior completions; active reset credit is 0/50 until freshly demonstrated after 2026-08-09 16:00. |

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
- No active Python or Rust test suite exists. `projects/file_stats/pyproject.toml` declares `testpaths = ["tests"]`, but `tests/` does not exist, so `pytest` currently collects nothing.
- `projects/hello-stats/Cargo.toml` has an empty `[dependencies]`; `clap` and `serde` are not wired yet.
- `projects/file_stats/README.md` is a 0-byte scaffold and `projects/hello-stats/README.md` does not exist. Neither cold-run README is usable evidence today.
- The Rust source and generated `Cargo.lock` contain unrelated user WIP and must remain untouched by documentation resets.
- Reset administration is not curriculum evidence.

### Evidence sources — CI does not exist yet

**There is no `.github/` directory in this repository and no GitHub Actions workflow has ever run.** Until the workflow is created:

| Period | Acceptable evidence |
|---|---|
| Before the CI workflow exists | **Local check/test output** — saved `pytest`, `ruff`, `cargo test`, `clippy`, and `rustfmt --check` transcripts, plus the exact command line |
| After the CI workflow exists | **GitHub Actions run URL**, alongside the local transcript |

No document, issue, or evidence row may cite a GitHub Actions run URL before the workflow is committed. Creating the workflow is a scheduled Week 4 task, not a claim that can be made now.

### Next bounded improvement

Resume Rustlings from its real state before claiming a new batch:

```sh
cd learning-materials/01-foundations/rustlings
rustlings run if2
```

---

Maintained alongside the Aegis Nexus vault. The vault is the private operating brain; this repository is the durable curriculum map.
