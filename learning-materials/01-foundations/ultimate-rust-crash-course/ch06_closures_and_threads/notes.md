# Section 6 — Final Lectures: Closures & Threads

## Concepts

- **Closures**: anonymous functions that can capture variables from their surrounding scope. Syntax: `|params| expr` or `|params: Type| -> RetType { block }`. They implement one of three traits depending on how they use captured variables: `Fn` (borrows immutably, callable repeatedly), `FnMut` (borrows mutably), `FnOnce` (takes ownership, callable once).
- **`move` closures**: the `move` keyword forces the closure to take ownership of everything it captures instead of borrowing it. This is required whenever the closure must outlive the current scope — most commonly, when handing it to another thread.
- **Threads**: `std::thread::spawn(closure)` runs the closure on a new OS thread and returns a `JoinHandle<T>` (where `T` is the closure's return type). Call `.join()` on the handle to block until the thread finishes and retrieve its result (wrapped in a `Result`, hence the usual `.unwrap()`).

## Must-know syntax

```rust
let add_one = |x: i32| x + 1;
fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 { f(x) }
apply(add_one, 5);

use std::thread;
let data = vec![1, 2, 3];
let handle = thread::spawn(move || {
    data.iter().sum::<i32>() // closure now owns `data`
});
let result: i32 = handle.join().unwrap();
```

## Exercise

- `exercise_h_closures_threads.rs` / `solution_h_closures_threads.rs` — write a closure with an explicit return, and spawn a `move` closure on a thread that sums a `Vec<i32>` and returns the total via `.join()`.
