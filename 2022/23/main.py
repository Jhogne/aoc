from collections import defaultdict
from itertools import count

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

y = 0
elves = set()
for line in lines:
    x = 0
    for c in line:
        if c == '#':
            elves.add((x,y))
        x += 1
    y += 1

DIRS = [[(-1,-1), (0,-1), (1,-1)], [(-1,1),(0,1),(1,1)], [(-1,-1),(-1,0),(-1,1)], [(1,1),(1,0),(1,-1)]]
turned = 0

for k in count(1):
    new = set()
    proposals = defaultdict(list)
    for elf in elves:
        found, skip = False, True
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dy == 0 and dx == 0:
                    continue
                if (elf[0]+dx, elf[1]+dy) in elves:
                    skip = False
        if not skip:
            for i in range(4):
                d = DIRS[(i+turned)%len(DIRS)]
                if all((elf[0]+dx,elf[1]+dy) not in elves for (dx,dy) in d):
                    proposals[(elf[0]+d[1][0],elf[1]+d[1][1])].append(elf)
                    found = True
                    break
        if not found:
            proposals[elf].append(elf)

    for pos,olds in proposals.items():
        if len(olds) == 1:
            new.add(pos)
        else:
            new.update(olds)
    
    turned += 1

    if new == elves:
        break

    elves = new

    if k == 10:
        xs = [x for x,_ in elves]
        ys = [y for _,y in elves]
        w,e,n,s = min(xs), max(xs), min(ys), max(ys)

        print((1+e-w)*(1+s-n) - len(elves))

print(k)

