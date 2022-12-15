from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().strip()

#lines = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

lines = [1 if c =='>' else -1 for c in lines]
floor = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6)]
tower = set(floor)
rocks = [
        [(0,2), (0,3), (0,4), (0,5)], 
        [(0,3), (1,2), (1,3), (1,4), (2,3)],
        [(0,2), (0,3), (0,4), (1,4), (2,4)],
        [(0,2), (1,2), (2,2), (3,2)],
        [(0,2), (0,3), (1,2), (1,3)],
        ]

def above_rock(rock):
    minx, maxx = min(x for (y,x) in rock), max(x for (y,x) in rock)
    edge = []
    for x in range(minx,maxx+1):
        top = (max(y for (y,x1) in rock if x == x1), x)
        edge.append(top)

    return edge


def belov_rock(rock):
    minx, maxx = min(x for (y,x) in rock), max(x for (y,x) in rock)
    edge = []
    for x in range(minx,maxx+1):
        bottom = (min(y-1 for (y,x1) in rock if x == x1), x)
        edge.append(bottom)

    return edge

def right_edge(rock):
    miny, maxy = min(y for (y,x) in rock), max(y for (y,x) in rock)
    edge = []
    for y in range(miny,maxy+1):
        rightmost = (y, max(x for (y1,x) in rock if y == y1))
        edge.append(rightmost)

    return edge

def left_edge(rock):
    miny, maxy = min(y for (y,x) in rock), max(y for (y,x) in rock)
    edge = []
    for y in range(miny,maxy+1):
        leftmost = (y,min(x for (y1,x) in rock if y == y1))
        edge.append(leftmost)

    return edge

def push_rock(rock, dx):
    if dx == 1:
        edge = right_edge(rock)
        if any(ex + dx > 6 for (_, ex) in edge):
            return rock
    else:
        edge = left_edge(rock)
        if any(ex + dx < 0 for (_, ex) in edge):
            return rock
    if any((ey,ex+dx) in tower for (ey,ex) in edge):
        return rock

    return [(y,x+dx) for (y,x) in rock]


def find_floors():
    lidx = 0
    floors = {}
    height = 0
    for i in range(5000):
        rock = rocks[i % 5]
        towertop = max((r[0] for r in tower), default=0)
        rockbot = towertop + 4

        rock = [(y+rockbot, x) for (y,x) in rock]

        while True:
            dx = lines[lidx]
            lidx = (lidx + 1) % len(lines)
            rock = push_rock(rock, dx)
            if any(r in tower for r in belov_rock(rock)):
                break
            rock = [(y-1, x) for (y,x) in rock]

        ys = set(y for (y,x) in rock)

        tower.update(rock)
        for y in ys:
            found = True
            for x in range(0, 7):
                if (y,x) not in tower:
                    found = False
                    break
            if found:
                state = (lidx, i%5)
                if state in floors:
                    above_floor = set()
                    for (ty,tx) in tower:
                        if ty >= y:
                            above_floor.add((ty-y,tx))

                    return 2659, (i-131), (lidx, i+1, above_floor)
                else:
                    floors[state] = (i, y)

total, repeats_in, state = find_floors()
ROCKS = 1000000000000
ROCKS -= 131

of_each, rocks_after = divmod(ROCKS, repeats_in)

total *= of_each
total += 211
lidx, i, tower = state
turns = 0
while turns < rocks_after-1:
    turns += 1
    rock = rocks[i % 5]
    towertop = max((r[0] for r in tower), default=0)
    rockbot = towertop + 4

    rock = [(y+rockbot, x) for (y,x) in rock]

    while True:
        dx = lines[lidx]
        lidx = (lidx + 1) % len(lines)
        rock = push_rock(rock, dx)
        if any(r in tower for r in belov_rock(rock)):
            break
        rock = [(y-1, x) for (y,x) in rock]

    tower.update(rock)
    i += 1

top = max(y for (y,x) in tower)
print(total + top)

