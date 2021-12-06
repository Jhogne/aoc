#![feature(test)]

use std::{fs,env};

mod days;

type Solution = fn(&str) -> String;

fn main() {
    let day: usize = env::args()
        .collect::<Vec<String>>()
        .get(1)
        .expect("Provide a day")
        .parse()
        .expect("Provide a number");

    let (input, part_1, part_2) = get_day(day);

    println!("{}", part_1(&input));
    println!("{}", part_2(&input));
}

fn get_day(day: usize) -> (String, Solution, Solution) {
    let f = format!("inputs/{}.txt", day);
    let input = fs::read_to_string(f).expect("Day not done yet");
    let (part_1, part_2) = get_solutions(day);

    (input, part_1, part_2)
}

fn get_solutions(day: usize) -> (Solution, Solution) {
    match day {
        1 => (days::day01::solve_1, days::day01::solve_2),
	 	2 => (days::day02::solve_1, days::day02::solve_2),
	 	3 => (days::day03::solve_1, days::day03::solve_2),
	 	4 => (days::day04::solve_1, days::day04::solve_2),
	 	5 => (days::day05::solve_1, days::day05::solve_2),
	 	6 => (days::day06::solve_1, days::day06::solve_2),
        _ => unreachable!()
    }
}

#[cfg(test)]
mod test {
    extern crate test;
    use test::Bencher;
    use crate::get_day;
    use crate::Solution;
    use std::env;

    pub fn setup_bench() -> (Solution, Solution, String) {
        let day: usize = env::var("AOC_DAY")
            .expect("Provide a day")
            .parse()
            .expect("Provide a number");
        let (input, part_1, part_2) = get_day(day);
        (part_1, part_2, input)
    }

    #[bench]
    pub fn bench_part_1(b: &mut Bencher) {
        let (solver, _, data) = setup_bench();
        b.iter(|| solver(&data))
    }

    #[bench]
    pub fn bench_part_2(b: &mut Bencher) {
        let (_, solver, data) = setup_bench();
        b.iter(|| solver(&data))
    }
}
