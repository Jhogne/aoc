use std::{collections::HashMap, collections::HashSet};

use itertools::Itertools;

type Map<'a> = HashMap<&'a str, Vec<&'a str>>;

fn count_paths<'a>(from: &'a str, map: &Map<'a>, visited: &mut HashSet<&'a str>) -> usize {
    if from == "end" {
        return 1
    }

    if from.chars().next().unwrap().is_lowercase() {
        if visited.contains(&from) {
            return 0;
        }

        visited.insert(from);
    }

    let count = map.get(&from)
        .unwrap()
        .iter()
        .fold(0, |acc, to| acc + count_paths(to, map, visited));

    if from.chars().next().unwrap().is_lowercase() {
        visited.remove(&from);
    }

    count

}

pub fn solve_1(input: &str) -> String {
    let vals = input.lines().map(|l| l.split_once('-').unwrap());

    let mut map = HashMap::new();
    for (from, to) in vals {
        map.entry(from)
            .or_insert_with(Vec::new)
            .push(to);
        map.entry(to)
            .or_insert_with(Vec::new)
            .push(from);
    }

    count_paths("start", &map, &mut HashSet::new()).to_string()
}

fn count_paths2<'a>(from: &'a str, map: &Map<'a>, visited: &mut HashMap<&'a str, u8>) -> usize {
    if from == "end" {
        return 1
    }

    if from.chars().next().unwrap().is_lowercase() {
        let twice = visited.values().contains(&2);
        let curr = visited.entry(from).or_insert(0);

        if *curr >= 1 && twice {
            return 0;
        }

        *curr += 1;
    }

    let count = map
        .get(from)
        .unwrap()
        .iter()
        .fold(0, |acc, to| acc + count_paths2(to, map, visited));

    if from.chars().next().unwrap().is_lowercase() {
        *visited.get_mut(from).unwrap() -= 1;
    }

    count

}

pub fn solve_2(input: &str) -> String {
    let vals = input.lines().map(|l| l.split_once('-').unwrap());

    let mut map = HashMap::new();
    for (from, to) in vals {
        if from != "end" && to != "start" {
            map.entry(from)
                .or_insert_with(Vec::new)
                .push(to);
        }

        if to != "end" && from != "start" {
            map.entry(to)
                .or_insert_with(Vec::new)
                .push(from);
        }
    }
    count_paths2("start", &map, &mut HashMap::new()).to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT_SMALL: &str = 
        "
start-A
start-b
A-c
A-b
b-d
A-end
b-end
        ";

    const INPUT_MEDIUM: &str = 
        "
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
        ";

    const INPUT_LARGE: &str = 
        "
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
        ";



    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT_SMALL.trim().to_string()), "10");
        assert_eq!(solve_1(&INPUT_MEDIUM.trim().to_string()), "19");
        assert_eq!(solve_1(&INPUT_LARGE.trim().to_string()), "226");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT_SMALL.trim().to_string()), "36");
        assert_eq!(solve_2(&INPUT_MEDIUM.trim().to_string()), "103");
        assert_eq!(solve_2(&INPUT_LARGE.trim().to_string()), "3509");

    }
}

