use itertools::Itertools;

pub fn solve_1(input: &str) -> String {
    let (pts, inst) = input.split_once("\n\n").unwrap();
    let mut points: Vec<(usize, usize)>= pts.lines()
        .flat_map(|l| l.split(','))
        .map(|s| s.parse().unwrap())
        .tuples()
        .collect();

    let instructions: Vec<(&str, usize)> = inst.lines()
        .map(|l| l.split_at(11).1)
        .map(|s| s.split_once('=').unwrap())
        .map(|(d,n)| (d, n.parse().unwrap()))
        .collect();

    let (axis, n) = instructions[0];
    for (x, y) in points.iter_mut() {
        if axis == "y" && *y > n {
            *y -= 2 * (*y - n);
        } 
        if axis == "x" && *x > n {
            *x -= 2 * (*x - n);
        } 
    }

    points.iter().unique().count().to_string()
}


pub fn solve_2(input: &str) -> String {
    let (pts, inst) = input.split_once("\n\n").unwrap();
    let mut points: Vec<(usize, usize)>= pts.lines()
        .flat_map(|l| l.split(','))
        .map(|s| s.parse().unwrap())
        .tuples()
        .collect();

    let instructions: Vec<(&str, usize)> = inst.lines()
        .map(|l| l.split_at(11).1)
        .map(|s| s.split_once('=').unwrap())
        .map(|(d,n)| (d, n.parse().unwrap()))
        .collect();

    for (axis, n) in instructions {
        for (x,y) in points.iter_mut() {
            if axis == "y" && *y > n {
                *y -= 2 * (*y - n);
            } 
            if axis == "x" && *x > n {
                *x -= 2 * (*x - n);
            } 
        }
    }

    let max_x = points.iter().max_by_key(|(x, _)| x).unwrap().0;
    let max_y = points.iter().max_by_key(|(_, y)| y).unwrap().1;

    let mut img = vec![vec!["."; max_x+1]; max_y+1];
    for (x, y) in points {
        img[y][x] = "█";
    }
    img.into_iter().map(|r| r.join("")).join("\n")
}

#[cfg(test)]
mod test {

    use super::solve_1;

    const INPUT: &str =
        "
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
        ";

    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "17");
    }
}

