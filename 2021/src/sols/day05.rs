use itertools::Itertools;
use std::collections::HashMap;

fn count_overlap(segments: Vec<(i32, i32, i32, i32)>) -> usize {
    let mut visited = HashMap::new();
    for (mut x1, mut y1, x2, y2) in &segments {
        let dx = (x2 - x1).signum();
        let dy = if dx == 0 { 
            (y2 - y1).signum()
        } else {
            (y2 - y1) / (x2 - x1).abs()
        };
    
        loop {
            let amt = visited.entry((x1, y1)).or_insert(0);
            *amt += 1;

            if (x1, y1) == (*x2, *y2) {
                break;
            }

            x1 += dx;
            y1 += dy;
        }
       
    }
    visited.values().filter(|n| **n > 1).count()
}

pub fn solve_1(input: &str) -> String {
    let segs: Vec<_> = input
        .lines()
        .filter_map(|s| s.split(|c| !char::is_numeric(c))
            .filter_map(|s| s.parse().ok())
            .collect_tuple())
        .filter(|(x1, y1, x2, y2)| x1 == x2 || y1 == y2)
        .collect();

    count_overlap(segs).to_string()
}

pub fn solve_2(input: &str) -> String {
    let segs: Vec<_> = input
        .lines()
        .filter_map(|s| s.split(|c| !char::is_numeric(c))
            .filter_map(|s| s.parse().ok())
            .collect_tuple())
        .collect();

    count_overlap(segs).to_string()
}

#[test]
fn example() {
    let input = "0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
".to_string();

    assert_eq!(solve_1(&input), "5");
    assert_eq!(solve_2(&input), "12");
}
