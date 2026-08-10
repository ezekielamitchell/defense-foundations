# Ultimate Rust Crash Course

**Source:** [Udemy](https://www.udemy.com/course/ultimate-rust-crash-course/) — Nathan Stocks  
**Catalog:** course #3  
**Activation:** historical completion is preserved at `9a4baa0` (2026-07-15). Under Aegis DD #85, the **active A20 tracker restarts at Chapter 1, 0/8**. Historical completion grants no current-gate or future-phase credit; fresh Rust proof comes from post-cutover demonstrations, `projects/hello-stats`, and active Rustlings progression.

**Status:** complete-historical; A20 active credit 0/8; scheduled only when the current Calendar manifest names a chapter block

**Schedule:** begins again at Chapter 1 when the current Calendar manifest names the block. Preserved files remain references; no inherited checkbox or completion credit carries forward.

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

## Pull these modules

Cargo workflow, ownership and borrowing, structs/enums, pattern matching, error handling, iterators, and practical CLI organization.

## Role

Use a preserved example only when it unblocks the Rust Book/Rustlings path. It must not displace the gate-controlling Rust project.

## Evidence

A Rust CLI that parses detection-log-like lines with `Result`-based errors and readable help output.

## Layout

One folder per course section (`ch01_introduction` … `ch08_final_words`), each with `notes.md` (concepts + must-know syntax) plus one `exercise_*.rs` (starter with `// TODO` gaps) / `solution_*.rs` pair per named exercise lecture in that section — e.g. `ch05_structs_traits_and_enums/` has both `exercise_f_structs_traits.rs` and `exercise_g_collections_enums.rs`. Every file is dependency-free — compile any of them directly with `rustc --edition 2021 <file>.rs && ./<binary>`.
