// Section 7: Invaders (stripped-down, dependency-free) — solution
// rustc --edition 2021 solution_mini_invaders.rs && ./solution_mini_invaders

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

    let update_state = Arc::clone(&state);

    let updater = thread::spawn(move || {
        for _ in 0..5 {
            thread::sleep(Duration::from_millis(50));
            let mut s = update_state.lock().unwrap();
            for inv in s.invaders.iter_mut() {
                inv.y += 1;
            }
            s.tick += 1;
        }
    });

    for _ in 0..5 {
        thread::sleep(Duration::from_millis(50));
        let s = state.lock().unwrap();
        render(&s);
    }

    updater.join().unwrap();
    println!("Game loop finished.");
}
