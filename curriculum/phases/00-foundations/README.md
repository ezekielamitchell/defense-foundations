# P0 — Foundations

**Status:** in progress  
**Dates:** Day 0/1 2026-07-14 → gate clock 2026-07-20 → six-week gate 2026-08-30 → maximum gate 2026-09-13
**Time:** approximately 10–15 hours/week

Week 0 runs 2026-07-14 through 2026-07-19 as a partial ramp and does not count toward gate-week velocity. Full execution weeks run Monday through Sunday beginning 2026-07-20. Aegis Nexus `01_Daily/_Phase Config.md` is the sole hard-date authority.

## Focus

Functional Python, Rust, Linux shell, and Git. Build the ability to write 100–200 line programs without keeping a tutorial open.

Foundations is the only active curriculum lane. CV, PyTorch, OpenCV, YOLO, ROS 2, agents, swarms, and other later-phase material remain unscheduled until explicit promotion.

## Topics

- Python environments, types, control flow, functions, modules, file I/O, `argparse`, `pathlib`, and basic tests.
- Rust ownership, borrowing, Cargo, structs, enums, pattern matching, `Result`, and `Option`.
- Shell navigation, search, pipes, environment variables, SSH, and tmux.
- Git status, diff, branches, commits, pushes, and basic conflict resolution.

## Materials

See [Foundations](../../../learning-materials/01-foundations/README.md) and the [weekly schedule](../../../TIMELINE.md#phase-0-week-08-plan).

## Evidence target

A paired Python/Rust CLI solving the same small problem, with tests, install/run documentation, example output, and comparison notes.

## Current baseline

- `projects/file_stats` is a greeting stub with no test suite found.
- `projects/hello-stats` is user WIP and does not yet implement file statistics; no Rust tests were found.
- Rustlings resumes at `if2`; `.rustlings-state.txt` records 15 completed exercises.
- Earlier deleted root CLIs remain historical evidence, not the current implementation.
- Work from 2026-07-03 through 2026-07-13 remains audit-valid history but is excluded from the current gate-week denominator.

Reset administration is not curriculum evidence.

## Exit gate

- Python CLI and Rust CLI built from a problem statement.
- First 50 Rustlings exercises complete.
- Basic shell and Git workflows performed without notes.
- At least one repository meets the README evidence standard.
- FizzBuzz, file I/O, and a basic CLI can be implemented without a tutorial.
