from math import prod

with open('input.txt', 'r') as f:
    lines = f.read().splitlines() 

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees = [0] * 5

for i,(dx,dy) in enumerate(slopes):
    x = 0
    for l in lines[::dy]:
        if l[x % len(l)] == '#':
            trees[i] += 1
        x += dx

print("Part 1:",trees[1])
print("Part 2:",prod(trees))