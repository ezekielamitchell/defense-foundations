// Section 2, Module System (lecture 10 — the course has no lettered exercise
// for this one; this is bonus practice so the concept still gets a file).
// Covers: mod, pub, use, calling a function through a module path.
//
// rustc --edition 2021 exercise_modules.rs && ./exercise_modules
// Expected output:
//   Hello, Rustacean!

mod greetings {
    // TODO 1: this fn is private to the module — make it `pub` so main() can call it
    pub fn hello(name: &str) -> String {
        format!("Hello, {}!", name)
    }
}

fn main() {
    // TODO 2: call greetings::hello("Rustacean") and print the result
    println!("{}", greetings::hello("endr"));
}
