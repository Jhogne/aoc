use itertools::Itertools;

fn get_adjacent(x: usize, y: usize, max_x: usize, max_y: usize) -> Vec<(usize, usize)> {
    let xs = x.max(1)-1..=max_x.min(x+1);
    let ys = y.max(1)-1..=max_y.min(y+1);

    xs.cartesian_product(ys)
        .filter(|(x1,y1)| (*x1 == x) ^ (*y1 == y))
        .collect()
}

pub fn solve_1(input: &str) -> String {
    let map: Vec<Vec<u32>> = input
        .lines()
        .map(|line| line
             .chars()
             .map(|c| c.to_digit(10).unwrap())
             .collect())
        .collect();

    let (max_x, max_y) = (map[0].len()-1, map.len()-1, );
    let mut risk = 0;
    for (y, x) in (0..map.len()).cartesian_product(0..map[0].len()) {
        if get_adjacent(x, y, max_x, max_y).iter().all(|(x1, y1)| map[y][x] < map[*y1][*x1]) {
                risk += map[y][x] + 1;
            }
    }
    risk.to_string()
}


fn get_basin_size(x: usize, y: usize, map: &mut Vec<Vec<(u32, bool)>>) -> u32 {
    if map[y][x].1 || map[y][x].0 == 9 {
        return 0
    }
    map[y][x].1 = true;
    let (max_x, max_y) = (map[0].len() - 1, map.len() - 1);
    let mut size = 1;
    for (x1, y1) in get_adjacent(x, y, max_x, max_y) {
        size += get_basin_size(x1, y1, map);
    }
    size
}

pub fn solve_2(input: &str) -> String {
    let mut map: Vec<Vec<_>> = input
        .lines()
        .map(|line| line
             .chars()
             .map(|c| (c.to_digit(10).unwrap(), false))
             .collect())
        .collect();
     
    let (max_x, max_y) = (map[0].len()-1, map.len()-1);
    let mut basins = Vec::new();
    for (y, x) in (0..map.len()).cartesian_product(0..map[0].len()) {
        if get_adjacent(x, y, max_x, max_y).iter().all(|(x1, y1)| map[y][x] < map[*y1][*x1]) {
                basins.push(get_basin_size(x, y, &mut map));
            }
    }

    let (a, b, c) = basins.iter().sorted().rev().next_tuple().unwrap();
    (a * b * c).to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
2199943210
3987894921
9856789892
8767896789
9899965678
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "15");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "1134");
    }
}

