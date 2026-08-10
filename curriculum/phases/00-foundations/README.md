# P0 — Foundations

**Status:** in progress  
**Dates:** reset Day 0 + gate clock 2026-08-09 at 16:00 → six-week minimum gate 2026-08-30 → eight-week maximum gate 2026-09-13
**Time:** scheduled inside the governed day envelopes; Calendar time is capacity, not completion

Condensed Week 1 is Sunday 2026-08-09 from the 16:00 cutover. Week 2 resumes the Monday–Sunday cadence on 2026-08-10. Aegis Nexus `01_Daily/_Phase Config.md` is the sole hard-date authority.

**Operating envelope (DD #85):** Monday–Friday 09:30–23:00, Saturday 09:30–18:15, Sunday 09:30–18:00, with 15-minute cross-domain transitions. Closeout is 22:15–22:35 Monday–Thursday and 22:15–22:50 Friday. Protected daily: sleep 00:00–04:30, gym 05:00–06:15, breakfast 07:00–08:00, lunch 12:00–13:00, dinner 18:30–20:00.

**Daily model:** Primary Build → Support Work → Research → Weekly Sampler. One dominant artifact per day; no per-topic daily lanes.

**Non-gate overlays:** the Hugging Face AI Agents Course runs at most **two linked blocks per full week** (90-minute COURSE + up to 120-minute LAB), consuming the deterministic-sampler allocation (no fifth lane, no new bucket). A daily research paper runs 60 minutes at 08:00–09:00. Neither substitutes for Python/Rust/Linux/Git gate evidence. Gates unchanged: 2026-08-30 six-week minimum, 2026-09-13 eight-week maximum.

## Focus

Functional Python, Rust, Linux shell, and Git. Build the ability to write 100–200 line programs without keeping a tutorial open.

Foundations is the gate-controlling curriculum lane. The bounded DD #78 overlays — one weekly Hugging Face Agents block, one weekly OpenCV sampler, and the daily research paper — are active but evidence-separated and non-gate. PyTorch, YOLO, ROS 2, LangGraph, RAG, MCP, autonomous consequential agents, swarms, and other later-phase material remain unscheduled until explicit promotion.

## Topics

- Python environments, types, control flow, functions, modules, file I/O, `argparse`, `pathlib`, and basic tests.
- Rust ownership, borrowing, Cargo, structs, enums, pattern matching, `Result`, and `Option`.
- Shell navigation, search, pipes, environment variables, SSH, and tmux.
- Git status, diff, branches, commits, pushes, and basic conflict resolution.

## Materials

See [Foundations](../../../learning-materials/01-foundations/README.md) and the [weekly schedule](../../../TIMELINE.md#phase-0-compressed-reset-plan).

## Evidence target

A paired Python/Rust CLI solving the same small problem, with tests, install/run documentation, example output, and comparison notes.

## Current baseline

- `projects/file_stats` is a greeting stub with no test suite found.
- `projects/hello-stats` is user WIP and does not yet implement file statistics; no Rust tests were found.
- Rustlings currently points to `if2` with 15 historical exercises; active reset credit is 0/50.
- Earlier CLIs and course completions remain historical evidence, not active reset completion.
- Hugging Face, Ultimate Rust, and every P0-authorized Udemy/O’Reilly course restart at 0%.
- Work before 2026-08-09 at 16:00 remains audit-valid history but is excluded from every active denominator.

Reset administration is not curriculum evidence.

## Exit gate

- Python CLI and Rust CLI built from a problem statement.
- First 50 Rustlings exercises complete.
- Basic shell and Git workflows performed without notes.
- At least one repository meets the README evidence standard.
- FizzBuzz, file I/O, and a basic CLI can be implemented without a tutorial.
