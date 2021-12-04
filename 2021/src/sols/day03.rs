pub fn solve_1(input: &str) -> String {
    let iters: Vec<_> = input.lines().collect();
    let len = iters[0].len();

    let mut gamma = 0;
    let mut epsilon = 0;
    for i in 0..len {
        let amt = iters.iter().filter(|curr| curr.chars().nth(i).unwrap() == '1' ).count();

        gamma <<= 1;
        epsilon <<= 1;
        if amt > iters.len() / 2 {
            gamma += 1;
        } else {
            epsilon += 1;
        }
    }
    (gamma * epsilon).to_string()
}

fn find_rating(mut nums: Vec<&str>, comparator: fn(usize, usize) -> bool) -> &str {
    for i in 0..nums[0].len() {
        let amt = nums.iter().filter(|curr| curr.chars().nth(i).unwrap() == '1' ).count();

        let cmp = if comparator(amt, nums.len() - amt) {'1'} else {'0'};

        nums.retain(|s| s.chars().nth(i).unwrap() == cmp);

        if nums.len() == 1 {
            return nums[0];
        }
    }
    unreachable!()
}

pub fn solve_2(input: &str) -> String {
    let iters: Vec<_> = input.lines().collect();
    let o2 = isize::from_str_radix(find_rating(iters.clone(), |x, y| x >= y), 2).unwrap();
    let co2 = isize::from_str_radix(find_rating(iters.clone(), |x, y| x < y), 2).unwrap();
    (o2 * co2).to_string()
}

#[test]
fn example() {
    let input = 
"00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
".to_string();

    assert_eq!(solve_1(&input), "198");
    assert_eq!(solve_2(&input), "230");
}
