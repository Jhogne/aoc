from itertools import combinations

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

galaxies = set()
for i,l in enumerate(lines):
    for j,c in enumerate(l):
        if lines[i][j] == "#":
            galaxies.add((i,j))

empty_rows, empty_cols = [], []
for i in range(len(lines)):
    if all([c == "." for c in lines[i]]):
        empty_rows.append(i)

for i in range(len(lines[0])):
    if all ([l[i] == "." for l in lines]):
        empty_cols.append(i)

def dist_sums(inc):
    for (y,x), (y1,x1) in combinations(galaxies, 2):
        maxx, maxy, minx, miny = max(x,x1), max(y,y1), min(x,x1), min(y,y1)
        xinc = sum([1 for e in empty_cols if minx < e < maxx]) * inc
        yinc = sum([1 for e in empty_rows if miny < e < maxy]) * inc 
        yield (maxy - miny) + yinc + (maxx - minx) + xinc

print(sum(dist_sums(1)))
print(sum(dist_sums(1000000-1)))
