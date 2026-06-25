# Curriculum Timeline

This timeline mirrors the Aegis Nexus `_Phase Config` as of **2026-06-22**. When dates conflict, the vault config wins. Only Phase 0 has fixed phase gates; later phases have durations and evidence gates until explicitly scheduled.

> **Re-anchor note (2026-06-22):** the Sunday 2026-06-21 kickoff did not occur, so P0 Day 1 is re-anchored to Monday **2026-06-22**. This is a *start-only* shift — the six-week (2026-08-02) and eight-week (2026-08-16) gates sit on the Sundays that close P0 weeks 6 and 8 and are held fixed; all downstream career/KL dates are unchanged. Mirrors Aegis Nexus Design Decision #45.

## Hard dates

| Milestone | Date |
|---|---|
| Commencement walk complete | 2026-06-14 |
| Curriculum kickoff / P0 Day 1 | **2026-06-22** |
| CV on-ramp begins | 2026-06-22 |
| Networking outreach + internship/contract option begins | 2026-06-22 |
| Resume and LinkedIn refresh | 2026-07-18 |
| GitHub profile aligned | 2026-08-01 |
| P0 six-week confidence checkpoint | **2026-08-02** |
| GDARS demo and CASEset publication-ready target | 2026-08-07 |
| P0 eight-week maximum gate | **2026-08-16** |
| First exploratory application wave | 2026-08-21 |
| Final Seattle University ML course | Sep–Dec 2026 |
| Degree conferred | Fall 2026 term end, approximately Dec 2026 |
| Early offer (optional Path B fallback only) | 2026-12-07 |
| KL go/no-go decision | 2026-12-21 |
| Kuala Lumpur build window | 2027-01-07 → 2027-05-06 |
| Committed application sprint | 2027-05-07 |
| Offer-signed target | 2027-07-07 |
| Full-time start target | 2027-09-07 |

## Active course-driven calendar

This ramp climbs the autonomy stack in order: foundations and perception first, then the ROS 2 middleware and distributed telemetry that wire perception into navigation and mission logic, then agent and mission-execution work. The Sep–Nov ROS 2 block is the autonomy-middleware stage, not a detour into robotics. Dates below are authoritative; the framing does not move them.

| Month | Primary lane | Parallel lane | Intended evidence |
|---|---|---|---|
| Jun 2026, from 06-22 | Foundations: Python, Rust, Linux, Git | Light OpenCV camera on-ramp | foundation reps and camera pipeline v0 |
| Jul 2026 | Foundations → paired CLIs; PyTorch basics begin only as capacity allows | OpenCV deepening; light LangGraph exposure | Python/Rust CLI pair and first detector demo |
| Aug 2026 | PyTorch and custom detector | YOLO introduction; Rust log tooling | custom detector and structured logs |
| Sep 2026 | ROS 2 for Beginners + university ML course | CV-log summarizer; Rust mission-log CLI | ROS 2 perception node and log summary |
| Oct 2026 | ROS 2 Nav2 | retrieval over project documentation and logs | reconnaissance-robot simulation and searchable logs |
| Nov 2026 | Nav2 and Embedded Rust | agent evaluation harness | mission demo and initial ISR-assistant tests |
| Dec 2026 | Embedded Rust, consolidation, KL decision | Agent sprint only if deliberately scheduled | portfolio consolidation and decision record |
| Jan–May 2027 | Kuala Lumpur focused build sprint | curriculum-aligned portfolio work | two polished repos, walkthrough, application packet |

This monthly calendar is an applied ramp, not permission to mark later numbered phases complete. Phase completion still requires the phase exit gate.

## Phase 0 weekly resource plan

P0 runs eight weeks, W26 through W33. P0 Week 1 is W26, opening with the Monday 2026-06-22 kickoff (first task 1:00 PM). The six-week gate closes W31 (Sun Aug 2) and the eight-week maximum gate closes W33 (Sun Aug 16).

| Week | Dates | Primary material | Required evidence |
|---|---|---|---|
| W26 — Week 1 | Jun 22–28 | **Kickoff Mon 06-22:** toolchains + `defense-foundations` repo + README; Missing Semester lecture 1 (shell); Python Crash Course ch. 1–8; MIT 6.0001 lectures 1–4; Rustlings batch 1 | clean environment, repo + README committed, first runnable Python scripts, file-processing script |
| W27 — Week 2 | Jun 29–Jul 5 | Rust Book ch. 1–6; Rustlings batches 1–3 | Rustlings batch and small Cargo program |
| W28 — Week 3 | Jul 6–12 | Missing Semester lectures 2–5; Pro Git ch. 1–3 | terminal workflow note, clean commits, PR practice |
| W29 — Week 4 | Jul 13–19 | `argparse`, `pathlib`, `pytest`, and `uv` | `csv_summary` v0 |
| W30 — Week 5 | Jul 20–26 | Rust Book ch. 7–10; `clap` v4; Rustlings batches 4–5 | `wc-rs` v0 |
| W31 — Week 6 | Jul 27–Aug 2 | README discipline; pytest and Cargo tests — **six-week gate Sun Aug 2** | paired comparison note and tests; six-week review |
| W32 — Week 7 | Aug 3–9 | Hardening and exit-gate review | edge cases, README polish, dependency cleanup |
| W33 — Week 8 | Aug 10–16 | P0 retrospective — **eight-week maximum gate Sun Aug 16** | pass/extend decision at maximum gate |

## Agent sprint decision windows

| Window | Earliest date | Condition |
|---|---|---|
| A | Week of 2026-08-03 | Six-week P0 checkpoint passes cleanly |
| B | 2026-08-16 or later | P0 exit gate passed and fall workload allows it |
| C, default | Dec 2026+ | Fall term complete; directly feeds the Mar 2027 ISR assistant |

Until a window is explicitly selected, the sprint remains **not started**.

## Later-phase scheduling rule

P1–P12 are intentionally listed by estimated duration in the phase folders. Assign a start date only when the previous evidence gate is passed and the phase is promoted during a review. This prevents an attractive calendar from masquerading as competence.
