pub fn solve_1(input: &str) -> String {
    let depths = input
        .lines()
        .map(|d| d.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();
    depths.windows(2).filter(|x| x[1] > x[0]).count().to_string()
}


pub fn solve_2(input: &str) -> String {
    let depths = input
        .lines()
        .map(|d| d.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();
    let sums = depths
        .windows(3)
        .map(|x| x.iter().sum())
        .collect::<Vec<u32>>();
    sums.windows(2).filter(|x| x[1] > x[0]).count().to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "
199
200
208
210
200
207
240
269
260
263";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "7");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "5");
    }
}
