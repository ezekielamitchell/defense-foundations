// Section 6, Exercise H: Closures & Threads — solution
// rustc --edition 2021 solution_h_closures_threads.rs && ./solution_h_closures_threads
use std::thread;

fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(x)
}

fn main() {
    let add_one = |x: i32| x + 1;
    println!("apply(add_one, 5) = {}", apply(add_one, 5));

    let data = vec![1, 2, 3, 4, 5];
    let handle = thread::spawn(move || {
        let sum: i32 = data.iter().sum();
        sum
    });

    let sum = handle.join().unwrap();
    println!("sum from thread = {}", sum);
}
