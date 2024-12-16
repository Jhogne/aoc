import math
from collections import defaultdict
import heapq

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

maze = set()
start, end = (-1,-1), (-1,-1)

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == '#':
            continue
        if c == 'S':
            start = (y,x)
        elif c == 'E':
            end = (y,x)
        maze.add((y,x))

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def get_neighbours(pos,di):
    for i in range(len(dirs)):
        y = pos[0] + dirs[i][0]
        x = pos[1] + dirs[i][1]
        if (y, x) in maze:
            if i == di:
                yield (y,x), i, 1
            else:
                yield (y,x), i, 1001


def best_path(start, di):
    distances = defaultdict(lambda: (math.inf, 99))
    distances[start] = (0,di)
    q = [(0, (di,start))]
    
    while q:
        dist, (di, curr) = heapq.heappop(q)
    
        if dist > distances[curr][0]:
            continue
    
        for n,di,weight in get_neighbours(curr, di):
            ndist = dist + weight
    
            if ndist < distances[n][0]:
                distances[n] = (ndist, di)
                heapq.heappush(q, (ndist, (di, n)))

    return distances

start_distances = best_path(start, 0)

p2 = 0
for i,(y,x) in enumerate(maze):
    before, di = start_distances[(y,x)]
    if before > start_distances[end][0]:
        continue
    after_distances = best_path((y,x), di)
    if before + after_distances[end][0] == start_distances[end][0]:
        p2 += 1

print(start_distances[end][0])
print(p2)
