import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    rs,ps = f.read().strip().split("\n\n")

rules = {}
for r in rs.splitlines():
    name, rest = r.split("{")
    rest = rest[:-1].split(",")
    default = rest[-1]
    conds = []
    for ru in rest[:-1]:
        var, op,num, to = re.findall(r"([a|m|x|s])([\<|\>])(\d+):([a-zA-Z]+)", ru)[0]
        conds.append((var, op, int(num), to))
    rules[name] = (conds, default)

def apply_rule(x, m, a, s, rule):
    conds, default = rules[rule]
    for (var, op, num, to) in conds:
        if var == "x":
            var = x
        elif var == "m":
            var = m
        elif var == "a":
            var = a
        elif var == "s":
            var = s

        if op == "<":
            if var < num:
                return to
        elif op == ">":
            if var > num:
                return to
    return default

def split(s, num, op):
    if op == "<":
        s1 = (s[0], num-1)
        s = (num, s[1])
    else:
        s1 = (num+1, s[1])
        s = (s[0], num)
    return s, s1

def find_acceptable(x, m, a, s, rule):
    conds, default = rules[rule]
    for (var, op, num, to) in conds:
        if var == "x":
            x, x1 = split(x, num, op)
            yield(x1, m, a, s, to)
        elif var == "m":
            m, m1 = split(m, num, op)
            yield(x, m1, a, s, to)
        elif var == "a":
            a, a1 = split(a, num, op)
            yield(x, m, a1, s, to)
        elif var == "s":
            s, s1 = split(s, num, op)
            yield(x, m, a, s1, to)
    yield (x,m,a,s,default)

def p1():
    total = 0
    for part in ps.splitlines():
        x, m, a, s = re.findall(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part)[0]
        x, m, a, s = int(x), int(m), int(a), int(s)
        curr = apply_rule(x, m, a, s, "in")
    
        while curr != "R" and curr != "A":
            curr = apply_rule(x, m, a, s, curr)
    
        if curr == "A":
            total += x + m + a + s
    return total

def p2():
    q = list(find_acceptable((1,4000),(1,4000),(1,4000),(1,4000),"in"))
    total = 0
    while q:
        (x,m,a,s,rule) = q.pop()
        if rule == "A":
            xinc = 1+x[1]-x[0]
            minc = 1+m[1]-m[0]
            ainc = 1+a[1]-a[0]
            sinc = 1+s[1]-s[0]
            inc = xinc * minc * ainc * sinc
            total += inc
            continue
        if rule == "R":
            continue
        for res in find_acceptable(x,m,a,s,rule):
            q.append(res)
    return total

print(p1())
print(p2())
