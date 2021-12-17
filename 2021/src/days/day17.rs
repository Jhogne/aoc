use itertools::Itertools;
use regex::Regex;

type Range = (i32, i32, i32, i32);

fn hits(mut dy: i32, mut dx: i32, (min_x, max_x, min_y, max_y): Range) -> bool {
    let (mut x, mut y) = (0, 0);
    while x <= max_x && y >= min_y {
        x += dx;
        y += dy;

        dx = 0.max(dx - 1);
        dy -= 1;

        if x <= max_x && x >= min_x && y <= max_y && y >= min_y {
            return true
        } 
    }
    false
}

pub fn solve_1(input: &str) -> String {
    let range: Range = Regex::new(r"(-?\d+)")
        .unwrap()
        .find_iter(input.trim())
        .map(|d| d.as_str().parse().unwrap())
        .next_tuple()
        .unwrap();
    let (_, max_x, min_y, _) = range;

    (min_y..100)
        .cartesian_product(0..=max_x)
        .filter(|&(y, x)| hits(y, x, range))
        .map(|(y, _)| (0..=y).sum::<i32>())
        .max()
        .unwrap()
        .to_string()
}


pub fn solve_2(input: &str) -> String {
    let range: Range = Regex::new(r"(-?\d+)")
        .unwrap()
        .find_iter(input.trim())
        .map(|d| d.as_str().parse().unwrap())
        .next_tuple()
        .unwrap();
    let (_, max_x, min_y, _) = range;

    (min_y..100)
        .cartesian_product(0..=max_x)
        .filter(|&(y, x)| hits(y, x, range))
        .count()
        .to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "target area: x=20..30, y=-10..-5";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "45");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "112");
    }
}

