import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Grid is represented in a regular 2D tile
# . is current node {dir} is neighbours
#   nw ne
#   w  .  e
#      sw se

dirs = {
    "e": 1 + 0j,
    "w": -1 + 0j,
    "sw": 0 + 1j,
    "se": 1 + 1j,
    "nw": -1 - 1j,
    "ne": 0 - 1j
}


def flip_tiles(instructions):
    black = set()
    for instruction in instructions:
        pos = 0 + 0j
        for ins in re.findall("e|w|sw|se|nw|ne", instruction):
            pos += dirs[ins]

        black.add(pos) if pos not in black else black.remove(pos)

    return black


def count_neighbours(tile, black):
    return sum(tile + d in black for d in dirs.values())


def get_neighbourhood(pos):
    return [pos] + [pos + d for d in dirs.values()]


def day(black):
    to_check = set(sum([get_neighbourhood(b) for b in black], []))
    next_black = set()
    for tile in to_check:
        amt = count_neighbours(tile, black)
        if tile in black and not (amt == 0 or amt > 2):
            next_black.add(tile)
        elif tile not in black and amt == 2:
            next_black.add(tile)
    return next_black


init = flip_tiles(lines)
state = init.copy()
for _ in range(100):
    state = day(state)

print("Part 1:", len(init))
print("Part 2:", len(state))
