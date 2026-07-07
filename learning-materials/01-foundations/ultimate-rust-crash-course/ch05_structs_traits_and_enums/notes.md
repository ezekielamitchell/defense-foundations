# Section 5 — The Meat of Rust: Structs, Traits, Collections & Enums

## Concepts

- **Structs**: `struct Name { field: Type, ... }` groups related data. `impl Name { }` blocks add behavior: functions taking `&self`/`&mut self`/`self` are *methods* (called as `value.method()`); functions without a `self` param are *associated functions* (called as `Type::function()`, e.g. constructors like `new`).
- **Traits**: `trait Name { fn method(&self) -> T { default body } }` defines shared behavior. `impl Name for Type { }` implements it for a concrete type, optionally overriding default method bodies. Traits are Rust's answer to interfaces, and can be used as bounds (`fn f<T: Name>(x: T)`) to write generic code.
- **Collections**: `Vec<T>` is a growable array (`vec![]`, `.push()`, `.pop()`, `.get()`, `.iter()`); `HashMap<K, V>` is a hash map (`HashMap::new()`, `.insert()`, `.get()`).
- **Enums**: `enum Name { VariantA, VariantB(T), VariantC { field: T } }` — variants can carry data. `Option<T>` (`Some(T)` / `None`) models "maybe a value" without null. `Result<T, E>` (`Ok(T)` / `Err(E)`) models "success or failure" without exceptions. `match` exhaustively destructures any enum; `if let Pattern = value { }` handles just the one case you care about.

## Must-know syntax

```rust
struct Animal { name: String, legs: u8 }
impl Animal {
    fn new(name: &str, legs: u8) -> Self { Animal { name: name.to_string(), legs } }
}

trait Describe {
    fn describe(&self) -> String { String::from("a thing") } // default impl
}
impl Describe for Animal {
    fn describe(&self) -> String { format!("{} has {} legs", self.name, self.legs) }
}

let mut v: Vec<i32> = vec![1, 2, 3];
v.push(4);

use std::collections::HashMap;
let mut m: HashMap<String, i32> = HashMap::new();
m.insert("a".to_string(), 1);

enum Shape { Circle(f64), Rectangle(f64, f64) }
match shape {
    Shape::Circle(r) => ...,
    Shape::Rectangle(w, h) => ...,
}

if let Some(x) = maybe_value { /* got x */ }
match result {
    Ok(v) => ...,
    Err(e) => ...,
}
```

## Exercises

- `exercise_f_structs_traits.rs` / `solution_f_structs_traits.rs` — implement `Describe` for `Animal` (struct + `impl` + trait default override).
- `exercise_g_collections_enums.rs` / `solution_g_collections_enums.rs` — fill in the `match` for `area()`, and use `if let` / `match` against a `HashMap` lookup that returns `Option<&Animal>`.
