# Defense Foundations

> The single educational-code and curriculum repo for Phase 0 foundations: Python, Rust, Linux, Git, README quality, tests, and small runnable CLIs. This repo holds the active curriculum map, learning materials, Rustlings work, and current foundation code.

## Current status

| Field | Value |
|---|---|
| Active phase | **P0 — Foundations** |
| Phase start (P0 Day 0/1) | **2026-07-03** |
| Six-week checkpoint | **2026-08-14** |
| Eight-week maximum gate | **2026-08-28** |
| Active model | Course-driven calendar, foundations-weighted |
| Date authority | Aegis Nexus `_Phase Config`, reconciled 2026-07-05 |

Foundations—Python, Rust, Linux, and Git—receive the primary weekly weight. They are the base layer of the autonomy stack: every capability above them—perception, edge inference, ROS 2 middleware, distributed telemetry, multi-agent coordination, mission planning, and human-machine teaming—is ultimately built and debugged in these tools. During P0 there is no parallel CV/robotics/agent lane; advanced CV, ROS 2, edge, and agent work cannot displace foundation evidence.

## Repository map

- [Timeline](TIMELINE.md) — authoritative hard dates, monthly ramp, Phase 0 weekly plan, and post-graduation window.
- [Curriculum](curriculum/README.md) — the 13 phases, category groupings, dependencies, and gate rules.
- [Learning materials](learning-materials/README.md) — individual course/resource folders grouped by learning focus.
- [Research queue](research/README.md) — paper backlogs grouped by technical domain.
- [Progress](progress/README.md) — status and evidence conventions for maintaining this index.
- [Mobile PWA](mobile/) — phone-friendly dashboard for P0 status, weekly tasks, evidence links, and quick capture notes.
- [hello-stats](hello-stats/) — Rust CLI for Project 0: file/stdin line·word·byte stats (runnable, unit-tested).
- [file_stats.py](file_stats.py) — Python CLI for Project 0: file/stdin line·word·byte stats (runnable, pytest-tested).

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
5. **Dates are not invented.** P0 and career milestones use hard dates; later phases remain duration- and evidence-gated until formally scheduled.
6. **Defense framing stays honest.** Report false positives, latency, resource budgets, failure modes, and limitations.
7. **Autonomy Systems Integration.** Every major portfolio artifact integrates at least two domains—perception, edge AI, robotics/ROS 2, distributed systems, agents, mission planning, or human-machine teaming. A model in a notebook is not the unit of work; an integrated system is. This rule exists to prevent isolated projects and to force systems thinking, because that is what the target role and a future founder actually need. See [Portfolio integration](#portfolio-integration).
8. **Evidence is interview-grade.** Prefer deployed systems, benchmarks, simulations, telemetry, evaluation frameworks, design documents, and demo videos over course completion, paper summaries, or one-off notebooks. The bar is defined in [Progress](progress/README.md#interview-grade-evidence).

## Project evidence lives here

| Path | Curriculum role |
|---|---|
| `hello-stats/` | Rust half of Project 0: file/stdin line·word·byte CLI — runnable, `cargo test` green. |
| `file_stats.py` | Python half of Project 0: file/stdin line·word·byte CLI — runnable, `pytest` green. |
| `learning-materials/01-foundations/rustlings/` | Rust fundamentals drills and local Rustlings state. |
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

## Project 0 — `hello-stats` (Rust) + `file_stats.py` (Python)

The first paired deliverable of Phase 0: the same small problem — count the lines, words, and bytes of a file or of stdin — solved twice, once as a Rust systems binary and once as a Python script. The counting is trivial on purpose; the deliverable is the foundation loop done end to end — argument parsing, file **and** stdin I/O, error handling that fails cleanly instead of panicking, tests, and a documented runnable interface.

### Python — `file_stats.py`

```sh
python file_stats.py README.md          # count a file
cat README.md | python file_stats.py    # count stdin
python file_stats.py missing.txt        # clean error, exit code 1
pytest                                   # run the tests
```

Uses `argparse` + `pathlib`; reads stdin when no path is given; a missing file prints one stderr line and exits `1` (no traceback).

### Rust — `hello-stats`

```sh
cd hello-stats
cargo run -- ../README.md               # count a file
cat ../README.md | cargo run            # count stdin
cargo run -- ../missing.txt             # clean error, exit code 1
cargo test                              # run the tests
```

`Result`-based error handling, no `unwrap()` on user input or file I/O; a bad path prints one stderr line and exits `1`.

### Example output (real)

Both CLIs print the same shape and the same numbers for the same input.

```text
$ printf 'hello world\nsecond line\n' | python file_stats.py
   lines    words    bytes  source
       2        4       24  <stdin>

$ printf 'hello world\nsecond line\n' | (cd hello-stats && cargo run -q)
   lines    words    bytes  source
       2        4       24  <stdin>

$ python file_stats.py README.md
   lines    words    bytes  source
     101     1116     8728  README.md

$ python file_stats.py missing.txt
file_stats: cannot open 'missing.txt': No such file or directory   (exit 1)
```

(The `README.md` counts reflect this file's size at the time of writing and grow as it does; the two-line example is the stable reference.)

### Python vs Rust — the same tool, two languages

| Dimension | Python (`file_stats.py`) | Rust (`hello-stats`) |
|---|---|---|
| Role | scripting, glue, fast iteration | systems binary, predictable runtime |
| Error handling | exception caught at the boundary (`except OSError`) | `Result` propagated with `?`, no `unwrap()` on I/O |
| I/O | `pathlib.Path.read_bytes()`, `sys.stdin.buffer` | `File::open`, `BufReader`, `io::stdin().lock()` |
| Failure mode | one stderr line + exit 1 | one stderr line + exit 1 |
| Distribution | needs a Python interpreter | single compiled binary |
| Tests | `pytest` (3 tests) | `cargo test` (2 tests) |

Python is faster to write and change; Rust compiles to a dependency-free binary with the error paths enforced at compile time. Real autonomy stacks use both — Python for training, tooling, and orchestration; Rust and C++ for the parts that must run predictably on an edge device or in a flight-critical loop.

### Why this matters for the foundation

Every layer above the foundation — perception, edge inference, ROS 2 nodes, telemetry, multi-agent coordination — is written, tested, and debugged in exactly these primitives: parse input, read a stream, handle the error, prove it with a test, document the interface. Project 0 is deliberately small so the *engineering habits* are the deliverable, not the algorithm. Getting file/stdin handling, `Result`-style error discipline, and a green test suite right here is what makes the low-false-positive, edge-deployed systems later in the curriculum credible rather than hand-waved.

---

Maintained alongside the Aegis Nexus vault. The vault is the private operating brain; this repository is the durable curriculum map.
