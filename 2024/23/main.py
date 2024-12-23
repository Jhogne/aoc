from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

comps = defaultdict(lambda: [])

for l in lines:
    frm, to = l.split('-')
    comps[frm].append(to)
    comps[to].append(frm)

def bfs(start, end):
    q = [(start, [])]
    while q:
        pos, path = q.pop(0)
        if path and pos == end:
            yield path
        if len(path) > 2:
            continue
        for n in comps[pos]:
            if n not in path:
                q.append((n, path + [n]))

def interconnected(start):
    q = [(start)]
    found = [start]
    while q:
        pos = q.pop(0)
        for n in comps[pos]:
            if all(p in comps[n] for p in found):
                found.append(n)
                q.append(n)
    return found

threes, largest = set(), set()
for comp in comps:
    for cycle in bfs(comp, comp):
        if frozenset(cycle) in threes:
            continue

        if len(cycle) == 3 and any(c[0] == "t" for c in cycle):
            threes.add(frozenset(cycle))

    ic = interconnected(comp)
    if len(ic) > len(largest):
        largest = ic

print(len(threes))
print(','.join(sorted(largest)))
