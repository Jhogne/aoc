use regex::Regex;

#[derive(Clone, PartialEq)]
enum Elem {
    Num(usize),
    Pair(Box<(Elem,Elem)>)
}

impl Elem {
    fn magnitude(self) -> usize {
        match self {
            Elem::Num(n) => n,
            Elem::Pair(c) => {
                let (a,b) = *c;
                3 * a.magnitude() + 2 * b.magnitude()
            }
        }
    }

    fn create_pair(lhs: Elem, rhs: Elem) -> Elem {
        Elem::Pair(Box::new((lhs, rhs)))
    }

    fn create_num_pair(lhs: usize, rhs: usize) -> Elem {
        Elem::create_pair(Elem::Num(lhs), Elem::Num(rhs))
    }
}

fn parse(s: &str) -> Elem {
    let remove_brackets = Regex::new(r"\[(.+)\]").unwrap();
    let content = remove_brackets.captures(s).unwrap().get(1).unwrap().as_str();
    let digit_pair = Regex::new(r"^(\d),(\d)$").unwrap();
    let digit_first = Regex::new(r"^(\d),(.+)$").unwrap();
    let digit_last = Regex::new(r"^(.+),(\d)$").unwrap();

    if let Some(pair) = digit_pair.captures(content) {
        return Elem::create_num_pair(pair[1].parse().unwrap(), pair[2].parse().unwrap())
    } 

    if let Some(caps) = digit_first.captures(content) {
        return Elem::create_pair(Elem::Num(caps[1].parse().unwrap()), parse(&caps[2]))
    } 

    if let Some(caps) = digit_last.captures(content) {
        return Elem::create_pair(parse(&caps[1]), Elem::Num(caps[2].parse().unwrap()))
    } 

    let mut count = 0;
    let mut idx = 0;
    for (i, c) in content.chars().enumerate() {
        if c == '[' {
            count += 1;
        } else if c == ']' {
            count -= 1;
        } else if count == 0 {
            idx = i;
        }
    }

    let (lhs,rhs) = content.split_at(idx);
    let rhs = rhs.split_at(1).1;
    Elem::create_pair(parse(lhs), parse(rhs))
}

fn add(lhs: Elem, rhs: Elem) -> Elem {
    Elem::create_pair(lhs, rhs)
}

fn split(n: usize) -> Elem {
    let floor = n / 2;
    let ceil = (n + 1) / 2;
    Elem::create_num_pair(floor, ceil)
}

fn explode(e: Elem) -> (usize, Elem, usize, bool) {
    match e {
        Elem::Pair(c) => match *c {
            (Elem::Num(n), Elem::Pair(c)) => {
                if let (Elem::Num(a), Elem::Num(b)) = *c {
                    return (a, Elem::create_num_pair(n, 0), b, true)
                }
                unreachable!()
            }
            (Elem::Pair(c), Elem::Num(n)) => {
                if let (Elem::Num(a), Elem::Num(b)) = *c {
                    return (a, Elem::create_num_pair(0, n), b, true)
                } 
                unreachable!()
            }
            (Elem::Num(a), Elem::Num(b)) => (a, Elem::Num(0), b, true),
            (lhs, rhs) => {
                let (a, e, b, d) = explode(lhs);
                (a, Elem::create_pair(e, inc_left(rhs, b)), 0, d)
            }
        }
        _ => unreachable!()
    }

}

fn inc_left(e: Elem, i: usize) -> Elem {
    match e {
        Elem::Num(n) => Elem::Num(n+i),
        Elem::Pair(c) => Elem::create_pair(inc_left((*c).0, i), (*c).1)
    }
}

fn inc_right(e: Elem, i: usize) -> Elem {
    match e {
        Elem::Num(n) => Elem::Num(n+i),
        Elem::Pair(c) => Elem::create_pair((*c).0, inc_right((*c).1, i))
    }
}

fn explode_once(curr: Elem, depth: u32, done: bool) -> (usize, Elem, usize, bool) {
    match curr.clone() {
        Elem::Pair(_) if depth == 4 && !done => explode(curr),
        Elem::Pair(c) => {
            let (a, b) = *c;
            let (l_keep, left, right_inc, actioned) = explode_once(a, depth+1, done);
            let (left_inc, right, r_keep, actioned) = explode_once(b, depth+1, done || actioned);

            let left = inc_right(left, left_inc);
            let right = inc_left(right, right_inc);
            (l_keep, Elem::create_pair(left, right), r_keep, done || actioned)
        }
        Elem::Num(n) => (0, Elem::Num(n), 0, done),
    }
}

fn split_once(curr: Elem, done: bool) -> (Elem, bool) {
    match curr {
        Elem::Num(n) if n >= 10 && !done => (split(n), true),
        Elem::Num(n) => (Elem::Num(n), done),
        Elem::Pair(c) => {
            let (a, b) = *c;
            let (left, actioned) = split_once(a, done);
            let (right, actioned) = split_once(b, done || actioned);

            (Elem::create_pair(left, right), done || actioned)
        }
    }
}

fn reduce(mut prev: Elem) -> Elem {
    let mut changed = true;
    while changed {
        changed = false;
        let (_, mut exploding, _, mut exploded) = explode_once(prev, 0, false);
        while exploded {
            let (_, tmp, _, e) = explode_once(exploding, 0, false);
            exploding = tmp;
            exploded = e;
            changed = true;
        }
        let (splitting, splitted) = split_once(exploding, false);

        changed = splitted || changed;
        prev = splitting;
    }
    prev 
}

pub fn solve_1(input: &str) -> String {
    let mut nums = Vec::new();
    for l in input.trim().lines() {
        nums.push(parse(l));
    }

    let mut res = nums.get(0).unwrap().clone();
    for num in nums.into_iter().skip(1) {
        res = reduce(add(res, num));
    }
        
   res.magnitude().to_string()
}


pub fn solve_2(input: &str) -> String {
    let mut nums = Vec::new();
    for l in input.trim().lines() {
        nums.push(parse(l));
    }

    let mut highest = 0;
    for x in nums.iter().cloned() {
        for y in nums.iter().cloned() {
            let sum = reduce(add(x.clone(), y)).magnitude();
            if sum > highest {
                highest = sum;
            }
        }
    }
        
   highest.to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
        ";

    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1("[9,1]".trim()), "29");
        assert_eq!(solve_1(INPUT.trim()), "4140");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "3993");
    }
}

