use itertools::Itertools;
use std::collections::HashSet;

const SIZE: usize = 10;

fn get_adjacent(y: usize, x: usize) -> Vec<(usize, usize)> {
    let xs = x.max(1)-1..=(SIZE-1).min(x+1);
    let ys = y.max(1)-1..=(SIZE-1).min(y+1);

    ys.cartesian_product(xs)
        .filter(|(y1, x1)| !(*x1 == x && *y1 == y))
        .collect()
}

fn step(octopi: &mut Vec<Vec<u32>>, y: usize, x: usize, flashed: &mut HashSet<(usize, usize)>) {
    octopi[y][x] += 1;
    if octopi[y][x] > 9 && !flashed.contains(&(y, x)) {
        flashed.insert((y, x));
        for (y1, x1) in get_adjacent(y, x) {
            step(octopi, y1, x1, flashed)
        }
    }
}

pub fn solve_1(input: &str) -> String {
    let mut octopi: Vec<Vec<u32>> = input.lines()
        .map(|l| l.chars()
             .map(|c| c.to_digit(10).unwrap())
             .collect())
        .collect();

    let mut flashes = 0;
    for _ in 0..100 {
        let mut flashed = HashSet::new();
        for (y, x) in (0..SIZE).cartesian_product(0..SIZE) {
            step(&mut octopi, y, x, &mut flashed)
        }

        flashes += flashed.len();

        octopi = octopi.iter()
            .map(|row| row.iter()
                 .map(|energy| if *energy > 9 { 0 } else { *energy })
                 .collect())
            .collect();
    }
    flashes.to_string()
}


pub fn solve_2(input: &str) -> String {
    let mut octopi: Vec<Vec<u32>> = input.lines()
        .map(|l| l.chars()
             .map(|c| c.to_digit(10).unwrap())
             .collect())
        .collect();
    let mut iterations: usize = 0;

    loop {
        let mut flashed = HashSet::new();
        for (y, x) in (0..SIZE).cartesian_product(0..SIZE) {
            step(&mut octopi, y, x, &mut flashed)
        }

        octopi = octopi.iter()
            .map(|row| row.iter()
                 .map(|energy| if *energy > 9 { 0 } else { *energy })
                 .collect())
            .collect();

        iterations += 1;

        if flashed.len() == SIZE * SIZE {
            return iterations.to_string();
        }
    } 
}

#[test]
fn example() {
    let input = "
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
        ".trim().to_string();

    println!("Part 1:");
    assert_eq!(solve_1(&input), "1656");

    println!("Part 2:");
    assert_eq!(solve_2(&input), "195");
}
