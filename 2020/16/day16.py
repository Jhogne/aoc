import re
from collections import defaultdict
import time

start = time.time()
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n\n')

ranges = []
for rule in lines[0].split('\n'):
    a,b,c,d = re.search(r'(\d+)-(\d+) or (\d+)-(\d+)',rule).groups()
    ranges.append((int(a),int(b)))
    ranges.append((int(c),int(d)))

rate = 0
valid = []
for ticket in lines[2][16:].split('\n'):
    t = []
    for value in ticket.split(','):
        valid_ticket = any(lo <= int(value) <= hi for lo,hi in ranges)
        if not valid_ticket:
            break
        else:
            t.append(int(value))
    if not valid_ticket:
        rate += int(value)
    else:
        valid.append(t)
    
fields = defaultdict(list)
for ticket in valid:
    for index,value in enumerate(ticket):
        candidates = []
        for i,(lo,hi) in enumerate(ranges):
            if lo <= value <= hi:
                candidates.append(i//2)
        fields[index].append(candidates)

my_ticket = lines[1][13:].split(',')
done = []
order = []
while len(order) < len(my_ticket):
    for i,field in enumerate(fields):
        foo = set.intersection(*map(set, fields[field])) - set(done)
        if len(foo) == 1:
            order.append((field,list(foo)[0]))
            done += list(foo)

acc = 1
for idx,field in order:
    if field < 6:
        acc *= int(my_ticket[idx])

print("Part 1:",rate)
print("Part 2:",acc)
print(time.time() - start)
