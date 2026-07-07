// Section 4, Exercise E: Ownership & References
// Covers: move semantics, Copy types, borrowing (&T / &mut T).
//
// rustc --edition 2021 exercise_e_ownership_references.rs && ./exercise_e_ownership_references
// Expected output:
//   hello has length 5
//   world!
//   moved
//   n1=5 n2=5

fn print_len(s: &String) -> usize {
    s.len()
}

fn add_exclaim(s: &mut String) {
    s.push('!');
}

fn main() {
    let s1 = String::from("hello");
    // TODO 1: call print_len, passing a *reference* so s1 is still usable afterward
    let len = print_len(&s1);
    println!("{} has length {}", s1, len);

    let mut s2 = String::from("world");
    // TODO 2: call add_exclaim, passing a *mutable reference* to s2
    add_exclaim(&mut s2);
    println!("{}", s2);

    let s3 = s2; // ownership of the String moves from s2 into s3
    // TODO 3: uncomment the line below to see a use-after-move compile error,
    // then re-comment it so the file compiles again.
    // println!("{}", s2);
    println!("moved");
    let _ = s3;

    let n1 = 5;
    let n2 = n1; // i32 is Copy, so this copies instead of moving
    println!("n1={} n2={}", n1, n2);
}
