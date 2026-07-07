// Section 7: Invaders (stripped-down, dependency-free)
// Demonstrates: struct-based entities, multithreaded state updates with
// Arc<Mutex<_>>, and a simple render loop that prints to the terminal.
// (No crossterm/audio crates — just std. See notes.md for why.)
//
// rustc --edition 2021 exercise_mini_invaders.rs && ./exercise_mini_invaders
// Illustrative output (exact tick interleaving may vary run to run):
//   --- tick N ---
//   Player at x=5
//   Invader at (0, N)
//   Invader at (2, N)
//   ... (repeats)
//   Game loop finished.

use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

struct Player {
    x: i32,
}

struct Invader {
    x: i32,
    y: i32,
}

struct GameState {
    player: Player,
    invaders: Vec<Invader>,
    tick: u32,
}

fn render(state: &GameState) {
    println!("--- tick {} ---", state.tick);
    println!("Player at x={}", state.player.x);
    for inv in &state.invaders {
        println!("Invader at ({}, {})", inv.x, inv.y);
    }
}

fn main() {
    let state = Arc::new(Mutex::new(GameState {
        player: Player { x: 5 },
        invaders: vec![Invader { x: 0, y: 0 }, Invader { x: 2, y: 0 }],
        tick: 0,
    }));

    // TODO 1: clone the Arc so the background thread can share ownership of `state`
    let update_state = Arc::clone(&state);

    let updater = thread::spawn(move || {
        for _ in 0..5 {
            thread::sleep(Duration::from_millis(50));
            // TODO 2: lock `update_state`, move every invader down by 1 (y += 1),
            // and increment `tick`
        }
    });

    for _ in 0..5 {
        thread::sleep(Duration::from_millis(50));
        // TODO 3: lock `state` (read-only use is fine) and call render() on it
    }

    updater.join().unwrap();
    println!("Game loop finished.");
}
