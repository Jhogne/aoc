import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

moving = set()
solid = set()
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == "#":
            solid.add((y,x))
        if c == "O":
            moving.add((y,x))

east_edge = max([x for (_,x) in moving | solid]) + 1
south_edge = max([y for (y,_) in moving | solid]) + 1

def roll_north(moving):
    moved = set()
    for (y,x) in sorted(moving, key=lambda x: x[0]):
        while True:
            if (y, x) in moved or (y, x) in solid or y == -1:
                moved.add((y+1, x))
                break
            else:
                y -= 1
    return moved

def roll_south(moving):
    moved = set()
    for (y,x) in sorted(moving, key=lambda x: x[0],reverse=True):
        while True:
            if (y, x) in moved or (y, x) in solid or y == south_edge:
                moved.add((y-1, x))
                break
            else:
                y += 1
    return moved

def roll_west(moving):
    moved = set()
    for (y,x) in sorted(moving, key=lambda x: x[1]):
        while True:
            if (y, x) in moved or (y, x) in solid or x == -1:
                moved.add((y, x+1))
                break
            else:
                x -= 1
    return moved

def roll_east(moving):
    moved = set()
    for (y,x) in sorted(moving, key=lambda x: x[1],reverse=True):
        while True:
            if (y, x) in moved or (y, x) in solid or x == east_edge:
                moved.add((y, x-1))
                break
            else:
                x += 1
    return moved


#n = roll_north(moving)
#print(n)
#w = roll_west(n)
#print(w)
#s = roll_south(w)
#print(s)
#e = roll_east(s)
#print(e)
old = moving
moved = roll_east(roll_south(roll_west(roll_north(moving))))
cycles = 1
maps = {}
values = {}
while frozenset(old) not in maps:
    maps[frozenset(old)] = frozenset(moved)
    cycles += 1
    old = moved 
    moved = roll_east(roll_south(roll_west(roll_north(moved))))

cycle_end = len(maps)
cycle_start = 0
seen = {}
curr = frozenset(moving)
while curr != maps[frozenset(old)]:
    cycle_start += 1
    curr = maps[curr]

cs = cycle_start -1
ce = cycle_end
amt = (1000000000 - cs) % (ce-cs)
print(cs, ce, cs + amt)

for k,s in enumerate(maps):
    if k == cs + amt:
        total = 0
        for (y,_) in s:
            total += (south_edge - y)
        print(k,total)
