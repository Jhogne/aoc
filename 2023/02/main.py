import re
import math
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def parse(lines):
    for l in lines:
        g = int(re.findall(r"Game (\d+)", l)[0]);
        bs = re.findall(r"(\d+) (blue)", l)
        rs = re.findall(r"(\d+) (red)", l)
        gs = re.findall(r"(\d+) (green)", l)
        yield (g, bs + rs + gs)

def p1():
    colors = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for g, cubes in parse(lines):
        if all([colors[col] >= int(n) for n, col in cubes]):
            total += g
    return total

def p2():
    total = 0
    for _, rounds in parse(lines):
        colors = defaultdict(lambda: 0)
        for n, col in rounds:
            colors[col] = max(colors[col], int(n))
    
        total += math.prod(colors.values())
    return total

print(p1())
print(p2())
