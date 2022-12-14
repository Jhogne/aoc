from ast import literal_eval
from itertools import count, pairwise

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

walls = set()
for line in lines:
    pts = map(literal_eval, line.split(' -> '))
    for (x1, y1), (x2, y2) in pairwise(pts):
        walls.update(
            (x,y)
            for x in range(min(x1, x2), max(x1, x2) + 1)
            for y in range(min(y1, y2), max(y1, y2) + 1)
        )

def drop_sand(occupied, abyss=None):
    x, y = 500, 0
    while True:
        if y == abyss:
            return None

        if (x, y) not in occupied:
            y += 1
        elif (x-1, y) not in occupied:
            x -= 1
        elif (x+1, y) not in occupied:
            x += 1
        else:
            return (x, y-1)

def p1(occupied):
    abyss = max(x[1] for x in occupied) + 1
    for n in count():
        sand = drop_sand(occupied, abyss)
        if not sand:
            print(n)
            break
    
        occupied.add(sand)

def p2(occupied):
    for n in count():
        if (500, 0) in occupied:
            print(n)
            break

        occupied.add(drop_sand(occupied))

p1(walls.copy())

f = max(x[1] for x in walls) + 2
walls.update((x, f) for x in range(499 - f, 501 + f))

p2(walls)
