import re
import math
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

corrupted = []
for i in range(len(lines)):
    x,y = (int(x) for x in re.findall(r"\d+", lines[i]))
    corrupted.append((y,x))

start = 0,0
target = 70,70
nbytes = 1024
def neighbours(y,x):
    return [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]

def bfs(corrupted):
    q = [start]
    dists = defaultdict(lambda: math.inf)
    dists[start] = 0
    while q:
        pos = q.pop(0)
        for n in neighbours(*pos):
            if dists[n] == float('inf') and n not in corrupted and start[0] <= n[0] <= target[0] and start[1] <= n[1] <= target[1]:
                dists[n] = dists[pos] + 1
                q.append(n)
    return dists[target]

def find_first_blocked():
    for j in range(len(lines)):
        if bfs(set(corrupted[0:j])) == math.inf:
            return lines[j-1]

print(bfs(set(corrupted[:nbytes])))
print(find_first_blocked())
