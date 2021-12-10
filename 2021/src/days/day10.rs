use itertools::Itertools;
use core::str::Chars;

fn reduce_chunks(chars: Chars<'_>) -> Result<Vec<char>, char> {
    let matches = |c| match c {
        ')' => '(',
        ']' => '[',
        '}' => '{',
        '>' => '<',
        _ => unreachable!(),
    };

    let mut stack = Vec::new();
    for c in chars {
        if matches!(c, '(' | '[' | '{' | '<') {
            stack.push(c);
        } else if matches(c) != stack.pop().unwrap() {
            return Err(c)
        }
    }

    Ok(stack) 
}

pub fn solve_1(input: &str) -> String {
    let lines = input.lines().map(|l| l.chars());
    let scores = |c| match c {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137,
        _ => unreachable!(),
    };

    let mut score: usize = 0;
    for chars in lines {
        if let Err(c) = reduce_chunks(chars)  {
            score += scores(c);
        }
    }

    score.to_string()
}


pub fn solve_2(input: &str) -> String {
    let lines = input.lines().map(|l| l.chars());
    let scores = |c| match c {
        '(' => 1,
        '[' => 2,
        '{' => 3,
        '<' => 4,
        _ => unreachable!(),
    };

    let mut required = Vec::new();
    for chars in lines {
        if let Ok(remains) = reduce_chunks(chars)  {
            required.push(remains);
        }
    }

    required.iter()
        .map(|comp| comp.iter()
             .rev()
             .fold(0, |tot: u64, next| tot * 5 + scores(*next)))
        .sorted()
        .nth(required.len() / 2)
        .unwrap()
        .to_string()
}

#[test]
fn example() {
    let input = "
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
    ".trim();

    println!("Example 1");
    assert_eq!(solve_1(&input), "26397");

    println!("Example 2");
    assert_eq!(solve_2(&input), "288957");
}
