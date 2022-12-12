with open('input.txt', 'r') as f:
    lines = [x.split(',') for x in f.read().strip().split('\n')]

p1 = p2 = 0
for line in lines:
    e1 = list(map(int, line[0].split('-')))
    e2 = list(map(int, line[1].split('-')))

    if e1[0] <= e2[0] <= e2[1] <= e1[1] or e2[0] <= e1[0] <= e1[1] <= e2[1]:
        p1 += 1

    if e1[0] <= e2[0] <= e1[1] or e2[0] <= e1[0] <= e2[1]:
        p2 += 1

print(p1)
print(p2)
