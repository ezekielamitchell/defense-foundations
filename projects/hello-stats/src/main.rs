#![allow(dead_code)]

fn add_one(x: i16, y: i16) -> i16 {
    x + y
}

pub fn multiply_this(x: f32, y: f32) -> f32 {
    x * y
}

fn main() {
    println!("Hello, world! : {}", multiply_this(5., 6.));
}
