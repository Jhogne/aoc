import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

pts = 0
sc = [1]*len(lines)
for i,l in enumerate(lines):
    nums = re.findall(r"\d+", l)
    win = set(nums[1:11])
    mine = set(nums[11:])
    mywins = len(win & mine)

    if mywins == 0:
        continue

    pts += pow(2, mywins-1)

    for j in range(i+1,i+mywins+1):
        sc[j] += sc[i]

print(pts)
print(sum(sc))
