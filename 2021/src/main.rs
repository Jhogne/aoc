use std::{fs,env};

mod sols;

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


fn get_day(day: u8) -> (fn(&String) -> String, fn(&String) -> String) {
    let f: (fn(&String) -> String, fn(&String) -> String) = match day {
        01 => (sols::day01::solve_1, sols::day01::solve_2),
        _ => panic!("This shouldn't happen :)"),
    };

    f
}


