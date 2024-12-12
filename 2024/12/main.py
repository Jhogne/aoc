import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('test.in', 'r') as f:
    lines = f.read().strip().splitlines()

grid = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[(y,x)] = c


def neighbours(y,x):
    return [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

def all_neighbours(y,x):
    return neighbours(y,x) + [(y+1, x+1), (y-1, x+1), (y+1, x-1), (y-1, x-1)]


seen = set()
def bfs(start):
    q = [start]
    shape = set()
    while q:
        pos = q.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        shape.add(pos)

        for n in neighbours(*pos):
            if n in grid and grid[start] == grid[n] and grid[n] not in seen:
                q.append(n)
    return shape

def sort_fences(fences):
    q = [fences[0]]
    res = []
    while q:
        pos = q.pop(0)
        if pos in res:
            continue

        res.append(pos)

        for n in neighbours(*pos):
            if n in fences:
                q.append(n)
    return res


def find_perim(points):
    fences = []
    for (y,x) in points:
        for (dy,dx) in neighbours(y,x):
            if (dy,dx) not in points:
                fences.append((dy,dx))

    return fences 

tot = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        shape = bfs((y,x))
        if len(shape) > 0:
            perim = find_perim(shape)
            print(perim)
            ordered_fences = sort_fences(perim)
            print(ordered_fences)
            #print(shape, perim)
            #tot += perim * len(shape)


print(tot)



