import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().split('\n\n')

seeds = re.findall(r"\d+",lines[0])
seeds = [int(x) for x in seeds]

ms = []
for l in lines[1:]:
    bs = []
    for b in l.splitlines()[1:]:
        ns = re.findall(r"\d+", b)
        ns = [int(x) for x in ns]
        m = [ns[1], ns[1]+ns[2], ns[0]]
        bs.append(m)
    ms.append(bs)

def lookup(s, m):
    for r in ms[m]:
        if r[0] <= s < r[1]:
            return s - r[0] + r[2]
    return s

def p1():
    minl = math.inf
    for s in seeds:
        for m in range(len(ms)):
            s = lookup(s, m)
        minl = min(minl, s)
    return minl

def p2():
    minl = math.inf
    for i in range(0,len(seeds),2):
        for s in range(seeds[i],seeds[i]+seeds[i+1]):
            for m in range(len(ms)-1,-1,-1):
                s = lookup(s, m)
            minl = min(minl, s)
    return minl

print(p1())
#print(p2()) # takes veeeeery long to run :(
