from itertools import combinations
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

freqs = defaultdict(lambda: [])
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c != ".":
            freqs[c].append((i,j))

minx,maxx,miny,maxy = 0, len(lines[0]), 0, len(lines)

def in_bounds(pos):
    return miny <= pos[0] < maxy and minx <= pos[1] < maxx

p1, p2 = set(), set()
for nodes in freqs.values():
    for (y,x),(y1,x1) in combinations(nodes, r=2):
        dx,dy = x-x1, y-y1
        
        next_pt = (y + dy, x + dx)
        next_pt_anti = (y1 - dy, x1 - dx)
        if in_bounds(next_pt):
            p1.add(next_pt)
        if in_bounds(next_pt_anti):
            p1.add((y1-dy,x1-dx))

        while in_bounds(next_pt):
            p2.add(next_pt)
            next_pt = (next_pt[0] + dy, next_pt[1] + dx)
        while in_bounds(next_pt_anti):
            p2.add(next_pt_anti)
            next_pt_anti = (next_pt_anti[0] - dy, next_pt_anti[1] - dx)

    if len(nodes) > 1:
        p2 |= set(nodes)

print(len(p1))
print(len(p2))
