import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def wins(t, d):
    for i in range(t):
        if (t - i) * i > d:
            yield 1

def p1():
    times = [int(x) for x in re.findall(r"\d+", lines[0])]
    dists = [int(x) for x in re.findall(r"\d+", lines[1])]
    total = 1
    for t, d in zip(times, dists):
        total *= sum(wins(t, d))

    return total

def p2():
    time = int(''.join(re.findall(r"\d+", lines[0])))
    dist = int(''.join(re.findall(r"\d+", lines[1])))

    return sum(wins(time,dist))

print(p1())
print(p2())
