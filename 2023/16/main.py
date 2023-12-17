import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

hsplitters, vsplitters = set(), set()
lmirrors, rmirrors = set(), set()

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == "|":
            vsplitters.add((y,x))
        elif c == "-":
            hsplitters.add((y,x))
        elif c == "/":
            lmirrors.add((y,x))
        elif c == "\\":
            rmirrors.add((y,x))

ymin, xmin = 0, 0
ymax, xmax = len(lines)-1, len(lines[0])-1

def find_largest(starts):
    energizes = []
    for (ds,ps) in starts:
        q = [(ds, ps)]
        seen, traveled = set(), set()
        while q:
            d,pos = q.pop(0)
            
            if not (ymin <= pos[0] <= ymax and xmin <= pos[1] <= xmax):
                continue
        
            if (d,pos) in traveled:
                continue
        
            seen.add(pos) 
            traveled.add((d,pos))
            
            if pos in lmirrors:
                d = (-d[1], -d[0])
            elif pos in rmirrors:
                d = (d[1], d[0])
            elif pos in hsplitters and d[1] == 0:
                q.append(((0,1), pos))
                q.append(((0,-1), pos))
                continue
            elif pos in vsplitters and d[0] == 0:
                q.append(((1,0), pos))
                q.append(((-1,0), pos))
                continue
        
            q.append((d, (pos[0] + d[0], pos[1]+d[1])))
        energizes.append(len(seen))
    return max(energizes)


nstarts = [((1,0),(0,x)) for x in range(xmax+1)]
sstarts = [((-1,0),(ymax,x)) for x in range(xmax+1)]
wstarts = [((0,1),(y,0)) for y in range(ymax+1)]
estarts = [((0,-1),(y,xmax)) for y in range(ymax+1)]

p1 = [((0,1),(0,0))]
p2 = nstarts + sstarts + wstarts + estarts 

print(find_largest(p1))
print(find_largest(p2))
