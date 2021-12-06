use std::collections::HashMap;

fn live_after(days: usize, lifetime: usize, seen: &mut HashMap<(usize, usize), usize>) -> usize {
    if lifetime >= days {
        return 1;
    }

    if seen.contains_key(&(lifetime, days)) {
        return *seen.get(&(lifetime, days)).unwrap();
    }

    let alive = live_after(days - lifetime - 1, 6, seen) + live_after(days - lifetime - 1, 8, seen);
    seen.insert((lifetime, days), alive);
    alive 
}

pub fn solve(input: &str, days: usize) -> String {
    let fishes = input.trim().split(',').map(|c| c.parse().unwrap());

    let seen = &mut HashMap::new();
    let mut count: usize= 0;

    for fish in fishes {
        count += live_after(days, fish, seen);
    }
    count.to_string()
}

pub fn solve_1(input: &str) -> String {
    solve(input, 80)
}

pub fn solve_2(input: &str) -> String {
    solve(input, 256)
}

#[test]
fn example() {
    let input = "3,4,3,1,2".to_string();

    assert_eq!(solve_1(&input), "5934");
    assert_eq!(solve_2(&input.to_string()), "26984457539");
}
