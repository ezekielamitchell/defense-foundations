# Resource Spine — Active Parallel Route

The [Parallel Course Map](PARALLEL_COURSE_MAP.md) is the current beginner source authority: selected O’Reilly Python, Udemy Rust and Coursera agent/AI/law lessons, with official references for specific gaps. The [first learning week](FOUNDATIONS_FAST_TRACK.md) starts Python, Rust and agent basics together. One primary course at a time per track; 2–3-hour studios and one-hour readings. Exact reservations live in private Aegis authority.

## P0 source ladder and artifact

| Need now | Primary or support | Use it to produce |
|---|---|---|
| Python functions, collections, files and tests | [Python Crash Course, 3e — O’Reilly](https://www.oreilly.com/library/view/python-crash-course/9781098156664/) as the selected primary; [Python tutorial](https://docs.python.org/3/tutorial/) for a specific syntax gap | One changed-input function, then a real file/error case and collected test in Project 0 |
| Rust tooling, borrowing, errors and tests | [Ultimate Rust Crash Course — Udemy](https://www.udemy.com/course/ultimate-rust-crash-course/) as the selected primary; [Rust Book](https://doc.rust-lang.org/book/) for current behavior | A tiny compiler experiment, a file/error case and a collected test independently of Python |
| Agent-loop vocabulary | [Vanderbilt AI Agents — Coursera](https://www.coursera.org/learn/ai-agents-python) introductory lessons; no API/framework requirement in the first week | A synthetic trace with goal, observation, allowed action, result and stop rule; no Foundation gate credit |
| AI and armed-conflict context | [AI For Everyone — Coursera](https://www.coursera.org/learn/ai-for-everyone/) for general limits; [ICRC human-centred AI paper](https://www.icrc.org/en/document/artificial-intelligence-and-machine-learning-armed-conflict-human-centred-approach) for domain-specific concerns | A sourced claim, limitation and human-control question in a research note |
| Warfare and legal vocabulary | [Leiden IHL — Coursera](https://www.coursera.org/learn/international-humanitarian-law) as the current primary; [MCDP 1 — official doctrine](https://www.marines.mil/News/Publications/MCPEL/Electronic-Library-Display/Article/899837/mcdp-1/) for a bounded conceptual comparison | Distinguish a legal rule, doctrine claim, historical example and unsupported assumption |

An [MIT OpenCourseWare Python lecture on YouTube](https://www.youtube.com/watch?v=xAcTmDO6NTI)
is optional support inside an existing Python studio: pause, predict one code
change and run it. A privately selected research paper belongs in its existing
reading block; record question, method, result and limitation without treating
the reading as Project 0 evidence. Do not add either as an extra weekly course.

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
Current introductory assignments are listed in the course map. Other inventory
entries remain references or later choices. No subscription entitlement,
enrollment, purchase or completion is inferred from a catalog listing.

## Source verification and version rules

The P0 provider and official source pages above were checked for this route
update. This verifies teaching scope, not paid access, completion or future
compatibility. Later-module references are pointers to recheck when those
modules become eligible; a link in this document does not activate a phase.

Use the installed project version's documentation. Preserve the existing Python
minimum and Rust edition until a real implementation issue requires a change.
Choose and record a supported ROS/simulator combination at P6; a distribution
name in this plan is not a permanent latest-version claim.

No downloaded book, paid-course transcript, copyrighted chapter, or private
coursework is copied into the repository by this refresh.
