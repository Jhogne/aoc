use std::mem::swap;

use itertools::Itertools;

fn parse(input: &str) -> (usize, usize) {
    input.lines()
        .map(|s| s.chars()
             .last()
             .unwrap()
             .to_digit(10)
             .unwrap() as usize)
        .next_tuple()
        .unwrap()
}

fn move_pawn(from: usize, roll: usize) -> usize {
    ((from + roll - 1) % 10) + 1
}

pub fn solve_1(input: &str) -> String {
    let (mut pos, mut other_pos) = parse(input);
    let (mut p, mut other, mut rolls) = (0, 0, 0);

    for dice in (1..).step_by(3) {
        rolls += 3;
        let roll = 3 * dice + 3;

        pos = move_pawn(pos, roll);
        p += pos;
        if p >= 1000 {
            break;
        }

        swap(&mut p, &mut other);
        swap(&mut pos, &mut other_pos);
    }
    (other * rolls).to_string()
}

const ROLLS: [(usize, u64); 7] = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)];

struct PlayerState {
    state: [[u64; 11]; 21],
}

impl PlayerState {
    fn new(start: usize) -> PlayerState {
        let mut state = [[0; 11]; 21];
        state[0][start] = 1;
        PlayerState { state }
    }

    fn universes_playing(&self) -> u64 {
        self.state.iter().map(|r| r.iter().sum::<u64>()).sum()
    }

    fn next_winners(&mut self) -> u64 {
        let mut new_state = [[0; 11]; 21];
        let mut winners = 0;

        for (score, positions) in self.state.iter().enumerate() {
            for (space, universes) in positions.iter().enumerate() {
                if *universes == 0 {
                    continue;
                }

                for (roll, next_universes) in ROLLS {
                    let next_space = move_pawn(space, roll);
                    if score + next_space >= 21 {
                        winners += next_universes * universes;
                    } else {
                        new_state[score + next_space][next_space] += next_universes * universes;
                    }
                }
            }
        }
        self.state = new_state;
        winners
    }
}

pub fn solve_2(input: &str) -> String {
    let (pos, other_pos) = parse(input);
    let (mut won, mut other_won) = (0, 0);
    let (mut state, mut other_state) = (PlayerState::new(pos), PlayerState::new(other_pos));

    while state.universes_playing() > 0 {
        won += state.next_winners() * other_state.universes_playing();
        swap(&mut won, &mut other_won);
        swap(&mut state, &mut other_state);
    }

    won.to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str = "
Player 1 starting position: 4
Player 2 starting position: 8
        ";


    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(&INPUT.trim().to_string()), "739785");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT.trim().to_string()), "444356092776315");
    }
}

