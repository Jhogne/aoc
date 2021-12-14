use std::collections::HashMap;

use itertools::Itertools;

fn solve(input: &str, steps: usize) -> String {
    let (template, reactions) = input.split_once("\n\n").unwrap();

    let mut rules: HashMap<(_, _), _> = HashMap::new();
    for (lhs, rhs) in reactions.lines().map(|l| l.split_once(" -> ").unwrap()) {
        let from = lhs.chars().next_tuple().unwrap();
        let to = rhs.chars().next().unwrap();
        rules.insert(from, to);
    }

    let mut results = template.chars().tuple_windows().counts();

    for _ in 0..steps {
        for ((fst, snd), amt) in results.clone() {
            let btwn = rules[&(fst, snd)];
            *results.get_mut(&(fst, snd)).unwrap() -= amt;
            *results.entry((fst, btwn)).or_insert(0) += amt;
            *results.entry((btwn, snd)).or_insert(0) += amt;
        }
    }

    let mut counts = HashMap::new();
    for ((fst, _), amt) in results {
        *counts.entry(fst).or_insert(0) += amt;
    }

    *counts.get_mut(&template.chars().last().unwrap()).unwrap() += 1;

    let (min, max) = counts.values().minmax().into_option().unwrap();
    (max - min).to_string()

}

pub fn solve_1(input: &str) -> String {
    solve(input, 10)
}

pub fn solve_2(input: &str) -> String {
    solve(input, 40)
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "1588");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "2188189693529");
    }
}

