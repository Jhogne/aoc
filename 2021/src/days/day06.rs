use std::collections::HashMap;

fn alive_after(days: usize, seen: &mut HashMap<usize, usize>) -> usize {
    if days <= 7 {
        return 2
    }

    if days <= 9 {
        return 3
    }

    if seen.contains_key(&days) {
        return *seen.get(&days).unwrap();
    }

    let alive = alive_after(days - 7, seen) + alive_after(days - 9, seen);
    seen.insert(days, alive);
    alive 
}

pub fn solve(input: &str, days: usize) -> String {
    let fishes = input
        .trim()
        .split(',')
        .map(|c| c.parse::<usize>().unwrap());

    let seen = &mut HashMap::new();
    let mut count: usize= 0;

    for fish in fishes {
        count += alive_after(days - fish, seen);
    }
    count.to_string()
}

pub fn solve_1(input: &str) -> String {
    solve(input, 80)
}

pub fn solve_2(input: &str) -> String {
    solve(input, 256)
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "3,4,3,1,2";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "5934");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "26984457539");
    }
}

