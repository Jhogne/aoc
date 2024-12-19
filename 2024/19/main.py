from functools import cache

with open('real.in', 'r') as f:
    lines = f.read().strip().split("\n\n")

available = set(lines[0].split(', '))
lengths = [len(x) for x in available]
shortest,longest = min(lengths),max(lengths)

@cache
def legal(pattern):
    if pattern == "":
        return 1 
    poss = []
    for i in range(shortest,min(longest, len(pattern))+1):
        if pattern[:i] in available:
            poss.append(legal(pattern[i:]))
    return sum(poss)

p1 = p2 = 0
for l in lines[1].splitlines():
    tot = legal(l)
    if tot:
        p1 += 1
    p2 += tot

print(p1)
print(p2)
