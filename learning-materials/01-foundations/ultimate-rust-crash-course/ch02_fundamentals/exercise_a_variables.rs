// Section 2, Exercise A: Variables
// Covers: let/mut, shadowing, constants, scope.
//
// rustc --edition 2021 exercise_a_variables.rs && ./exercise_a_variables
// Expected output:
//   x = 5
//   x after shadowing = 10
//   counter after inner scope = 3

const MAX_ATTEMPTS: u32 = 3; // constants need an explicit type + SCREAMING_SNAKE_CASE

fn main() {
    let x = 5;
    println!("x = {}", x);

    // TODO 1: shadow `x` with a new binding equal to `x * 2`
    let x = x * 2;
    println!("x after shadowing = {}", x);

    let mut counter = 0;
    {
        // TODO 2: increment `counter` by MAX_ATTEMPTS inside this inner scope
        counter += MAX_ATTEMPTS;
    }
    println!("counter after inner scope = {}", counter);
}
