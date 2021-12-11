use itertools::Itertools;
use std::collections::HashSet;

pub fn solve_1(input: &str) -> String {
    let outputs = input.lines()
        .map(|line| line.split_once(" | ")
             .unwrap()
             .1
             .split_whitespace());

    let lengths = [2, 3, 4, 7];
    outputs
        .flat_map(|segs| segs.filter(|seg| lengths.contains(&seg.len())))
        .count()
        .to_string()
}

pub fn solve_2(input: &str) -> String {
    let lines = input.lines()
        .flat_map(|line| line.split('|'))
        .map(|segs| segs.split_whitespace()
             .map(|seg| seg
                .chars()
                .collect::<HashSet<_>>())
             .collect::<Vec<_>>());

    let mut count: u32 = 0;
    for (inp,out) in lines.tuples() {
        let mut digit = vec![HashSet::new(); 10];

        for segments in inp.iter() {
            let n = match segments.len() {
                2 => 1,
                3 => 7,
                4 => 4,
                7 => 8,
                _ => continue,
            };
            digit[n].extend(segments);
        }

        for segments in inp.iter() {
            let n = match segments.len() {
                6 => if !digit[1].is_subset(segments) {
                    6
                } else if digit[4].is_subset(segments) {
                    9
                } else {
                    0
                },
                5 => if digit[1].is_subset(segments) {
                    3
                } else if digit[4].union(segments).count() == 6 {
                    5
                } else {
                    2
                },
                _ => continue,
            };
            digit[n].extend(segments);
        };
        count += out.iter()
            .map(|seg| digit.iter().position(|d| d == seg).unwrap())
            .join("")
            .parse::<u32>()
            .unwrap();
    }
    count.to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
        ";

    const INPUT_SMALL: &str = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf";

    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "26");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT_SMALL.trim().to_string()), "5353");
        assert_eq!(solve_2(&INPUT.trim().to_string()), "61229");
    }
}

