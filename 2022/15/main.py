import re
import math

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

Y = 2000000
MAXPOS = 4000000

beacons, sensors = set(), set()
leftmost, rightmost = math.inf, -math.inf
for line in lines:
    sx, sy, bx, by = map(int, re.findall("-?\d+", line))

    dist = abs(bx - sx) + abs(by - sy)
    sensors.add((sx, sy, dist))
    beacons.add((bx, by))
    
    if sx - dist < leftmost:
        leftmost = sx - dist

    if sx + dist > rightmost:
        rightmost = sx + dist


p1 = 0
for x in range(leftmost, rightmost+1):
    for (sx, sy, dist) in sensors:
        if (x, Y) not in beacons and abs(sx - x) + abs(sy - Y) <= dist:
            p1 += 1
            break

print(p1)

def distance_from(x, y, dist):
    currx, curry = x, y+dist
    dx, dy = 1, -1

    pts = set()
    while (currx, curry) not in pts:
        pts.add((currx, curry))

        if currx == x + dist:
            dx, dy = -1, -1
        elif curry == y - dist:
            dx, dy = -1, 1
        elif currx == x - dist:
            dx, dy = 1, 1
        elif curry == y + dist:
            dx, dy = 1, -1

        currx, curry = currx + dx, curry + dy

    return pts

def check_candidate(x, y):
    done = True
    for (sx, sy, dist) in sensors:
        if abs(sx - x) + abs(sy - y) <= dist:
            done = False
            break

    if done:
        print(x, y)
        print(x * 4000000 + y)
        exit()

for (i, (sx, sy, dist)) in enumerate(sensors):
    print(i)
    for (x, y) in distance_from(sx, sy, dist+1):
        if 0 <= x <= MAXPOS and 0 <= y <= MAXPOS:
            check_candidate(x, y)

