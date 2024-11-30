import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict
from copy import deepcopy

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()


bricks = []
for l in lines:
    x,y,z,x1,y1,z1 = [int(n) for n in re.findall(r"\d+", l)]

    brick = []
    for bx in range(x,x1+1):
        for by in range(y,y1+1):
            for bz in range(z,z1+1):
                brick.append([bx,by,bz])
    brick = sorted(brick, key=lambda x: x[2])
    bricks.append(brick)

bricks = sorted(bricks, key=lambda x: x[0][2])

def fall(bricks):
    lowest = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(len(bricks)):
        zpos = 0
        for (x,y,_) in bricks[i]:
            zpos = max(zpos, lowest[x][y])
        zpos += 1
    
        minz = math.inf
        for block in bricks[i]:
            minz = min(minz, block[2])
    
        for m in range(len(bricks[i])):
            bricks[i][m][2] = zpos + (bricks[i][m][2] - minz)
            lowest[bricks[i][m][0]][bricks[i][m][1]] = bricks[i][m][2]
    return bricks

bricks = fall(bricks)

def p1():
    for i in range(len(bricks)):
        blocks = set()
        for block in bricks[i]:
            blocks.add(tuple(block))
        bricks[i] = blocks
    
    supported_by = defaultdict(lambda: [])
    supports  = defaultdict(lambda: [])
    
    for i,brick in enumerate(bricks):
        below = set()
        for (x,y,z) in brick:
            below.add((x,y,z-1))
    
        for j,brick2 in enumerate(bricks):
            if i == j:
                continue
            
            if len(below & set(brick2)) > 0:
                supports[j].append(i)
                supported_by[i].append(j)
    
    nofalls = {i for i in range(len(bricks))}
    falls = {i for i in range(len(bricks))}
    
    for candidate in nofalls.copy():
        removable = True
        for above in supports[candidate]:
            if supported_by[above] == [candidate]:
                removable = False
                break
        if removable:
            falls.remove(candidate)
        else:
            nofalls.remove(candidate)
    return len(nofalls)

total = 0
for idx in range(len(bricks)):
    prev = [brick for i,brick in enumerate(bricks) if i != idx]
    after = fall(deepcopy(prev))
    fallen = 0
    for i in range(len(after)):
        if prev[i] != after[i]:
            fallen += 1
    total += fallen

print(p1())
print(total)
