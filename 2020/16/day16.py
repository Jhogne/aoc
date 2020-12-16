import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    rules, my, others = f.read().strip().split('\n\n')

# Add all tuples (low,high) for all ranges in the list
ranges = []
for rule in rules.split('\n'):
    l1, r1, l2, r2 = re.search(r'(\d+)-(\d+) or (\d+)-(\d+)', rule).groups()
    ranges.append((int(l1), int(r1)))
    ranges.append((int(l2), int(r2)))

# Filter out the invalid passwords and solve part 1
p1 = 0
valids = []
for ticket in others.splitlines()[1:]:
    ticket = [int(n) for n in ticket.split(',')]
    invalids = [value for value in ticket if not any(
        lo <= int(value) <= hi for lo, hi in ranges)]
    p1 += sum(invalids)
    if len(invalids) == 0:
        valids.append(ticket)

# Find the index of the possible rules for each number in each ticket
fields = defaultdict(list)
for ticket in valids:
    for field_idx, value in enumerate(ticket):
        candidates = set(
            [i // 2 for i, (lo, hi) in enumerate(ranges) if lo <= value <= hi])
        fields[field_idx].append(candidates)

# Find the only possible rule for each number index and solve part 2
my_ticket = my.splitlines()[1].split(',')
done = set()
p2 = 1
while len(done) < len(my_ticket):
    for field in fields:
        candidates = set.intersection(*fields[field]) - done
        if len(candidates) == 1:
            done.update(candidates)
            p2 *= int(my_ticket[field]) if candidates.pop() < 6 else 1

print("Part 1:", p1)
print("Part 2:", p2)
