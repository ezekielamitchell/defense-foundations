# Section 2 — Fundamentals

## Concepts

- **Cargo**: `cargo new <name>` scaffolds a project (`Cargo.toml` + `src/main.rs`). `cargo build` compiles, `cargo run` compiles-and-runs, `cargo check` type-checks without producing a binary. `Cargo.toml` lists metadata and `[dependencies]` pulled from crates.io.
- **Variables**: `let` bindings are immutable by default; `mut` makes them reassignable. Rust infers types from usage, but you can annotate explicitly (`let x: i32 = 5;`). **Shadowing** lets you re-`let` the same name to a new value/type — it's a new binding, not a mutation.
- **Constants**: `const NAME: Type = value;` — always require an explicit type, are `SCREAMING_SNAKE_CASE` by convention, and must be computable at compile time.
- **Scope**: a variable lives from its `let` to the end of the enclosing `{ }` block. Inner blocks can read outer variables; outer scope can't see inner-block-only bindings.
- **Memory safety**: the borrow checker enforces ownership/borrowing rules at compile time, which is how Rust rules out null pointers, dangling references, and data races without a garbage collector.
- **Functions**: `fn name(param: Type) -> ReturnType { }`. The last expression in the body (no trailing `;`) is the return value; you can also `return` early.
- **Module system**: `mod name { ... }` groups code; items are private by default — add `pub` to expose them. `use path::to::item;` brings an item into scope so you don't have to fully qualify it every time.

## Must-know syntax

```rust
let x = 5;              // immutable
let mut y = 5;          // mutable
let x = x * 2;          // shadowing — new binding, same name
const MAX: u32 = 100;   // explicit type required

fn add(a: i32, b: i32) -> i32 {
    a + b // no semicolon = return value
}

mod greetings {
    pub fn hello(name: &str) -> String {
        format!("Hello, {}!", name)
    }
}
use greetings::hello;
```

Cargo commands: `cargo new`, `cargo build`, `cargo run`, `cargo check`.

## Exercises

- `exercise_a_variables.rs` / `solution_a_variables.rs` — variables, shadowing, constants, scope.
- `exercise_b_functions.rs` / `solution_b_functions.rs` — functions, expression vs. `return`.
- `exercise_modules.rs` / `solution_modules.rs` — `mod`/`pub`/`use` (lecture 10 has no lettered exercise in the course itself; this is bonus practice for it).
