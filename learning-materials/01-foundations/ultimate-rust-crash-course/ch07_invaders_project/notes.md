# Section 7 — Project: Invaders

## Concepts

The real course project builds a terminal Space Invaders clone using `crossterm` (rendering/input) and `rodio` (audio), across a setup lecture, a rendering-and-multithreading lecture, and lectures for the player, shooting, invader AI, and win/lose state machine.

That needs real crates and a terminal, so it doesn't fit a single dependency-free file. `exercise_mini_invaders.rs`/`solution_mini_invaders.rs` here instead isolate the one concept that transfers directly: **sharing mutable state safely across threads**, the same pattern the real game uses to run its update loop and render loop concurrently.

- `Arc<T>` ("atomically reference-counted") lets multiple owners (here, two threads) share the same heap value.
- `Mutex<T>` wraps a value so only one thread can access it at a time; `.lock()` blocks until it's your turn and returns a guard you can read/write through.
- `Arc<Mutex<T>>` is the standard combo: `Arc` shares ownership across threads, `Mutex` makes the shared access safe.
- A background thread mutates game state (moves invaders down) while the main thread renders it — the same structural split as the real game's update/render loop, just printed to stdout instead of drawn with `crossterm`.

**Note:** because both threads sleep independently and lock at different moments, the exact tick shown at each render is not perfectly deterministic — that's real concurrency, not a bug in the exercise.

## Must-know syntax

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let state = Arc::new(Mutex::new(MyState { .. }));
let state_for_thread = Arc::clone(&state);

let handle = thread::spawn(move || {
    let mut guard = state_for_thread.lock().unwrap();
    guard.field += 1; // mutate through the guard
});

{
    let guard = state.lock().unwrap(); // read-only use is the same call
    println!("{}", guard.field);
}
handle.join().unwrap();
```

When you're ready to build the *actual* crossterm/rodio game, follow the course repo (`https://github.com/CleanCut/ultimate_rust_crash_course`) — that's a multi-file Cargo project with real dependencies, out of scope for this single-file exercise format.

## Exercise

- `exercise_mini_invaders.rs` / `solution_mini_invaders.rs` — clone the `Arc`, lock it inside the spawned thread to mutate invader positions and the tick counter, and lock the outer `Arc` in the main loop to render.
