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
	 	7 => (days::day07::solve_1, days::day07::solve_2),
	 	8 => (days::day08::solve_1, days::day08::solve_2),
	 	9 => (days::day09::solve_1, days::day09::solve_2),
	 	10 => (days::day10::solve_1, days::day10::solve_2),
	 	11 => (days::day11::solve_1, days::day11::solve_2),
	 	12 => (days::day12::solve_1, days::day12::solve_2),
	 	13 => (days::day13::solve_1, days::day13::solve_2),
	 	14 => (days::day14::solve_1, days::day14::solve_2),
	 	15 => (days::day15::solve_1, days::day15::solve_2),
	 	16 => (days::day16::solve_1, days::day16::solve_2),
	 	17 => (days::day17::solve_1, days::day17::solve_2),
	 	18 => (days::day18::solve_1, days::day18::solve_2),
	 	19 => (days::day19::solve_1, days::day19::solve_2),
	 	20 => (days::day20::solve_1, days::day20::solve_2),
	 	21 => (days::day21::solve_1, days::day21::solve_2),
	 	22 => (days::day22::solve_1, days::day22::solve_2),
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
