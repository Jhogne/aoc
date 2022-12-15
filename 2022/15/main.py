import re
import math

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

#lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
#Sensor at x=9, y=16: closest beacon is at x=10, y=16
#Sensor at x=13, y=2: closest beacon is at x=15, y=3
#Sensor at x=12, y=14: closest beacon is at x=10, y=16
#Sensor at x=10, y=20: closest beacon is at x=10, y=16
#Sensor at x=14, y=17: closest beacon is at x=10, y=16
#Sensor at x=8, y=7: closest beacon is at x=2, y=10
#Sensor at x=2, y=0: closest beacon is at x=2, y=10
#Sensor at x=0, y=11: closest beacon is at x=2, y=10
#Sensor at x=20, y=14: closest beacon is at x=25, y=17
#Sensor at x=17, y=20: closest beacon is at x=21, y=22
#Sensor at x=16, y=7: closest beacon is at x=15, y=3
#Sensor at x=14, y=3: closest beacon is at x=15, y=3
#Sensor at x=20, y=1: closest beacon is at x=15, y=3
#""".splitlines()

Y = 2000000
MAXPOS = 4000000#20

beacons = set()
sensors = set()
leftmost = math.inf
rightmost = -math.inf
maxpoints = set()
for line in lines:
    sx, sy, bx, by = map(int, re.findall("-?\d+", line))

    dist = abs(bx - sx) + abs(by - sy)
    sensors.add((sx, sy, dist))
    beacons.add((bx, by))
    
    if sx - dist < leftmost:
        leftmost = sx - dist

    if sx + dist > rightmost:
        rightmost = sx + dist

    maxpoints.add((sx + dist, sx - dist, sy + dist, sy - dist))


#p1 = 0
#for x in range(leftmost, rightmost+1):
#    for (sx, sy, dist) in sensors:
#        if (x, Y) not in beacons and abs(sx - x) + abs(sy - Y) <= dist:
#            p1 += 1
#            break
#
#print(p1)


for x in range(0, MAXPOS):
    invalid = False
    for r, l, _, _ in maxpoints:
        if l <= x <= r:
            invalid = True
            break
    if not invalid:
        print(x)
        break



