use std::collections::HashMap;

fn done(rooms: Vec<Vec<char>>, home_size: usize) -> bool {
    for (i, room) in rooms.iter().enumerate() {
        if room.len() != home_size {
            return false;
        }
        for occupant in room {
            if get_home(*occupant) != i {
                return false;
            }
        }
    }
    true
}

fn get_home(amph: char) -> usize {
    if amph == 'A' {
        return 0
    }
    if amph == 'B' {
        return 1
    }
    if amph == 'C' {
        return 2
    }
    if amph == 'D' {
        return 3
    }
    unreachable!()
}

fn move_cost(amph: char, steps: usize) -> usize {
    let mul = match amph {
        'A' => 1,
        'B' => 10,
        'C' => 100, 
        'D' => 1000,
        _ => unreachable!()
    };
    mul * steps
}

fn home_clear(amph: char, rooms: &[Vec<char>]) -> bool {
    for occupant in rooms[get_home(amph)].iter().rev() {
        if *occupant != amph {
            return false;
        }
    }
    true
}

fn path_clear(from: usize, to: usize, hallway: [char; 11]) -> bool {
    for spot in &hallway[from.min(to)+1..from.max(to)] {
        if *spot != ' ' {
            return false;
        }
    }
    true
}

fn hall_dist(from: usize, to: usize) -> usize {
    ((from as i32) - (to as i32)).abs() as usize
}

fn go_home(from: usize, hallway: [char; 11], rooms: Vec<Vec<char>>, home_size: usize) -> (usize, [char;11], Vec<Vec<char>>) {
    let amph = hallway[from];
    let (mut new_hallway, mut new_rooms) = (hallway, rooms.clone());
    new_rooms[get_home(amph)].push(amph);
    new_hallway[from] = ' ';
    let steps = (home_size - rooms[get_home(amph)].len()) + hall_dist(from, outside_home(amph));
    (steps, new_hallway, new_rooms)
}

fn home_from_room(amph: char, from: usize, hallway: [char; 11], rooms: Vec<Vec<char>>, home_size: usize) -> (usize, [char;11], Vec<Vec<char>>) {
    let (new_hallway, mut new_rooms) = (hallway, rooms.clone());
    new_rooms[get_home(amph)].push(amph);
    new_rooms[from].remove(0);
    let steps = (home_size - rooms[get_home(amph)].len()) + (1 + home_size - rooms[from].len()) + hall_dist(outside_room(from), outside_home(amph));
    (steps, new_hallway, new_rooms)
}

fn spot_from_room(to: usize, from: usize, hallway: [char; 11], rooms: Vec<Vec<char>>, home_size: usize) -> (usize, [char;11], Vec<Vec<char>>) {
    let (mut new_hallway, mut new_rooms) = (hallway, rooms.clone());
    new_hallway[to] = rooms[from][0];
    new_rooms[from].remove(0);
    let steps = 1 + (home_size - rooms[from].len()) + hall_dist(outside_room(from), to);
    (steps, new_hallway, new_rooms)
}

fn outside_home(amph: char) -> usize {
    2 * (get_home(amph) + 1)
}

fn outside_room(room_num: usize) -> usize {
    2 * (room_num + 1)
}

fn get_possible_spots(from: usize, hallway: [char; 11]) -> Vec<usize> {
    let mut possible = Vec::new();
    for (spot, occupant) in hallway[from..].iter().enumerate() {
        if *occupant != ' ' {
            break; 
        }
        let spot = spot + from;
        if spot != 2 && spot != 4 && spot != 6 && spot != 8 {
            possible.push(spot)
        }
    }
    for (spot, occupant) in hallway[..from].iter().rev().enumerate() {
        if *occupant != ' ' {
            break; 
        }
        let spot = from - spot - 1;
        if spot != 2 && spot != 4 && spot != 6 && spot != 8 && *occupant == ' ' {
            possible.push(spot)
        }
    }
    possible
}

type Rooms = Vec<Vec<char>>;
type Hallway = [char; 11];

fn solve(rooms: Rooms, hallway: Hallway, energy: usize, cache: &mut HashMap<(Rooms, Hallway), usize>, home_size: usize) -> usize {
    
    if done(rooms.clone(), home_size) {
        return energy
    }

    if cache.contains_key(&(rooms.clone(), hallway)) {
        return *cache.get(&(rooms, hallway)).unwrap()
    }

    let mut attempts = Vec::new();
    for (spot, occupant) in hallway.iter().cloned().enumerate() {
        if occupant == ' ' {
            continue;
        }

        if home_clear(occupant, &rooms) && path_clear(spot, outside_home(occupant), hallway) {
            let (steps, new_hallway, new_rooms) = go_home(spot, hallway, rooms.clone(), home_size);
            attempts.push(solve(new_rooms, new_hallway, energy + move_cost(occupant, steps), cache, home_size))
        }
    }

    if let Some(cost) = attempts.iter().min() {
        if cost < cache.get(&(rooms.clone(), hallway)).unwrap_or(&0) {
            cache.insert((rooms, hallway), *cost);
        }
        return *cost
    }

    for (room_num, room) in rooms.iter().enumerate() {
        if room.is_empty() {
            continue
        }

        let amph = room[0];

        if get_home(amph) == room_num && home_clear(amph, &rooms) {
            continue;
        }

        if home_clear(amph, &rooms) && path_clear(outside_room(room_num), outside_home(amph), hallway) {
           let (steps, new_hallway, new_rooms) = home_from_room(amph, room_num, hallway, rooms.clone(), home_size);
 
            attempts.push(solve(new_rooms, new_hallway, energy + move_cost(amph, steps), cache, home_size))
        }
    }

    if let Some(cost) = attempts.iter().min() {
        if cost < cache.get(&(rooms.clone(), hallway)).unwrap_or(&0) {
            cache.insert((rooms, hallway), *cost);
        }
        return *cost
    }

    for (room_num, room) in rooms.iter().enumerate() {
        if room.is_empty() {
            continue
        }

        let amph = room[0];

        if get_home(amph) == room_num && home_clear(amph, &rooms) {
            continue;
        }
        

        for candidate in get_possible_spots(outside_room(room_num), hallway) {
            let (steps, new_hallway, new_rooms) = spot_from_room(candidate, room_num, hallway, rooms.clone(), home_size);
            attempts.push(solve(new_rooms, new_hallway, energy + move_cost(amph, steps), cache, home_size));
        }
    }

    if let Some(cost) = attempts.iter().min() {
        if cost < cache.get(&(rooms.clone(), hallway)).unwrap_or(&0) {
            cache.insert((rooms, hallway), *cost);
        }
        return *cost
    }

    cache.insert((rooms, hallway), 999999);
    999999
}

fn parse(input: &str) -> Vec<Vec<char>> {
    let rows = input.lines().map(|l| l.chars().filter(|c| c.is_alphabetic()));
    let mut out = vec![Vec::new(); 4];
    for row in rows {
        for (i,c) in row.enumerate() {
            out[i].push(c);
        }
        
    }
    out
}

fn unfold(mut rooms: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let to_insert = [('D','D'), ('C','B'), ('B','A'), ('A','C')];
    for (i, (top, bot)) in to_insert.iter().enumerate() {
        rooms[i].insert(1, *top);
        rooms[i].insert(2, *bot);
    }
    rooms
}

pub fn solve_1(input: &str) -> String {
    solve(parse(input), [' '; 11], 0,  &mut HashMap::new(), 2).to_string()
}

pub fn solve_2(input: &str) -> String {
    solve(unfold(parse(input)), [' '; 11], 0,  &mut HashMap::new(), 4).to_string()
}

#[cfg(test)]
mod test {

    use super::{solve_1, solve_2};

    const INPUT: &str =
        "
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
        ";

    #[test]
    pub fn example_part_1() {
        assert_eq!(solve_1(INPUT), "12521");
    }

    #[test]
    fn example_part_2() {
        assert_eq!(solve_2(&INPUT), "44169");
    }
}

