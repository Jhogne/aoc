from itertools import product

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def get_neighbourhood(pos):
    return list(product(*[range(i-1, i+2) for i in pos]))

def active_neighbours(active, positions, me):
    return sum(pos in active for pos in positions if pos != me)

def solve(active):
    to_check = set(sum([get_neighbourhood(pos) for pos in active], []))
    for _ in range(6):
        next_active, next_check = set(), set()
        for pos in to_check:
            neighbourhood = get_neighbourhood(pos)
            amt = active_neighbours(active, neighbourhood, pos)
            if pos in active and (amt == 2 or amt == 3):
                next_active.add(pos)
                next_check.update(neighbourhood)
            elif pos not in active and amt == 3:
                next_active.add(pos)
                next_check.update(neighbourhood)
        active, to_check = next_active, next_check
    return len(next_active)


active3D = set([(x, y, 0) for x, row in enumerate(lines)
                for y, item in enumerate(row) if item == '#'])
active4D = set([(x, y, 0, 0) for x, row in enumerate(lines)
                for y, item in enumerate(row) if item == '#'])

print("Part 1:", solve(active3D))
print("Part 2:", solve(active4D))