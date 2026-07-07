// Section 3, Exercise D: Control Flow & Strings — solution
// rustc --edition 2021 solution_d_control_flow_strings.rs && ./solution_d_control_flow_strings

fn main() {
    let arr: [i32; 5] = [1, 2, 3, 4, 5];

    let mut idx = 0;
    let first_over_three = loop {
        if arr[idx] > 3 {
            break arr[idx];
        }
        idx += 1;
    };

    let s1: &str = "Hello";
    let s2: String = String::from("World");
    let greeting = format!("{}, {}!", s1, s2);

    println!("first element over 3 = {}", first_over_three);
    println!("{}", greeting);
}
