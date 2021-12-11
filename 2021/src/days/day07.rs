use itertools::Itertools;

pub fn solve_1(input: &str) -> String {
    let crabs: Vec<i32> = input
        .trim()
        .split(',')
        .map(|s| s.parse().unwrap())
        .collect();

    let target = *crabs
        .iter()
        .sorted()
        .nth(crabs.len() / 2)
        .unwrap();

    crabs
        .iter()
        .map(|n| (n - target).abs())
        .sum::<i32>()
        .to_string()
}

fn fuel(steps: i32) -> i32 {
    steps * (steps + 1) / 2
}

pub fn solve_2(input: &str) -> String {
    let crabs: Vec<i32> = input
        .trim()
        .split(',')
        .map(|s| s.parse().unwrap())
        .collect();

    let (min, max) = crabs
        .iter()
        .minmax()
        .into_option()
        .unwrap();

    (*min..=*max)
        .map(|i| crabs
             .iter()
             .map(|n| fuel((n - i).abs()))
             .sum::<i32>())
        .min()
        .unwrap()
        .to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "16,1,2,0,4,2,7,1,2,14";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "37");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "168");
    }
}

