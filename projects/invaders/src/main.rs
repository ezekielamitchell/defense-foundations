use rusty_audio::Audio;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let mut audio = Audio::new();
    println!("Hello, world!");
    Ok();
}
