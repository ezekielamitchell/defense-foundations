// Section 2, Exercise B: Functions — solution
// rustc --edition 2021 solution_b_functions.rs && ./solution_b_functions

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn square(n: i32) -> i32 {
    return n * n;
}

fn main() {
    println!("add(2, 3) = {}", add(2, 3));
    println!("square(4) = {}", square(4));
}
