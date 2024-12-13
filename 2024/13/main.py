import re

with open('real.in', 'r') as f:
    lines = f.read().strip().split('\n\n')

buttons = []
for b in lines:
    button = []
    for l in b.splitlines():
        button.append([int(x) for x in re.findall(r'\d+', l)])
    buttons.append(button)

def intersect(a1,b1,c1,a2,b2,c2):
    x = (b1*c2-b2*c1)/(a1*b2-a2*b1)
    y = (c1*a2-c2*a1)/(a1*b2-a2*b1)
    return -x,-y

p1 = 0
def find_presses(p2=False):
    tot = 0
    for a,b,target in buttons:
        if p2:
            target[0] += 10000000000000
            target[1] += 10000000000000
        x,y = intersect(a[0],b[0],target[0],a[1],b[1],target[1])
        if x.is_integer() and y.is_integer():
            if p2 or x <= 100 and y <= 100:
                tot += 3 * x + y
    return int(tot)

print(find_presses())
print(find_presses(p2=True))
