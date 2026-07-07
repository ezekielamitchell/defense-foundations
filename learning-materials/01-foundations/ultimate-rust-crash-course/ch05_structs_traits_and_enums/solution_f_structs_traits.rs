// Section 5, Exercise F: Structs & Traits — solution
// rustc --edition 2021 solution_f_structs_traits.rs && ./solution_f_structs_traits

trait Describe {
    fn describe(&self) -> String {
        String::from("a thing")
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

impl Describe for Animal {
    fn describe(&self) -> String {
        format!("{} has {} legs", self.name, self.legs)
    }
}

fn main() {
    let dog = Animal::new("Dog", 4);
    println!("{}", dog.describe());
}
