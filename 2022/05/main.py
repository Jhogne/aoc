import re
from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = [l.splitlines() for l in f.read().split('\n\n')]

instructions = [[int(i) for i in re.findall(r"\d+", l)] for l in lines[1]]

stacks = [[] for _ in range(0, 9)]
for line in reversed(lines[0][:-1]):
    for (i, crate) in enumerate(line[1::4]):
        if crate != ' ':
            stacks[i].append(crate)

def p1(stacks, frm, to, amt):
   for _ in range(amt):
        crate = stacks[frm].pop()
        stacks[to].append(crate)

def p2(stacks, frm, to, amt):
    stacks[to] += stacks[frm][-amt:]
    stacks[frm] = stacks[frm][:-amt]

def move_crates(stacks, move_strategy):
    for [amt, frm, to] in instructions: 
        move_strategy(stacks, frm-1, to-1, amt)

    return ''.join(s[-1] for s in stacks)

print(move_crates(deepcopy(stacks), p1))
print(move_crates(deepcopy(stacks), p2))
