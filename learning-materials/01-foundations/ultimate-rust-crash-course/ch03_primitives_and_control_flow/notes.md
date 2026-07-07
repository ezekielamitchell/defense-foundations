# Section 3 — Primitive Types & Control Flow

## Concepts

- **Scalar types**: signed/unsigned integers at fixed widths (`i8`/`u8` … `i128`/`u128`), pointer-sized `isize`/`usize` (used for indexing/lengths), floats `f32`/`f64`, `bool`, and `char` (a 4-byte Unicode scalar value, not a byte).
- **Compound types**: tuples `(T1, T2, ...)` group different types and are accessed by `.0`, `.1`, ...; arrays `[T; N]` are fixed-size, same-type, stack-allocated, accessed by index.
- **Control flow**: `if`/`else` is an expression (can be used in a `let`); `while` loops on a condition; `for x in iterable` is the idiomatic iteration form; `loop` repeats forever until `break`, and `break value;` lets a `loop` produce a value.
- **Strings**: `&str` is a borrowed, immutable string slice (often `'static` for literals); `String` is a growable, heap-allocated, owned string. Convert with `.to_string()` / `String::from()`. Concatenate with `format!()` (doesn't consume operands) or `+` (consumes the left `String`).

## Must-know syntax

```rust
let n: i32 = -5;
let u: u8 = 255;
let f: f64 = 3.14;
let c: char = 'R';

let t: (i32, i32) = (3, 4);
t.0; t.1;

let arr: [i32; 3] = [1, 2, 3];
arr[0];

for i in 0..arr.len() { /* ... */ }   // exclusive range
let found = loop {
    if condition { break value; }
};

let s1: &str = "hi";
let s2: String = String::from("there");
let combined = format!("{}, {}!", s1, s2);
```

## Exercises

- `exercise_c_simple_types.rs` / `solution_c_simple_types.rs` — scalar types, tuples, arrays.
- `exercise_d_control_flow_strings.rs` / `solution_d_control_flow_strings.rs` — `loop { break value; }`, `&str` vs `String`, `format!()`.
