// Section 3, Exercise C: Simple Types — solution
// rustc --edition 2021 solution_c_simple_types.rs && ./solution_c_simple_types

fn main() {
    let _a: i32 = -5;
    let _b: u8 = 255;
    let c: f64 = 3.14;
    let d: bool = true;
    let e: char = 'R';

    let point: (i32, i32) = (3, 4);
    let arr: [i32; 5] = [1, 2, 3, 4, 5];

    let mut sum = 0;
    for i in 0..arr.len() {
        sum += arr[i];
    }

    println!("point = {:?}", point);
    println!("array sum = {}", sum);
    println!("bool={} char={} float={:.2}", d, e, c);
}
