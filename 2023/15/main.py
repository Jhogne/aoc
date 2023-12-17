import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    line = f.read().strip().split(",")


#total = 0
#for s in line:
#    value = 0
#    for c in s:
#        value += ord(c)
#        value *= 17
#        value %= 256
#    print(value)
#    total += value
#
#print(total)
def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


total = 0
boxes = defaultdict(lambda: [])
for s in line:
    value = 0
    if "=" in s:
        l,n = s.split("=")
    else:
        l = s[:-1]
        n = -1
    value = hash(l)
    if n == -1:
        boxes[value] = [v for v in boxes[value] if v[0] != l]
    else:
        if any([v[0] == l for v in boxes[value]]):
            boxes[value] = [v if v[0] != l else (l,n) for v in boxes[value]]
        else:
            boxes[value].append((l,n))

p2 = 0
for b in boxes:
    for i,s in enumerate(boxes[b]):
        p2 += (b+1) * (i+1) * int(s[1])


p1 = sum([hash(l) for l in line])
print(p1)
print(p2)


