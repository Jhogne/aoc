import re
import math
from functools import lru_cache, cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

with open('test.in', 'r') as f:
    lines = f.read().strip().splitlines()

garden_plot = set()
start = (-1,-1)
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == ".":
            garden_plot.add((y,x))
        if c == "S":
            garden_plot.add((y,x))
            start = (y,x)

seen = set()
@cache
def step(curr, remaining):
    if remaining == 0:
        return 1
    steps = 0
    for dy,dx in (1,0), (0,1), (-1,0), (0,-1):
        new = curr[0]+dy, curr[1]+dx
        new_inf = new[0]%len(lines), new[1]%len(lines[0])
        if new_inf in garden_plot:
            steps += step(new, remaining-1)
    return steps
    #if remaining == 0:
    #    return {curr}

    #steps = set()
    #for dy,dx in (1,0), (0,1), (-1,0), (0,-1):
    #    new = curr[0]+dy, curr[1]+dx
    #    new_inf = new[0]%len(lines), new[1]%len(lines[0])
    #    if new_inf in garden_plot:
    #        num = step(new, remaining-1)
    #        steps |= num
    #return steps

steps = step(start,1000)
print(steps)


ex = """...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........
"""

os = set()
for (y,l) in enumerate(ex.splitlines()):
    for (x,c) in enumerate(l):
        if c == "O":
            os.add((y,x))


#print(os)
#print(os-steps)
