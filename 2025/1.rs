use std::fs;

fn main() {
    let input: Vec<String> = fs::read_to_string("day1.in")
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    part1(input.clone());
    // part2(input.clone());
}

fn part1(input: Vec<String>) {
    let mut dial: i32 = 50;
    let mut num_zeros: i32 = 0;

    for line in input {
        let rotation = &line[0..1];
        let distance: i32 = match line[1..line.len()].parse() {
            Ok(num) => num,
            Err(e) => {
                eprintln!("Failed to parse integer: {}", e);
                // Handle the error as appropriate for your application
                return;
            }
        };

        if rotation == "L" {
            dial = (dial - distance) % 100;
        } else if rotation == "R" {
            dial = (dial + distance) % 100;
        }

        println!("After {}{}, dial is {}", rotation, distance, dial);

        if dial == 0 {
            num_zeros += 1;
        }
    }

    println!("Part 1 password is: {}", num_zeros);
}

fn modulo_minus(mut dial: i32, distance: i32) -> (i32, i32) {
    let mut num_zeros = 0;

    // Set the dial to maximum value if it is at 0
    if dial == 0 {
        dial = 100;
    }

    if (dial - distance) >= 0 {
        dial -= distance;
        if dial == 0 {
            num_zeros += 1;
        }
    } else {
        // Case when dial < distance
        dial -= distance;
        if dial < 0 {
            num_zeros += 1;
            // Apply the modulo operation
            dial += 100;
        }
    }

    return (dial, num_zeros);
}

fn part2(input: Vec<String>) {
    let mut dial: i32 = 50;
    let mut num_zeros: i32 = 0;

    for line in input {
        let rotation = &line[0..1];
        let distance: i32 = match line[1..line.len()].parse() {
            Ok(num) => num,
            Err(e) => {
                eprintln!("Failed to parse integer: {}", e);
                // Handle the error as appropriate for your application
                return;
            }
        };

        if rotation == "L" {
            if distance < 100 {
                let t = modulo_minus(dial, distance);
                dial = t.0;
                num_zeros = t.1;
            } else {
                for _ in 0..(distance / 100) {
                    let d: i32 = 100;
                    let t = modulo_minus(dial, d);
                    dial = t.0;
                    num_zeros = t.1;
                }
            }
        } else if rotation == "R" {
            dial = (dial + distance) % 100;
        }

        if dial == 0 {
            num_zeros += 1;
        }
    }

    println!("Part 2 password is: {}", num_zeros);
}
