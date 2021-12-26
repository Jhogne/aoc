use itertools::Itertools;

pub fn solve_1(input: &str) -> String {
    let mut map = input.lines().map(|l| l.chars().collect_vec()).collect_vec();

    let mut count = 0;
    loop {
        count += 1;

        let mut next_map = vec![vec!['.';map[0].len()];map.len()];
        for (y,row) in map.iter().enumerate() {
            for (x,dir) in row.iter().enumerate() {
                if *dir == '>' {
                    if map[y][(x+1)%map[0].len()] == '.' {
                        next_map[y][(x+1)%map[0].len()] = '>';
                    } else {
                        next_map[y][x] = '>';
                    }
                }
            }

        }
        for (y,row) in map.iter().enumerate() {
            for (x,dir) in row.iter().enumerate() {
                if *dir == 'v' {
                    if (map[(y+1)%map.len()][x] == '>' || map[(y+1)%map.len()][x] == '.') && next_map[(y+1)%map.len()][x] != '>' {
                        next_map[(y+1)%map.len()][x] = 'v';
                    } else {
                        next_map[y][x] = 'v';
                    }
                }
            }
        }
        if map == next_map {
            break
        }
        map = next_map;

    }
    count.to_string()
}


pub fn solve_2(_input: &str) -> String {

    "not implemented".to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "58");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "not implemented");
    }
}

