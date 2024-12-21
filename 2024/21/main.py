from functools import cache
from collections import defaultdict
import random 

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

num2coord = {"7": (0,0), "8": (0,1), "4": (1,0), "9": (0,2), "5": (1,1), "1": (2,0), "6": (1,2), "2": (2,1), "3": (2,2), "A": (3,2), "0": (3,1)}
coord2num = {num2coord[num] : num for num in num2coord}

dir2coord = {(-1,0): (0,1), (0,-1): (1,0), (1,0): (1,1), "A": (0,2), (0,1): (1,2)}
coord2dir = {dir2coord[di] : di for di in dir2coord}

dir2char = {(1,0): "v", (0,1): ">", (-1,0): "^", (0,-1): "<", "A": "A"}
char2dir = {dir2char[di] : di for di in dir2char}

char2coord = {c: dir2coord[char2dir[c]] for c in char2dir}

@cache
def moves_between(start, end, robot):
    q = [[start]]
    res = []
    if robot:
        nodes = coord2dir
    else:
        nodes = coord2num
    while q:
        path = q.pop(0)
        v = path[-1]
        if v == end:
            res.append(path)
            continue
        y,x = v
        for n in [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]:
            if n in nodes and n not in path:
                new_path = path.copy()
                new_path.append(n)
                q.append(new_path)

    minpath = len(min(res, key=len))
    minpaths = [p for p in res if len(p) == minpath]
    res1 = []
    for mp in minpaths:
        mp = pos2dirs(mp)
        mp.append("A")
        res1.append(''.join(mp))
    return least_moves(res1)

def least_moves(paths):
    moves = defaultdict(lambda: [])
    for p in paths:
        prev = p[0]
        steps = 0
        for s in p[1:]:
            if s == prev:
                continue
            steps += 1
            prev = s
        moves[steps].append(p)
    r = random.randint(0,len(moves[min(moves)])-1) # wtf
    return moves[min(moves)][r]

def pos2dirs(poss):
    res = []
    for prev,curr in zip(poss, poss[1:]):
        dy = curr[0] - prev[0]
        dx = curr[1] - prev[1]
        res.append(dir2char[(dy,dx)])
    return res

def shortest_paths(seq, curr, robot):
    if seq == "" or seq == []:
        return []
    target = seq[0]
    if robot:
        lookup = char2coord
    else:
        lookup = num2coord
    res = moves_between(lookup[curr],lookup[target], robot)

    return [res] + shortest_paths(seq[1:], target, robot)

@cache
def expand(seq, n):
    if n == 0:
        return len(seq)
    seq = "A" + seq
    tot = 0
    for s,e in zip(seq,seq[1:]):
        path = moves_between(char2coord[s], char2coord[e], True) 
        tot += expand(path, n-1)
        
    return tot

def my_seq(nums, n):
    paths = shortest_paths(nums, "A", False)
    tot = 0
    for segment in paths:
        expanded = expand(segment, n)
        tot += expanded

    return tot * int(nums[:3])

p1s, p2s = set(), set()
# is this even a real solution?
# something is wrong with least_moves so just test a bunch of different
# random values and take the lowest of them.. maybe I will go back to 
# this in the future but not now
for i in range(1000):
    p1, p2 = 0, 0
    for l in lines:
        p1 += my_seq(l, 2)
        p2 += my_seq(l, 25)
    p1s.add(p1)
    p2s.add(p2)
    expand.cache_clear()
    moves_between.cache_clear()
print(min(p1s))
print(min(p2s))
