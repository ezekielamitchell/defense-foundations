# Section 4 — The Heart of Rust: Ownership & Borrowing

## Concepts

- **Ownership**: every value has exactly one owner. When the owner goes out of scope, the value is `drop`ped (its memory freed) automatically — no garbage collector needed.
- **Move semantics**: assigning a non-`Copy` value (like `String`) to a new binding, or passing it by value to a function, *moves* it. The old binding becomes invalid; using it afterward is a compile error, not a runtime bug.
- **Copy types**: simple stack-only types (integers, floats, `bool`, `char`, and tuples of `Copy` types) implement `Copy`, so assignment duplicates the value instead of moving it — both bindings stay valid.
- **References & borrowing**: `&T` is an immutable borrow, `&mut T` is a mutable borrow. Borrowing lets a function use a value without taking ownership of it. The borrow checker enforces: at any point you may have *either* one mutable reference *or* any number of immutable references, never both — this is what rules out data races at compile time.

## Must-know syntax

```rust
fn print_len(s: &String) -> usize { s.len() }       // immutable borrow
fn shout(s: &mut String) { s.push('!'); }            // mutable borrow

let s1 = String::from("hi");
let len = print_len(&s1);   // borrow, s1 still valid after

let s2 = s1;                 // MOVE — s1 is no longer valid
// println!("{}", s1);       // compile error: value borrowed after move

let n1 = 5;
let n2 = n1;                 // COPY — both n1 and n2 valid (i32 is Copy)
```

## Exercise

- `exercise_e_ownership_references.rs` / `solution_e_ownership_references.rs` — pass references instead of moving where a value is still needed afterward, and observe (via a commented-out line) what a use-after-move error looks like.
