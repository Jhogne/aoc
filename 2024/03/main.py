import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

p1, p2 = 0, 0
active = True
for l in lines:
    muls = re.findall(r"mul\((\d+),(\d+)\)", l)
    ops = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don)'t\(\)", l)
    for a,b in muls:
        p1 += int(a) * int(b)
    for a,b,start,stop in ops:
        if stop:
            active = False
        elif start:
            active = True
        elif active:
            p2 += int(a) * int(b)

print(p1)
print(p2)
