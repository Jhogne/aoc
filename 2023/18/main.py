import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('test.in', 'r') as f:
    lines = f.read().strip().splitlines()


dug = set()
curr = (0,0)
for l in lines:
    _, _, col = l.split()
    col = col[2:-1]
    l,d = col[:-1],col[-1]
    l = int(l,16)
    print(l,d)
    if d == "0":
        new = (curr[0], curr[1] + l)
    elif d == "2":
        new = (curr[0], curr[1] - l)
    elif d == "1":
        new = (curr[0] + l, curr[1])
    elif d == "3":
        new = (curr[0] - l, curr[1])

    #d,l,_ = l.split()
    #l = int(l)
    #if d == "R":
    #    new = (curr[0], curr[1] + l)
    #elif d == "L":
    #    new = (curr[0], curr[1] - l)
    #elif d == "D":
    #    new = (curr[0] + l, curr[1])
    #elif d == "U":
    #    new = (curr[0] - l, curr[1])

    #miny = min(curr[0], new[0])
    #minx = min(curr[1], new[1])
    #maxy = max(curr[0], new[0])
    #maxx = max(curr[1], new[1])
    #diffy = maxy - miny
    #diffx = maxx - minx
    #for y in range(0, diffy+1):
    #    for x in range(0, diffx+1):
    #        toadd = (miny+y, minx+x)
    #        dug.add(toadd)
    #curr = new

miny = min(dug, key=lambda x: x[0])[0]
minx = min(dug, key=lambda x: x[1])[1]
maxy = max(dug, key=lambda x: x[0])[0]
maxx = max(dug, key=lambda x: x[1])[1]

#inside = set()
#amt = 0
#for y in range(miny,maxy+1):
#    count = 0
#    for x in range(minx,maxx+1):
#        if (y,x) in dug and (y-1,x):
#            count += 1
#        elif (y,x) not in dug and count % 2 == 1:
#            amt += 1
#            inside.add((y,x))

start = sorted(dug)[1]
start = (1,1)
q = [start]
seen = set()
while q:
    c = q.pop()
    if c in seen or c in dug:
        continue
    seen.add(c)
    for dy,dx in (0,1), (0,-1), (1,0), (-1,0):
        q.append((c[0]+dy, c[1]+dx))


print(len(dug))
print(len(dug)+len(seen))


#for y in range(miny,maxy+1):
#    for x in range(minx, maxx+1):
#        if (y,x) in dug:
#            print("#", end='')
#        else:
#            print(".", end='')
#    print()
