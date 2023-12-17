import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict
from copy import deepcopy

with open('real.in', 'r') as f:
    lines = f.read().split("\n\n")

def vertical_mirror(pattern):
    possible_lines = []
    for (i,l),l1 in zip(enumerate(pattern), pattern[1:]):
        if l == l1:
            possible_lines.append(i)

    matches = set()
    for match in possible_lines:
        good = True
        for y in range(0,len(pattern)-match-1):
            if pattern[match+y+1] != pattern[match-y]:
                good = False
                break
            if match-y == 0:
                break
        if good:
            matches.add(match+1)
    return matches

def rotate(pattern):
    rotated = []
    for y in range(len(pattern[0])):
        col = []
        for x in range(len(pattern)):
            col.append(pattern[x][y])
        rotated.append(col)
    return rotated

p1, p2 = 0, 0
for i,pattern in enumerate(lines):
    pattern = pattern.splitlines()
    pattern1 = rotate(pattern)
    oldv = vertical_mirror(pattern)
    oldh = vertical_mirror(pattern1)
    
    v1 = next(iter(oldv)) if oldv else 0
    h1 = next(iter(oldh)) if oldh else 0
    p1 += v1 * 100 + h1

    pattern = [list(s) for s in pattern] 
    patterns = []
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            patterns.append(deepcopy(pattern))
            if patterns[-1][y][x] == "#":
                patterns[-1][y][x] = "."
            else:
                patterns[-1][y][x] = "#"
    found = False
    for pattern in patterns:
        pattern1 = rotate(pattern)
        h = vertical_mirror(pattern1) - oldh
        v = vertical_mirror(pattern) - oldv
        if len(v) > 0:
            v = v.pop()
        else:
            v = 0

        if len(h) > 0:
            h = h.pop()
        else:
            h = 0
        if v > 0 and v != oldv:
            p2 += v * 100
            found = True
            break
        if h > 0 and h != oldh:
            p2 += h
            found = True
            break
    if not found:
        print(i)

print(p1)
print(p2)

