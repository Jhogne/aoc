type Board = Vec<(usize, bool)>;

fn transpose<T: Copy>(a: Vec<T>, width: usize, height: usize) -> Vec<T> {
    let mut t: Vec<T> = Vec::with_capacity(a.len());
    for i in 0..width {
        for j in 0..height {
            t.push(a[j * width + i]);
        }
    }
    t
}

fn parse(input: &str) -> (Vec<usize>, Vec<Board>) {
    let mut parts = input.split("\n\n");
    let nums = parts
        .next()
        .unwrap()
        .split(',')
        .map(|s| s.parse::<usize>().unwrap())
        .collect();
    let boards: Vec<Board> = parts
        .map(
            |s| s
            .lines()
            .flat_map(
                |c| c
                .split_whitespace()
                .map(
                    |s| (s
                         .parse::<usize>()
                         .unwrap(), false)))
            .collect())
        .collect();
    (nums, boards)
}

fn has_won(board: &Board) -> bool {
    [board.to_vec(), transpose(board.to_vec(), 5, 5)]
        .concat()
        .chunks(5)
        .any(|r| r.iter().all(|(_, m)| *m))
}

fn sum_unmarked(board: &Board) -> usize {
    board
        .iter()
        .filter_map(|(n, m)| if !m { Some(n) } else { None })
        .sum()
}

fn mark(board: &Board, num: usize) -> Board {
    board
        .iter()
        .map(|(n, m)| (*n, *m || *n == num))
        .collect()
}

pub fn solve_1(input: &str) -> String {

    let (nums, mut boards) = parse(input);

    for num in nums {
        for board in &mut boards {
            *board = mark(board, num);

            if has_won(board) {           
                return (sum_unmarked(board) * num).to_string()
            }
        }
    }
    panic!("No solution found");
}

pub fn solve_2(input: &str) -> String {
    let (nums, mut boards) = parse(input);

    let mut won: Vec<_> = (0..boards.len()).collect();
    for num in nums {
        for (i, board) in boards.iter_mut().enumerate() {
            *board = mark(board, num);
            if has_won(board) {
                won.retain(|n| *n != i);
                if !won.is_empty() {
                    continue;
                }
                return (sum_unmarked(board) * num).to_string()
            }
        }
    }
    panic!("No solution found");
}

#[test]
fn example() {
    let input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
".to_string();

    assert_eq!(solve_1(&input), "4512");
    assert_eq!(solve_2(&input), "1924");
}
