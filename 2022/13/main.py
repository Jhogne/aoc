from ast import literal_eval
from functools import cmp_to_key

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

def cmp(left, right):
    for l, r in zip(left, right):
        match l, r:
            case int(), int() if r > l: return -1
            case int(), int() if r < l: return 1
            case int(), list(): return cmp([l], r)
            case list(), int(): return cmp(l, [r])
            case list(), list(): return cmp(l, r)
    return -1 if len(left) <= len(right) else 1

p1 = 0
divider1, divider2 = [[2]], [[6]]
packets = [divider1, divider2]
for i, pair in enumerate(lines, 1):
    left, right = map(literal_eval, pair.splitlines())
    if cmp(left, right) == -1:
        p1 += i
    packets += [left, right]

packets = sorted(packets, key=cmp_to_key(cmp))

print(p1)
print((1 + packets.index(divider1)) * (1+packets.index(divider2)))
