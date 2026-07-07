// Section 5, Exercise G: Collections & Enums
// Covers: Vec, HashMap, enums with data, Option<T>, match, if let.
//
// rustc --edition 2021 exercise_g_collections_enums.rs && ./exercise_g_collections_enums
// Expected output:
//   total area = 24.57
//   Found: Spider has 8 legs
//   No cat in the zoo

use std::collections::HashMap;
use std::f64::consts::PI;

struct Animal {
    name: String,
    legs: u8,
}

impl Animal {
    fn new(name: &str, legs: u8) -> Self {
        Animal { name: name.to_string(), legs }
    }

    fn describe(&self) -> String {
        format!("{} has {} legs", self.name, self.legs)
    }
}

enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

fn area(shape: &Shape) -> f64 {
    // TODO 1: match on `shape` — Circle(r) => pi*r*r, Rectangle(w, h) => w*h
    match shape {
        &Shape::Circle(r) => PI*r*r,
        &Shape::Rectangle(w, h) => w*h,
    }
}

fn find_animal<'a>(zoo: &'a HashMap<String, Animal>, name: &str) -> Option<&'a Animal> {
    zoo.get(name)
}

fn main() {
    let mut zoo: HashMap<String, Animal> = HashMap::new();
    zoo.insert("dog".to_string(), Animal::new("Dog", 4));
    zoo.insert("spider".to_string(), Animal::new("Spider", 8));

    let shapes = vec![Shape::Circle(2.0), Shape::Rectangle(3.0, 4.0)];
    let mut total_area = 0.0;
    for s in &shapes {
        total_area += area(s);
    }
    println!("total area = {:.2}", total_area);

    // TODO 2: use `if let Some(animal) = find_animal(&zoo, "spider")` to print
    // "Found: {animal.describe()}"
    if let Some(animal) = find_animal(&zoo, "spider") {
        println!("Found: {}", animal.describe());
    };

    // TODO 3: use `match` on find_animal(&zoo, "cat") to print either
    // "Found: {describe()}" or "No cat in the zoo"
    match find_animal(&zoo, "hippo") {
        Some(a) => println!("Found: {}", a.describe()),
        None => println!("No cat in the zoo"),
    }


}
