// Section 2, Exercise A: Variables — solution
// rustc --edition 2021 solution_a_variables.rs && ./solution_a_variables

const MAX_ATTEMPTS: u32 = 3;

fn main() {
    let x = 5;
    println!("x = {}", x);

    let x = x * 2;
    println!("x after shadowing = {}", x);

    let mut counter = 0;
    {
        counter += MAX_ATTEMPTS;
    }
    println!("counter after inner scope = {}", counter);
}
