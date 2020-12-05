from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def find_value(seats, lo, hi):
    new = (lo + hi) / 2
    if(not seats):
        return int(lo)
    if(seats[0] == 'F' or seats[0] == 'L'):
        return find_value(seats[1:], lo, new)
    if(seats[0] == 'B' or seats[0] == 'R'):
        return find_value(seats[1:], new, hi)

ids = []
for l in lines:
    ids.append(find_value(l[:-3], 0, 128) * 8 + find_value(l[-3:], 0, 8))
    
ids = sorted(ids)
print("Part 1:", ids[-1])
print("Part 2:", [i for i in range(ids[0], ids[-1]) if not i in ids][0])