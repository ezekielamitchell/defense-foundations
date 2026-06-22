# defense-foundations

> Curriculum hub and progress tracker for a structured transition into defense-focused AI / autonomy engineering. This repo is the index; the proof lives in the linked project repos.

## Problem statement

Modern defense autonomy needs engineers who can take a perception or decision system from a research claim to a system that runs reliably on constrained edge hardware, with calibrated false-positive behavior and an honest account of its limits — yet most learning paths optimize for either pure ML theory or generic software engineering, leaving a gap exactly where defense work lives. This repository is the spine of a deliberate, evidence-driven curriculum that closes that gap: it starts from verifiable foundations (Python, Rust, Linux, Git, and README discipline) and builds toward edge computer vision, robotics, and human-machine teaming, treating every phase as proof — runnable code, measured results, and clear documentation — rather than completion claims. The goal is not a certificate but a portfolio that a defense/autonomy hiring team can inspect, run, and trust.

## What this repo is

- The **index** of a 13-phase curriculum and the day-to-day **evidence tracker** for the active phase.
- A pointer to the real work, which lands as increments in dedicated project repos (see [Repo map](#repo-map)).
- Operating rule: **if it isn't backed by a runnable artifact, a command transcript, or a README, it didn't happen.** No phase is marked complete on vibes.

## Current phase — Phase 0: Foundations

**Computer Literacy · Python Foundations · Rust Foundations** — `in-progress`

| Item | Date |
|---|---|
| Phase start | 2026-06-15 |
| 6-week checkpoint | 2026-07-27 |
| 8-week max exit | 2026-08-10 |

### Phase 0 exit-gate checklist
- [ ] 100–200 line Python CLI from a problem statement
- [ ] 100–200 line Rust CLI with Cargo and `Result`-based error handling
- [ ] First 50 Rustlings exercises completed
- [ ] Linux shell basics fluent: `cd`, `ls`, `rg`, `find`, pipes, env vars, `ssh`, `tmux`
- [ ] Git `status` / `diff` / `branch` / `commit` / `push` without notes
- [ ] At least one repo has a README with install/run command and example output
- [ ] Same small problem solved in Python and Rust, with comparison notes
- [ ] Implement FizzBuzz, file IO, and a basic CLI without a tutorial open

### Active Phase 0 work
- **Project 0 — Joint Python + Rust CLI pair:** `csv_summary` (Python) and `wc-rs` (Rust) — same problem, both languages, with a comparison note.
- **`hello-stats`** — early Rust/stats reps.
- **`rustlings`** — ownership, error handling, compiler-error fluency (batches 1–10 → first 50).

## Evidence tracker

One row per work day. Fill only the lane(s) that moved; an empty cell at week's end means that lane didn't move.

| Date | Python proof | Rust proof | Linux/Git proof | Repo / commit | Next command |
|---|---|---|---|---|---|
| 2026-06-17 | `python3 -m venv .venv && python -V` — venv created, interpreter verified | `rustup update`, `cargo --version`, `cargo new hello-stats`, `cargo install rustlings && rustlings init` — toolchain current, scaffolds created | `git init` (branch `main`); README + problem statement written (commit + GitHub publish pending) | defense-foundations · hello-stats · rustlings | Rustlings batches 1–3; first runnable Python script (read CSV path arg → print row count) |

## Weekly resource plan (Phase 0, W25–W33)

| Week | Dates | Primary resource | Output |
|---|---|---|---|
| W25 | Jun 15–21 | Missing Semester lec 1 (shell); *Python Crash Course* ch. 1–4 | setup notes, repo, first runnable scripts |
| W26 | Jun 22–28 | *Python Crash Course* ch. 1–8; MIT 6.0001 lec 1–4 | Python file-processing script |
| W27 | Jun 29–Jul 5 | The Rust Book ch. 1–6; Rustlings 1–3 | Rustlings batch + tiny Cargo program |
| W28 | Jul 6–12 | Missing Semester lec 2–5; Pro Git ch. 1–3 | terminal workflow note, clean commits |
| W29 | Jul 13–19 | Python CLI: `argparse`, `pathlib`, `pytest`, `uv` | `csv_summary` v0 |
| W30 | Jul 20–26 | Rust Book ch. 7–10; `clap` v4; Rustlings 4–5 | `wc-rs` v0 |
| W31 | Jul 27–Aug 2 | README discipline; pytest + cargo test — **6-week gate Jul 27** | paired comparison note, tests in both repos |
| W32 | Aug 3–9 | Polish + hardening; reread exit-gate criteria | hardened repos |
| W33 | Aug 10–16 | Phase 0 retrospective — **8-week max Aug 10** | pass/extend decision |

## Curriculum map (13 phases)

| # | Phase | Weeks | Status |
|---|---|---|---|
| 0 | Foundations (Python, Rust, Linux, Git) | 6–8 | **in-progress** |
| 1 | Math, Linux, Git | 8–10 | not-started |
| 2 | Core ML | 8–10 | not-started |
| 3 | Computer Vision + Deep Learning | 10–12 | not-started |
| 4 | Rust Systems | 8–10 | not-started |
| 5 | Robotics + Embedded | 10–12 | not-started |
| 6 | Edge AI Deployment | 8–10 | not-started |
| 7 | Transformers | 10–12 | not-started |
| 8 | ROS 2 + Sensor Fusion | 10–12 | not-started |
| 9 | Multi-Agent + Swarm | 8–10 | not-started |
| 10 | Gaze + HMT | 6–8 | not-started |
| 11 | Doctrine + Ethics | 4–6 | not-started |
| 12 | Research Capstone | ongoing | not-started |

## Repo map

Foundations reps land as increments in dedicated repos rather than as throwaway scratch:

| Repo | Role |
|---|---|
| `defense-foundations` (this) | Curriculum index + tracker |
| `project-aegis` | Flagship: edge low-false-positive ground intelligence / threat detection (GDARS) |
| `CASEset` | Context-aware gaze estimation dataset + pipeline (IEEE IRC 2024) |
| `GUARDEN` | Distributed IoT + on-device TFLite Micro detection |
| `computer-vision` | CV experiments and exercises |
| `hello-stats` | Phase 0 Rust/stats reps |
| `rustlings` | Rust fundamentals drills |

---

*Tracker maintained alongside the Aegis Nexus operating vault. Evidence > claims.*
