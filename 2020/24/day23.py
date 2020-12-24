from collections import defaultdict
import time

start = time.time()
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

tiles = {}
for y in range(-75,75):
    for x in range(-75,75):
        tiles[complex(x,y)] = False


for line in lines:
    pos = 0+0j
    i = 0
    while i < len(line):
        if line[i] == 'e':
            pos += 1
            i += 1
        elif line[i] == 'w':
            pos -= 1
            i += 1
        elif line[i] == 's' and line[i+1] == 'w':
            pos += 1j
            i += 2
        elif line[i] == 's' and line[i+1] == 'e':
            pos += 1+1j
            i += 2
        elif line[i] == 'n' and line[i+1] == 'w':
            pos += -1-1j
            i += 2
        elif line[i] == 'n' and line[i+1] == 'e':
            pos -= 1j
            i += 2
        else:
            print(line[i] + line[i+1])
    tiles[pos] = not tiles[pos]

print("Part 1:",sum(tiles.values()))
neighbours = [1, -1, 1j, -1j, 1+1j, -1-1j]
def adjacent(tile):
    count = 0
    for n in neighbours:
        if tile + n in tiles and tiles[tile+n]:
            count += 1
    return count

for i in range(100):
    next_day = tiles.copy()
    for tile in tiles:
        if tiles[tile] and (adjacent(tile) == 0 or adjacent(tile) > 2):
            next_day[tile] = False
        elif not tiles[tile] and adjacent(tile) == 2:
            next_day[tile] = True
    tiles = next_day

print("Part 2:",sum(tiles.values()))

print(time.time() - start)