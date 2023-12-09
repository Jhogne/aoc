from functools import reduce

def ints(line):
    return [int(x) for x in line.split()]

with open('real.in', 'r') as f:
    lines = [ints(l) for l in f.read().splitlines()]

def diffs(ns):
    res = []
    for i in range(1,len(ns)):
        res.append(ns[i]-ns[i-1])
    return res

p1 = p2 = 0
for ns in lines:
    rs, ls = [], []
    
    while any([n != 0 for n in ns]):
        rs.append(ns[-1])
        ls.append(ns[0])
        ns = diffs(ns)

    p1 += sum(rs)
    p2 += reduce(lambda a,b: b - a, reversed(ls), 0)

print(p1)
print(p2)
