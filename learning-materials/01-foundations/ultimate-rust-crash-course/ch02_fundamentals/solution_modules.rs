// Section 2, Module System — solution
// rustc --edition 2021 solution_modules.rs && ./solution_modules

mod greetings {
    pub fn hello(name: &str) -> String {
        format!("Hello, {}!", name)
    }
}

fn main() {
    println!("{}", greetings::hello("Rustacean"));
}
