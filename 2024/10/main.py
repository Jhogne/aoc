with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

starts = set()
poss = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        poss[(y,x)] = int(c)
        if c == '0':
            starts.add((y,x))

def neighbours(y,x):
    return [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

def find_score(start, all_paths=True):
    q = [start]
    seen = set()
    tot = 0
    while q:
        pos = q.pop(0)
        if pos in seen:
            continue
        if all_paths:
            seen.add(pos)
        if poss[pos] == 9:
            tot += 1

        for n in neighbours(*pos):
            if n in poss and poss[n] == poss[pos] + 1 and poss[n] not in seen:
                q.append(n)
    return tot

print(sum(find_score(pos) for pos in starts))
print(sum(find_score(pos, False) for pos in starts))
