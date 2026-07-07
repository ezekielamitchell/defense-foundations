// Section 2, Exercise B: Functions
// Covers: fn syntax, parameters, return values, expressions vs statements.
//
// rustc --edition 2021 exercise_b_functions.rs && ./exercise_b_functions
// Expected output:
//   add(2, 3) = 5
//   square(4) = 16

fn add(a: i32, b: i32) -> i32 {
    // TODO 1: return the sum as an expression (no `return`, no trailing semicolon)
    a + b
}

fn square(n: i32) -> i32 {
    // TODO 2: return n * n using an explicit `return` statement this time
    return n * n;
}

fn main() {
    println!("add(2, 3) = {}", add(2, 3));
    println!("square(4) = {}", square(4));
}
