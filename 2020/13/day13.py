from math import inf
from itertools import count

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

ts = int(lines[0])
buses = [(offset,int(id)) for offset,id in enumerate(lines[1].split(',')) if id != 'x']

best = (inf, 0)
for _,bus in buses:
    best = min(best, (bus - ts % bus, bus))

acc = 1
step = 1
for offset,bus in buses:
    for i in count(acc,step):
        if ((i + offset) % bus == 0):
            acc = i
            step *= bus
            break

print("Part 1:", best[0]*best[1])
print("Part 2:",acc)
