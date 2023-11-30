from itertools import count
import re
import math
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

#lines = """1=-0-2
#12111
#2=0=
#21
#2=01
#111
#20012
#112
#1=-1=
#1-12
#12
#1=
#122
#""".splitlines()
lines = "0122-0==-=211==-2-200".splitlines()

s = 0
for line in lines:
    k = 1
    t = 0
    for d in reversed(line):
        if d == '-':
            t -= 1*k
        elif d == '=':
            t -= 2*k
        else:
            t += int(d)*k
        k *= 5
    s += t

NS = ['2','1','0','-','=']

t = s
k = 1
while k < s:
    k *= 5
o = ''
while k != 0:
    res = ''
    best = None
    if t < 0:
        for n in NS[-3:]:
            if n == '-':
                m = -k
            elif n == '=':
                m = -2*k
            else:
                m = int(n)*k
            if best == None or abs(t - m) < abs(t-best):
                best = m
                res = n
    else:
        for n in NS[:3]:
            m = int(n)*k
            if best == None or abs(t - m) < abs(t-best):
                best = m
                res = n

    o += res
    t = t - best
    k //= 5
print(o)
