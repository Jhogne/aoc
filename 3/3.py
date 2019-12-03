import re

with open('3.txt', 'r') as f:
    input = f.read().splitlines()
input1 = input[0].split(',')
input2 = input[1].split(',')

l = map(lambda x: re.split('(\d+)', x), input1)
l2 = map(lambda x: re.split('(\d+)', x), input2)

list1 = []
list2 = []
for i in l:
    list1.append(tuple([i[0], int(i[1])]))
for i in l2:
    list2.append(tuple([i[0], int(i[1])]))

class line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def intersects(self,line2):
        left = self if self.start[0] < line2.start[0] else line2
        right = self if left != self else line2
        bottom = self if self.start[1] < line2.start[1] else line2
        top = self if bottom != self else line2

        return left.end[0] > right.end[0] and bottom.end[1] > top.end[1]
    
    def steps(self):
        if(self.start[0] == self.end[0]):
            return abs(self.start[1] - self.end[1])
        else:
            return abs(self.start[0] - self.end[0])
            
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

moves1 = [line([0,0],[0,0])]
moves2 = [line([0,0],[0,0])]

for i,j in zip(list1, list2):
    move(moves1,*i)
    move(moves2,*j)

intersectsions = []
for i in moves1:
    for j in moves2:
        if(i.intersects(j)):
            if i.start[0] == i.end[0]:
                intersectsions.append([i.start[0], j.start[1]])
            else:
                intersectsions.append([j.start[0], i.start[1]])
sum = 0

sums = []
for i in intersectsions:
    sums.append(0)

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

print(min(sums))
