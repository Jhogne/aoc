import math
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

free = set()
start, end = (-1,-1), (-1,-1)
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c != '#':
            free.add((y,x))
        if c == 'S':
            start = (y,x)
        if c == 'E':
            end = (y,x)

def bfs(start):
    q = [start]
    dists = defaultdict(lambda: math.inf)
    dists[start] = 0
    while q:
        y,x = q.pop(0)
        for n in [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]:
            if dists[n] == float('inf'):
                dists[n] = dists[(y,x)] + 1
                if n in free:
                    q.append(n)
    return dists

def free_n_away(y,x,n):
    res = []
    for dy in range(-n+1,n):
        for dx in range(-n+1,n):
            dist = abs(dy) + abs(dx)
            if dist >= n:
                continue
            if (y+dy, x+dx) in free:
                res.append(((y+dy, x+dx), dist))

    return res

s2e = bfs(start)
e2s = bfs(end)

def better_cheats(n):
    tot = 0
    cheats = {(y,x): free_n_away(y,x,n+1) for (y,x) in free}
    for cheat_start in cheats:
        fst = s2e[cheat_start]
        for pt,l in cheats[cheat_start]:
            cheat_dist = fst + e2s[pt] + l
            if s2e[end] - cheat_dist >= 100:
                tot += 1
    return tot

print(better_cheats(2))
print(better_cheats(20))
