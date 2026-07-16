// Section 6, Exercise H: Closures & Threads
// Covers: closure syntax, capturing environment, move closures, Fn trait,
// std::thread::spawn, JoinHandle.
//
// rustc --edition 2021 exercise_h_closures_threads.rs && ./exercise_h_closures_threads
// Expected output:
//   apply(add_one, 5) = 6
//   sum from thread = 15

use std::thread;

fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(x)
}

fn main() {
    // TODO 1: define a closure `add_one` that takes an i32 and returns x + 1
    let add_one = |x: i32| {x+1};
    println!("apply(add_one, 5) = {}", apply(add_one, 5));

    let data = vec![1, 2, 3, 4, 5];
    // TODO 2: spawn a thread with a `move` closure that sums `data` via
    // data.iter().sum() and returns the sum as the closure's value
    let handle = thread::spawn(move || {
        //data.iter().sum::<i32>()
        let sum: i32 = data.iter().sum();
        sum
    });

    let sum = handle.join().unwrap();
    println!("sum from thread = {}", sum);
}
