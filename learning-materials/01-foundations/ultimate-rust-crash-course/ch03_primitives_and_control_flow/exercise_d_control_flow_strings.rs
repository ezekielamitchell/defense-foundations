// Section 3, Exercise D: Control Flow & Strings
// Covers: loop + break-with-value, &str vs String, format!().
//
// rustc --edition 2021 exercise_d_control_flow_strings.rs && ./exercise_d_control_flow_strings
// Expected output:
//   first element over 3 = 4
//   Hello, World!

fn main() {
    let arr: [i32; 5] = [1, 2, 3, 4, 5];

    // TODO 1: replace the line below with a real search — check `arr[idx] > 3`,
    // `break arr[idx];` if so, otherwise `idx += 1;` and keep looping
    let mut idx = 0;
    let first_over_three = loop {
        if arr[idx] >3 {break arr[idx]}
        else {idx+=1} // placeholder: always breaks on the first element
    };

    let s1: &str = "Hello";
    let s2: String = String::from("World");
    // TODO 2: build "Hello, World!" with format!() from s1 and s2
    println!("{}", format!("{}, {}!", s1, s2));

    println!("first element over 3 = {}", first_over_three);
}
