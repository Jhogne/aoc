import re

def parse(s):
    split = re.split('(\d+)',s)
    return tuple([split[0], int(split[1])])

with open('input.txt', 'r') as f:
        input = f.read().splitlines()
input[0] = map(parse, input[0].split(','))
input[1] = map(parse, input[1].split(','))

class line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def steps(self):
        if(self.start[0] == self.end[0]):
            return abs(self.start[1] - self.end[1])
        else:
            return abs(self.start[0] - self.end[0])
            
    def intersects(self,line2):
        left = self if self.start[0] < line2.start[0] else line2
        right = self if left != self else line2
        bottom = self if self.start[1] < line2.start[1] else line2
        top = self if bottom != self else line2

        return left.end[0] > right.end[0] and bottom.end[1] > top.end[1]
    
    def lengthToPoint(self, point):
        minx = min(self.start[0], self.end[0])
        miny = min(self.start[1], self.end[1])
        maxx = max(self.start[0], self.end[0])
        maxy = max(self.start[1], self.end[1])
        if(self.start[0] == point[0] or self.start[1] == point[1]):
            if((point[0] < maxx and point[0] > minx) or (point[1] < maxy and point[1] > miny)):
                return abs(point[1] - self.start[1]) + abs(point[0] - self.start[0])
        return -1

def move(moves, dir, amount):
    last = moves[-1]
    if dir == 'R':
        moves.append(line(last.end, [last.end[0] + amount, last.end[1]]))
    elif dir == 'L':
        moves.append(line(last.end, [last.end[0] - amount, last.end[1]]))
    elif dir == 'U':
        moves.append(line(last.end, [last.end[0], last.end[1] + amount]))
    elif dir == 'D':
        moves.append(line(last.end, [last.end[0], last.end[1] - amount]))
    else:
        print('WTF dude')

def findIntersections(lines1, lines2):
    intersectsions = []
    for i in lines1:
        for j in lines2:
            if(i.intersects(j)):
                if i.start[0] == i.end[0]:
                    intersectsions.append([i.start[0], j.start[1]])
                else:
                    intersectsions.append([j.start[0], i.start[1]])
    return intersectsions

moves1 = [line([0,0],[0,0])]
moves2 = [line([0,0],[0,0])]

for i,j in zip(input[0], input[1]):
    move(moves1,*i)
    move(moves2,*j)

intersectsions = findIntersections(moves1, moves2)

# Part 1
minpath = abs(intersectsions[0][0]) + abs(intersectsions[0][1])
for i in intersectsions:
    cost = abs(i[0]) + abs(i[1])
    if cost < minpath: 
        minpath = cost
print("Part 1: " + str(minpath))

# Part 2
sums = [0]*len(intersectsions)

index = 0
for i in intersectsions:
    for p in moves1:
        if(p.lengthToPoint(i) == -1):         
            sums[index] += p.steps()
        else: 
            sums[index] += p.lengthToPoint(i)
            break
    for p in moves2:
        if(p.lengthToPoint(i) == -1):         
            sums[index] += p.steps()
        else: 
            sums[index] += p.lengthToPoint(i)
            break
    index += 1

print("Part 2: " + str(min(sums)))