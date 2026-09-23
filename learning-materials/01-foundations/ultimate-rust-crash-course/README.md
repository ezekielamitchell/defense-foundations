# Ultimate Rust Crash Course

> **Current P0 routing:** Use selected introductory lessons alongside Python,
> diagnose recalled basics, and apply the missing concepts to `hello-stats`.
> Preserve historical exercise/completion facts without duplicate credit.
> [Resource Spine](../../../curriculum/RESOURCE_SPINE.md) and
> [Start Here](../../../curriculum/START_HERE.md) govern the educational route.


<!-- AEGIS:PHASE0_PROJECTION:START -->
> **Generated public curriculum projection — do not hand-edit this block.** Schema `aegis.phase0-public-projection.v1`.

**Current educational phase:** P0 is active; current-period work remains unverified. Later phases are not started. A course, reservation, checked task, or generated page is not implementation evidence.

**Core competency route:** P0 → P1 → P2 → P4 → P6 → P8 → P10 → P11 → P12. Optional depth: P3, P5, P7, P9. Python, Rust, AI agents, battlefield AI, and warfare are studied in parallel, with one primary teaching source per track.

**Project 0:** Python `projects/file_stats` and Rust `projects/hello-stats` must independently prove the same file-statistics contract on identical fixtures. Record the artifact, working directory, command, exit code, observed output, changed paths, verdict, blocker, and next command.

This public view contains no personal schedule. Use the private Aegis plan and Calendar for current reservations.

Use a source to resolve an observed gap and apply the lesson in code; attendance alone earns no credit.

<!-- projection-json-sha256: cfccf5c07a3074f24d9f4ffa2770419619093b8b912c285a8afd19fb2af8cbcf -->
<!-- AEGIS:PHASE0_PROJECTION:END -->

## Phase 0 execution contract

The [Udemy listing](https://www.udemy.com/course/ultimate-rust-crash-course/) still reports December 2021 as its last update (checked September 12, 2026). Its fundamentals remain familiar gap-fill support; follow current Rust/Cargo documentation for tooling and never replay the full historically completed course simply because the new-period counter is zero.

- Use this course in the current Rust studio; do not create course-completion debt.
- Official Rust, Cargo, crate, and standard-library documentation remains the primary implementation authority.
- Apply the selected lesson to `projects/hello-stats` in the same studio and
  reserve time for independent code and command evidence.
- Stop at the named lecture or exercise boundary and record the exact next lecture, exercise, failing command, and file as the resume point.
- Preserved files and historical completion remain audit context only. A scheduled or watched lesson grants no current credit.

## Preserved historical chapter record

- Chapter 1 — Introduction + toolchain sanity
- Chapter 2 — Fundamentals
- Chapter 3 — Primitives and control flow
- Chapter 4 — Ownership and borrowing
- Chapter 5 — Structs, traits, collections, and enums
- Chapter 6 — Closures and threads
- Chapter 7 — Invaders project
- Chapter 8 — Final review

Historical completion and solution files remain available for audit. They do not pre-check this tracker.

## Active Phase 0 scope

Only Chapters 1–5 are eligible for issue-bound Phase 0 routing:

1. Introduction + toolchain sanity
2. Fundamentals
3. Primitives and control flow
4. Ownership and borrowing
5. Structs, traits, collections, and enums

Chapters 6–8 are outside the current Phase 0 route. Do not pull closures/threads, the Invaders project, or final-review material merely to finish the course.

## Active issue-bound route

The private active manifest owns dated Chapter 1–5 route and session length.
Each authorized pull stays inside its Rust block, applies immediately to
`hello-stats`, and remains zero-credit until observed current-period evidence
meets the named acceptance test. The course is a supplemental gap-fill source;
Official documentation remains the implementation reference; CLI texts are
gap-driven support.
Historical completion remains preserved without duplicate credit.

## Pull these modules

Cargo workflow, ownership and borrowing, structs/enums, pattern matching, error handling, iterators, and practical CLI organization.

## Role

Use a preserved example only when it unblocks the Rust Book/Rustlings path or a named `hello-stats` issue. It must not displace the gate-controlling Rust project.

## Resume record

At the end of each authorized slice, record: `chapter/lecture stopped | next exact lecture or exercise | hello-stats file changed | command run | observed result | blocker`.

## Evidence

Fresh proof for the canonical `hello-stats` file-statistics contract: identical Python/Rust fixtures, `Result`-based errors, clear output and observed tests. Older course artifacts remain historical evidence, not a different current project requirement.

## Layout

One folder per course section (`ch01_introduction` … `ch08_final_words`), each with `notes.md` (concepts + must-know syntax) plus one `exercise_*.rs` (starter with `// TODO` gaps) / `solution_*.rs` pair per named exercise lecture in that section — e.g. `ch05_structs_traits_and_enums/` has both `exercise_f_structs_traits.rs` and `exercise_g_collections_enums.rs`. Every file is dependency-free — compile any of them directly with `rustc --edition 2021 <file>.rs && ./<binary>`.
