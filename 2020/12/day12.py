from math import cos, sin, radians

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()

def rotate(x, y, angle):
    x_prim = x * cos(radians(angle)) - y * sin(radians(angle))
    y_prim = y * cos(radians(angle)) + x * sin(radians(angle))
    return round(x_prim), round(y_prim)

(x1,y1) = (0,0)
(dx,dy) = (1,0)
for ins in instructions:
    op = ins[0]
    amt = int(ins[1:])
    if op == 'L':
        dx, dy = rotate(dx, dy, amt)
    elif op == 'R':
        dx, dy = rotate(dx, dy, 360 - amt)
    elif op == 'F':
        x1 += amt * dx
        y1 += amt * dy
    elif op == 'N':
        y1 = y1 + amt
    elif op == 'S':
        y1 = y1 - amt
    elif op == 'E':
        x1 = x1 + amt
    elif op == 'W':
        x1 = x1 - amt

(x2,y2) = (0,0)
(wpx,wpy) = (10,1)
for ins in instructions:
    op = ins[0]
    amt = int(ins[1:])
    if op == 'L':
        wpx, wpy = rotate(wpx, wpy, amt)
    elif op == 'R':
        wpx, wpy = rotate(wpx, wpy, 360 - amt)
    elif op == 'F':
        x2 += amt * wpx
        y2 += amt * wpy
    elif op == 'N':
        wpy = wpy + amt
    elif op == 'S':
        wpy = wpy - amt
    elif op == 'E':
        wpx = wpx + amt
    elif op == 'W':
        wpx = wpx - amt

print("Part 1:", abs(x1) + abs(y1))
print("Part 2:", abs(x2) + abs(y2))
