use itertools::Itertools;

fn block([mut z, w]: [i64;2], [a, b, c]: [i64;3]) -> (i64, i64, i64, i64) {
    let mut x = (z % 26) + a;
    z /= b;
    x = if x == w { 1 } else { 0 };
    x = if x == 0 { 1 } else { 0 };
    let mut y = (25 * x) + 1;
    z *= y;
    y = (w + c) * x;
    z += y;
    (x, y, z, w)
}

fn solve_blocks(mut input: Vec<[i64;3]>, z: i64, mut decs: u32, ws: Vec<i64>) -> Option<Vec<i64>> {
    if z == 0 && input.is_empty() {
        return Some(Vec::new())
    }

    if 26_i64.pow(7 - decs) < z {
        return None
    }

    let inp = input.pop();
    if inp == None {
        return None
    }
    let inp = inp.unwrap();
    if inp[1] == 26 {
        decs += 1;
    }

    for w in ws.clone() {
        let z_new = block([z,w], inp).2;

        if let Some(mut p) = solve_blocks(input.clone(), z_new, decs, ws.clone()) {
            p.push(w);
            return Some(p)
        }
    }
    None
}

pub fn solve(input: &str, ws: Vec<i64>) -> String {
    let instructions = input.trim().lines().map(|l| l.split_whitespace().collect_vec()).rev().collect::<Vec<Vec<&str>>>();
    let mut first = Vec::new();

    let mut diffs = Vec::new();
    let mut curr = [0,0,0];
    let mut y_adds = 0;
    for ins in instructions.iter().rev() {
        if ins[0] == "inp" && curr != [0,0,0] {
            diffs.push(curr);
            curr = [0,0,0];
            y_adds = 0;
        }

        if ins[0] == "add" && ins[1] == "x" {
            if let Ok(n) = ins[2].parse::<i64>() {
                curr[0] = n;
            }
        } else if ins[0] == "div" && ins[1] == "z" {
            curr[1] = ins[2].parse::<i64>().unwrap();
        } else if ins[0] == "add" && ins[1] == "y" {
            y_adds += 1;
            if y_adds == 4 {
                curr[2] = ins[2].parse::<i64>().unwrap();
            }
        } 
        if diffs.is_empty() {
            first.push(ins);
        }
    }
    diffs.push(curr);

    let p = solve_blocks(diffs.into_iter().rev().collect(), 0, 0, ws).unwrap();
    p.into_iter().map(|d| d.to_string()).rev().join("")
}


pub fn solve_1(input: &str) -> String {
    solve(input, (1..=9).rev().collect())
}

pub fn solve_2(input: &str) -> String {
    solve(input, (1..=9).collect())
}

#[cfg(test)]
mod test {


    #[test]
    pub fn example_part_1() {
    }

    #[test]
    fn example_part_2() {
    }
}

