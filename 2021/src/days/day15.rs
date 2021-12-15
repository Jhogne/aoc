use std::collections::{HashMap, BinaryHeap};
use core::cmp::Reverse;

use itertools::Itertools;

fn get_adjacent((x, y): (usize, usize), (max_x, max_y): (usize, usize)) -> Vec<(usize, usize)> {
    let xs = x.max(1)-1..=max_x.min(x+1);
    let ys = y.max(1)-1..=max_y.min(y+1);

    xs.cartesian_product(ys)
        .filter(|(x1,y1)| (*x1 == x) ^ (*y1 == y))
        .collect()
}

fn dijkstra(graph: Vec<Vec<usize>>) -> usize {

    let mut q = BinaryHeap::new();
    let mut dists = HashMap::new();

    let end = (graph[0].len() - 1, graph.len() - 1);

    dists.insert((0, 0), 0);
    q.push(Reverse((0, (0, 0))));

    while let Some(Reverse((dist, pt))) = q.pop() {
        for adj in get_adjacent(pt, end) {
            let alt = dist + graph[adj.1][adj.0];

            if alt < *dists.get(&adj).unwrap_or(&usize::MAX) {
                dists.insert(adj, alt);
                q.push(Reverse((alt, adj)));
            }
        }
        if pt == end {
            break;
        }
    }

    dists[&end]
}

pub fn solve_1(input: &str) -> String {
    let m: Vec<Vec<_>> = input.lines()
        .map(|l| l
             .chars()
             .map(|c| c.to_digit(10).unwrap() as usize)
             .collect())
        .collect();

    dijkstra(m).to_string()
}


pub fn solve_2(input: &str) -> String {
    let small: Vec<Vec<_>> = input.lines()
        .map(|l| l
             .chars()
             .map(|c| c.to_digit(10).unwrap() as usize)
             .collect())
        .collect();

    let x_limit = small.len();
    let y_limit = small[0].len();
    let mut m = vec![vec![0; small[0].len() * 5]; small.len() * 5];
    for i in 0..5 {
        for j in 0..5 {
            for y in 0..x_limit {
                for x in 0..y_limit {
                    m[x_limit * i + y][y_limit * j + x] = ((small[y][x] + i + j - 1) % 9) + 1;
                }
            }
        }
    }

    dijkstra(m.clone()).to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "40");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "315");
    }
}

