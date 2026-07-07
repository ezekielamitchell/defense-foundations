// Section 5, Exercise G: Collections & Enums — solution
// rustc --edition 2021 solution_g_collections_enums.rs && ./solution_g_collections_enums

use std::collections::HashMap;

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
    match shape {
        Shape::Circle(r) => std::f64::consts::PI * r * r,
        Shape::Rectangle(w, h) => w * h,
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

    if let Some(animal) = find_animal(&zoo, "spider") {
        println!("Found: {}", animal.describe());
    }

    match find_animal(&zoo, "cat") {
        Some(a) => println!("Found: {}", a.describe()),
        None => println!("No cat in the zoo"),
    }
}
