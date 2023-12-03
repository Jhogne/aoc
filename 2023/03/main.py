import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

nums = []
symbols = set()
gears = set()
for y, l in enumerate(lines):
    d = ['',[]]
    for x, c in enumerate(l):
        if c == '*':
            gears.add((x,y))
        if c.isdigit():
            d[0] += c
            d[1].append((x,y))
        elif c != '.':
            symbols.add((x,y))
        if not c.isdigit() and len(d[0]) > 0:
            nums.append(d) 
            d = ['',[]]
    if d != [',',[]]:
        nums.append(d)

def symbol_neighbour(x, y):
    for dy in [y-1,y,y+1]:
        for dx in [x-1,x,x+1]:
            if (dx, dy) in symbols:
                return True

    return False


total = 0
for d, poss in nums:
    for x, y in poss:
        if symbol_neighbour(x,y):
            total += int(d)
            break
print(total)


def num_neighbours(x, y):
    ns = []
    found = set()
    for dy in [y-1,y,y+1]:
        for dx in [x-1,x,x+1]:
            for d, poss in nums:
                if (dx,dy) in poss and (d,poss[0]) not in found:
                    ns.append(int(d))
                    found.add((d,poss[0]))
                    break

    return ns 

total = 0
for x,y in gears:
    ns = num_neighbours(x,y) 
    if len(ns) == 2:
        total += math.prod(ns)

print(total)
