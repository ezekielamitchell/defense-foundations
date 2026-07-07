// Section 5, Exercise F: Structs & Traits
// Covers: struct definition, impl blocks, methods vs. associated functions,
// trait definitions, default trait methods, implementing traits for a type.
//
// rustc --edition 2021 exercise_f_structs_traits.rs && ./exercise_f_structs_traits
// Expected output:
//   Dog has 4 legs

trait Describe {
    fn describe(&self) -> String {
        String::from("a thing") // default implementation
    }
}

struct Animal {
    name: String,
    legs: u8,
}

impl Animal {
    fn new(name: &str, legs: u8) -> Self {
        Animal { name: name.to_string(), legs }
    }
}

// TODO 1: implement the Describe trait for Animal, overriding describe()
// to return "{name} has {legs} legs"
impl Describe for Animal {
    fn describe(&self) -> String { String::from("Animal") }
}

fn main() {
    let dog = Animal::new("Dog", 4);
    println!("{}", dog.describe());
    println!("A {} had {} legs.", dog.name, dog.legs);
}
