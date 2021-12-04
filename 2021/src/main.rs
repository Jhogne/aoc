use std::{fs,env};

mod sols;

type Solution = fn(&str) -> String;
fn main() {
    let usr_in = &env::args().collect::<Vec<String>>()[1].parse::<u8>();
    let day = match usr_in {
        Ok(n) => n,
        Err(_) => panic!("Invalid day"),
    };
    let in_file = format!("inputs/{}.txt", day);
    let input = fs::read_to_string(in_file).unwrap();
    let fns = get_day(*day);

    println!("{}", fns.0(&input));
    println!("{}", fns.1(&input));
}


fn get_day(day: u8) -> (Solution, Solution) {
    match day {
        1 => (sols::day01::solve_1, sols::day01::solve_2),
	 	2 => (sols::day02::solve_1, sols::day02::solve_2),
	 	3 => (sols::day03::solve_1, sols::day03::solve_2),
	 	4 => (sols::day04::solve_1, sols::day04::solve_2),
        _ => unreachable!()
    }
}


