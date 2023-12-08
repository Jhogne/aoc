import math
import sys
import re

sys.setrecursionlimit(100000)

with open('real.in', 'r') as f:
    insts, nodes = f.read().strip().split('\n\n')

network = {}
for n in nodes.splitlines():
    f, l, r = re.findall(r"[A-Z0-9]{3}", n)
    network[f] = (l, r)

def find(curr, steps, istarget):
    if istarget(curr):
        return steps
    inst = insts[steps % len(insts)]
    return find(network[curr]["LR".index(inst)], steps + 1, istarget)

def zzz(node):
    return node == "ZZZ"

def anyz(node):
    return node.endswith("Z")

def p1():
    return find("AAA", 0, zzz)

def p2():
    starts = [x for x in network if x.endswith("A")]
    to_zs = [find(s,0,anyz) for s in starts]
    return math.lcm(*to_zs)

print(p1())
print(p2())
