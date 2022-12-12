from itertools import takewhile

with open('input.txt', 'r') as f:
    forest = f.read().splitlines()

forestt = list(zip(*forest))
visible = lambda l: min(1 + len(list(takewhile(smaller, l))), len(l))
p1 = p2 = 0
for y in range(0,len(forest)):
    for x in range(0,len(forest)):
        bx, ax = forest[y][:x], forest[y][x+1:]
        by, ay = forestt[x][:y], forestt[x][y+1:]

        for line in [bx, ax, by, ay]:
            if all(forest[y][x] > tree for tree in line):
                p1 += 1
                break

        smaller = lambda t: t < forest[y][x]

        l, r = visible(bx[::-1]), visible(ax)
        u, d = visible(by[::-1]), visible(ay)
        p2 = max(l * r * u * d, p2)

print(p1)
print(p2)
