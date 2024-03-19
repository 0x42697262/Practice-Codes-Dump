use std::io;

const DIGITS: &[u8] = b"0123456789.";

fn infix_to_postfix(input: &String) -> Vec<u8> {
    let mut prefix: Vec<u8> = Vec::new();
    prefix
}

fn infix_to_prefix(input: &String) -> Vec<u8> {
    let mut postfix: Vec<u8> = Vec::new();
    postfix
}

fn evaluate_postfix() {}

fn evaluate_prefix() {}

fn read_number() {}

// Input: A valid arithmetic expression
// Output:
//        - prefix notation
//        - postfix notation
//        - evaluation
//
// Use postfix notation to evaluate the arithmetic expression input.
//
// Sample Inputs:
//      1+2+3+4+5+6+7+8+9+10-55
//      1-2-3-4-5-6-7-8-9-10+55
//      100/2/5/5/2*100
//      20*2+50
//
// Sample Outputs:
//      - + + + + + + + + + 1 2 3 4 5 6 7 8 9 10 55
//      1 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 55 -
//      0
//      + - - - - - - - - - 1 2 3 4 5 6 7 8 9 10 55
//      1 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 55 +
//      2
//      * / / / / 100 2 5 5 2 100
//      100 2 / 5 / 5 / 2 / 100 *
//      100
//      + * 20 2 50
//      20 2 * 50 +
//      90
fn main() {
    let mut input: String = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Arithmetic expression");

    let prefix: Vec<u8> = infix_to_prefix(&input);
    let postfix: Vec<u8> = infix_to_postfix(&input);
}
