// Section 4, Exercise E: Ownership & References — solution
// rustc --edition 2021 solution_e_ownership_references.rs && ./solution_e_ownership_references

fn print_len(s: &String) -> usize {
    s.len()
}

fn add_exclaim(s: &mut String) {
    s.push('!');
}

fn main() {
    let s1 = String::from("hello");
    let len = print_len(&s1);
    println!("{} has length {}", s1, len);

    let mut s2 = String::from("world");
    add_exclaim(&mut s2);
    println!("{}", s2);

    let s3 = s2;
    println!("moved");
    let _ = s3;

    let n1 = 5;
    let n2 = n1.clone();
    println!("n1={} n2={}", n1, n2);
}
