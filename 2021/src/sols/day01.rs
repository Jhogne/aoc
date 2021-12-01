pub fn solve_1(input: &String) -> String {
    let depths = input
        .lines()
        .map(|d| d.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();
    depths.windows(2).filter(|x| x[1] > x[0]).count().to_string()
}


pub fn solve_2(input: &String) -> String {
    let depths = input
        .lines()
        .map(|d| d.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();
    let sums = depths
        .windows(3)
        .map(|x| x.into_iter().sum())
        .collect::<Vec<u32>>();
    sums.windows(2).filter(|x| x[1] > x[0]).count().to_string()
}


#[test]
fn example() {
    let input = "199
200
208
210
200
207
240
269
260
263".to_string();

    assert_eq!(solve_1(&input), "7");
    assert_eq!(solve_2(&input), "5");
}

