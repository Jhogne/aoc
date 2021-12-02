pub fn solve_1(input: &String) -> String {
    let (x,y) = input
        .split_whitespace()
        .collect::<Vec<_>>()
        .chunks(2)
        .map(|x| (x[0], x[1].parse::<u32>().unwrap()))
        .fold((0,0), |(x,y), (dir, amt)| match dir {
            "forward" => (x + amt, y),
            "up"      => (x, y - amt),
            "down"    => (x, y + amt),
            _         => unreachable!(),
        });

    (x * y).to_string()
}

pub fn solve_2(input: &String) -> String {
    let (x,y,_) = input
        .split_whitespace()
        .collect::<Vec<_>>()
        .chunks(2)
        .map(|x| (x[0], x[1].parse::<u32>().unwrap()))
        .fold((0,0,0), |(x,y,aim), (dir, amt)| match dir {
            "forward" => (x + amt, y + aim * amt, aim),
            "up"      => (x, y, aim - amt),
            "down"    => (x, y, aim + amt),
            _         => unreachable!(),
        });

    (x * y).to_string()
}    

#[test]
fn example() {
    let input = "forward 5
down 5
forward 8
up 3
down 8
forward 2
".to_string();

    assert_eq!(solve_1(&input), "150");
    assert_eq!(solve_2(&input), "900");
}
