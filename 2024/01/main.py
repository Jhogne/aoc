with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

left, right = [], []
for l in lines:
    a, b = l.split()
    left.append(int(a))
    right.append(int(b))

p1 = 0
for a,b in zip(sorted(left), sorted(right)):
    p1 += abs(a - b)
print(p1)

p2 = 0
for n in left:
    p2 += n * right.count(n)
print(p2)
