// Section 3, Exercise C: Simple Types
// Covers: scalar types (integers, floats, bool, char), tuples, arrays.
//
// rustc --edition 2021 exercise_c_simple_types.rs && ./exercise_c_simple_types
// Expected output:
//   point = (3, 4)
//   array sum = 15
//   bool=true char=R float=3.14

fn main() {
    let _a: i32 = -5;
    let _b: u8 = 255;
    let c: f64 = 3.14;
    let d: bool = true;
    let e: char = 'R';

    let point: (i32, i32) = (3, 4); // tuple
    let arr: [i32; 5] = [1, 2, 3, 4, 5]; // fixed-size array

    // TODO 1: sum every element of `arr` into `sum` using `for i in 0..arr.len()`
    let mut sum = 0;

    for i in 0..arr.len(){
        sum+=arr[i];
    }

    println!("point = {:?}", point);
    println!("array sum = {}", sum);
    println!("bool={} char={} float={:.2}", d, e, c);
}
