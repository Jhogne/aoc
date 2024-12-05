import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    [rules, updates] = f.read().strip().split('\n\n')

rules = [(int(x) for x in l.split("|")) for l in rules.splitlines()]
updates = [[int(x) for x in l.split(",")] for l in updates.splitlines()]

befores, afters = defaultdict(lambda: []), defaultdict(lambda: [])
for before, after in rules:
    befores[before].append(after)
    afters[after].append(before)

p1 = 0
invalid = []
for l in updates:
    valid = True
    for i,d in enumerate(l):
        if any(x in l[:i] for x in befores[d]) or any(x in l[i:] for x in afters[d]):
            invalid.append(l)
            break
    if invalid[-1] != l:
        p1 += l[len(l) // 2]

p2 = 0
for l in invalid:
    curr = []
    while len(curr) < len(l):
        for d in l:
            if d in curr:
                continue
            if all(x in curr for x in befores[d] if x in l) and \
               all(x not in curr for x in afters[d] if x in l):
                    curr.append(d)
    p2 += curr[len(curr)//2]

print(p1)
print(p2)
