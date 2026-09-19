# Resource Spine — v2

**Prepared 2026-09-19.** Select one teaching source for the active competency.
References answer questions; electives remain closed until needed. This is the
new curriculum selection, not an activated Calendar/resource-registry rewrite.
See [Reset Handoff](RESET_HANDOFF.md).

## Beginner desk

| When | Primary | Use and stop point | Evidence |
|---|---|---|---|
| Z0–Z4 | [Python Crash Course, 3e](https://nostarch.com/python-crash-course-3rd-edition) | Chapters 1–8, then 10; one concept plus exercises at a time. Chapter 9 only as needed | A small independently modified program, then file-reading function |
| Alternative to PCC | [CS50P](https://cs50.harvard.edu/python/) | Functions/variables through files/testing; replace PCC, do not take both | Your own exercises and later Project 0; follow course submission rules |
| Z5–Z6 | PCC Chapter 11; [pytest first steps](https://docs.pytest.org/en/stable/getting-started.html) | First assertion, test discovery, then temporary files when needed | Show a real test fail and pass |
| Z7–Z8 | [The Rust Programming Language](https://doc.rust-lang.org/book/) | Chapters 1–6, then selected 8–9, 11–12; ownership/errors before CLI depth | Explain an error and build the matching small behavior |
| Rust practice | Local [Rustlings](../learning-materials/01-foundations/rustlings/README.md) | Concepts from variables onward; preserve saved historical solutions; record fresh exercises | Observed passes plus independent variations |
| Shell | [Missing Semester 2026 shell lesson](https://missing.csail.mit.edu/2026/course-shell/) | Paths, command arguments, pipes and streams as Project 0 needs them | Find input, run program, redirect and inspect output |
| Git | [Pro Git](https://git-scm.com/book/en/v2) | Getting started, recording changes, diff and basic branches | Explain the diff and deliberately select a change; publishing is separate |

The Rust Book explicitly assumes prior programming experience. Introduce it after
Python functions and tests, rather than requiring two unfamiliar languages at once.
Book chapters are our selected teaching boundaries; finishing a book is not a gate.

## Later main-route sources

| Module | Primary source | Bounded application |
|---|---|---|
| P1 | [Python standard library](https://docs.python.org/3.11/library/), pytest, [Cargo Book](https://doc.rust-lang.org/cargo/) | JSON/CSV, schemas, tests, fixtures, deterministic logs; one harness |
| P2 | [scikit-learn getting started](https://scikit-learn.org/stable/getting_started.html) and its linked evaluation guides | One small baseline; leakage, held-out data, simple metrics and uncertainty |
| P4 | [Tokio tutorial](https://tokio.rs/tokio/tutorial), [Serde](https://serde.rs/) | One asynchronous service with bounded resources; no framework collection |
| P4/P10 reference | [Designing Data-Intensive Applications, 2e](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) | Read only the reliability, logs, replication and partition discussion needed by a current design question |
| P6 | Python standard library first; [ROS 2 tutorials](https://docs.ros.org/en/jazzy/Tutorials.html) for a chosen adapter | Tiny discrete-event simulator before a large simulator; one external adapter at a time |
| P8 | Typed state-machine contract and actual tool/interface docs | Human approval, cancellation, expiry, refused input, event trace; an LLM is optional |
| P10 | [Lamport: Time, Clocks and Ordering](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/) | Explain causality with a tiny reordered-message fixture; do not turn the paper into a prerequisite to Z0 |
| P11 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Trace one concrete risk to a control and exercised test; the framework is voluntary guidance, not certification |
| P12 | Your reproducible runs, relevant primary papers and source documentation | Answer one bounded question with baselines, failures and a clean rerun |

## Depth modules — select only for a named need

- **P3 perception:** [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html),
  then one small image task. Classic baseline and data provenance come first.
- **P5 embedded:** platform vendor documentation and [Embedded Rust Book](https://docs.rust-embedded.org/book/).
  Simulation or a bench-safe substitute can satisfy the interface-learning goal.
- **P7 estimation/navigation:** one selected estimator/package's official docs,
  with [MIT linear algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
  for the exact matrix/coordinate gap. Do not attempt every estimator.
- **P9 RL:** [Sutton and Barto's author-hosted book](http://incompleteideas.net/book/the-book-2nd.html)
  for MDP/value/reward concepts, then one algorithm and a non-learning baseline.
- **C++ adapter literacy:** [CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/)
  and the target project's build/debug docs when an adapter requires a native change.
- **Gaze, VLA, MARL, agent frameworks:** backlog; choose only after a concrete
  experiment demonstrates why the simpler interface or baseline is insufficient.

## Paid inventory and duplicate avoidance

Keep any existing paid-resource inventory as history and optional references.
In the new plan:

- PCC becomes the beginner teaching spine; pytest and Command-Line Rust become
  later references within Project 0.
- Effective Python and Programming Rust are not beginner prerequisites.
- Udemy Rust, pytest, CV, ROS and agent courses are optional substitutes or
  targeted references, not parallel completion obligations.
- No new purchase is required to begin; CS50P and the official sources provide a
  free route. Existing subscriptions do not prove current entitlement to every book.

## Source verification and version rules

Public primary pages for PCC, CS50P, the Rust Book, Missing Semester, Pro Git,
Tokio, scikit-learn and PyTorch were checked on September 19. NIST and Lamport
were also inspected during this route review. This verifies teaching scope, not
paid access, completion, or future compatibility. Some ROS documentation pages
were blocked to automated access; search results confirmed the tutorial route.
Later reference links are pointers to recheck when their modules activate.

Use the installed project version's documentation. Preserve the existing Python
minimum and Rust edition until a real implementation issue requires a change.
Choose and record a supported ROS/simulator combination at P6; a distribution
name in this plan is not a permanent latest-version claim.

No downloaded book, paid-course transcript, copyrighted chapter, or private
coursework is copied into the repository by this refresh.
