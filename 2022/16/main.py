import re
from functools import lru_cache
from itertools import combinations

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

tunnels = {}
weights = {}
for line in lines:
    valves = re.findall(r"[A-Z][A-Z]", line)
    rate = int(re.search(r"\d+", line)[0])
    tunnels[valves[0]] = valves[1:]
    weights[valves[0]] = rate

cache = {}
@lru_cache(maxsize=10000000000)
def p1(curr, minutes, closed):
    if minutes < 2:
        return 0

    if not closed:
        return 0

    values = []
    if weights[curr] > 0 and curr in closed:
        for neighbour in tunnels[curr]:
            ifopen = p1(neighbour, minutes-2, closed - frozenset([curr]))
            values.append(ifopen + weights[curr] * (minutes-1))
    for neighbour in tunnels[curr]:
        values.append(p1(neighbour, minutes-1, closed))

    res = max(values)
    return res

relevant = frozenset([key for key in weights.keys() if weights[key] != 0])

print(p1('AA', 30, relevant))

best = 0
for i in range(len(relevant)):
    print(i)
    for me in combinations(relevant, i):
        me = frozenset(me)
        tot = p1('AA', 26, me)
        tot += p1('AA', 26, relevant - me)

        best = max(tot, best)

print(best)
