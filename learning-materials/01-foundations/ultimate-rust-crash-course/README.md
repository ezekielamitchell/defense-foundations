# Ultimate Rust Crash Course

**Source:** [Udemy](https://www.udemy.com/course/ultimate-rust-crash-course/) — Nathan Stocks  
**Catalog:** course #3  
**Activation:** P0-eligible, optional supplement

## Pull these modules

Cargo workflow, ownership and borrowing, structs/enums, pattern matching, error handling, iterators, and practical CLI organization.

## Role

Use this course only when its explanation unblocks the Rust Book/Rustlings path. It must not become a second linear curriculum.

## Evidence

A Rust CLI that parses detection-log-like lines with `Result`-based errors and readable help output.

## Layout

One folder per course section (`ch01_introduction` … `ch08_final_words`), each with `notes.md` (concepts + must-know syntax) plus one `exercise_*.rs` (starter with `// TODO` gaps) / `solution_*.rs` pair per named exercise lecture in that section — e.g. `ch05_structs_traits_and_enums/` has both `exercise_f_structs_traits.rs` and `exercise_g_collections_enums.rs`. Every file is dependency-free — compile any of them directly with `rustc --edition 2021 <file>.rs && ./<binary>`.
