use itertools::Itertools;

fn get_adjacent(y: i32, x: i32) -> [(i32, i32); 9] {
    [
        (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
        (y, x - 1),     (y, x),     (y, x + 1),
        (y + 1, x - 1), (y + 1, x), (y + 1, x + 1),
    ]
}

struct Grid {
    img: Vec<usize>,
    min: i32,
    max: i32,
    pad: usize,
    alg: Vec<usize>
}

impl Grid {
    fn create(img: Vec<usize>, size: usize, alg: Vec<usize>) -> Grid {
        Grid {img, min: 0, max: size as i32, pad: 0, alg }
    }

    fn get(&self, y: i32, x: i32) -> usize {
        if y < self.min || x < self.min || y > self.max || x > self.max {
            return self.pad;
        }
        let (y, x) = (y - self.min, x - self.min);
        self.img[(y * ((self.max - self.min) + 1) + x) as usize]
    }

    fn count_light(&self) -> usize {
        self.img.iter().map(|&d| d as usize).sum()
    }

    fn enhance(&mut self) {
        let mut next = Vec::new();
        for i in self.min - 1..=self.max + 1 {
            for j in self.min - 1..=self.max + 1 {
                let idx = get_adjacent(i, j)
                    .into_iter()
                    .fold(0, |acc, (y, x)| acc << 1 | self.get(y, x));

                next.push(self.alg[idx]);
            }
        }
        self.img = next;
        self.min -= 1;
        self.max += 1; 
        self.pad = self.alg[self.pad * (self.alg.len() - 1)];
    }
}

fn solve(input: &str, iters: u8) -> usize {
    let (alg, img) = input.split_once("\n\n").unwrap();
    let to_nums = |c| if c == '#' { 1 } else { 0 };

    let alg = alg.chars()
        .map(to_nums)
        .collect_vec();

    let img = img.lines()
        .flat_map(|row| row.chars().map(to_nums))
        .collect_vec();
    let length = (img.len() as f32).sqrt() as usize;

    let mut grid = Grid::create(img, length - 1, alg);
    for _ in 0..iters {
        grid.enhance();
    }
    grid.count_light()
}

pub fn solve_1(input: &str) -> String {
    solve(input, 2).to_string()
}

pub fn solve_2(input: &str) -> String {
    solve(input, 50).to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "35");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "3351");
    }
}

