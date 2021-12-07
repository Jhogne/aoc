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

#[test]
fn example() {
    let input = "16,1,2,0,4,2,7,1,2,14".to_string();

    assert_eq!(solve_1(&input), "37");
    assert_eq!(solve_2(&input), "168");
}
