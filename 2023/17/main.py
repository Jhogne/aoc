import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict
from queue import PriorityQueue

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()


def turn_right(dy,dx):
    match dy,dx:
        case 0,1: return 1,0
        case 1,0: return 0,-1
        case 0,-1: return -1,0
        case -1,0: return 0,1

def turn_left(dy,dx):
    match dy,dx:
        case 0,1: return -1,0
        case 1,0: return 0,1
        case 0,-1: return 1,0
        case -1,0: return 0,-1

N = (-1,0)
S = (1,0)
E = (0,1)
W = (0,-1)
def p1():
    q = PriorityQueue() 
    q.put((-int(lines[0][0]), (0,-1,0,1,3,[])))

    seen = set()
    while not q.empty():
        loss,(y,x,dy,dx,straight,path) = q.get()
    
        if y == len(lines)-1 and x == len(lines[0])-1:
            print(loss)
            break
    
        if (y,x,dy,dx,straight) in seen:
            continue
    
        seen.add((y,x,dy,dx,straight))
    
        left_dy,left_dx = turn_left(dy,dx)
        left_y, left_x = y+left_dy, x+left_dx
        if 0 <= left_y < len(lines) and 0 <= left_x < len(lines[0]):
            left_loss = loss + int(lines[left_y][left_x])
            left_path = path[:]
            left_path.append((left_y,left_x,"l",left_loss))
            q.put((left_loss,(left_y,left_x,left_dy,left_dx,2,left_path)))
    
        right_dy,right_dx = turn_right(dy,dx)
        right_y, right_x = y+right_dy, x+right_dx
        if 0 <= right_y < len(lines) and 0 <= right_x < len(lines[0]):
            right_loss = loss + int(lines[right_y][right_x])
            right_path = path[:]
            right_path.append((right_y,right_x,"r",right_loss))
            q.put((right_loss,(right_y,right_x,right_dy,right_dx,2,right_path)))
    
        if straight > 0:
            straight_y, straight_x = y+dy, x+dx
            if 0 <= straight_y < len(lines) and 0 <= straight_x < len(lines[0]):
                straight_path = path[:]
                straight_loss = loss + int(lines[straight_y][straight_x])
                straight_path.append((straight_y,straight_x,"s",straight_loss))
                q.put((straight_loss,(straight_y,straight_x,dy,dx,straight-1,straight_path)))

def p2():
    q = PriorityQueue() 
    q.put((-int(lines[0][0]), (0,-1,0,1,-1,[])))

    seen = set()
    while not q.empty():
        loss,(y,x,dy,dx,straight,path) = q.get()
    
        if y == len(lines)-1 and x == len(lines[0])-1 and straight >= 4:
            print(loss)
            #print(path)
            break
    
        if (y,x,dy,dx,straight) in seen:
            continue
    
        seen.add((y,x,dy,dx,straight))

        if straight < 10:
            straight_y, straight_x = y+dy, x+dx
            if 0 <= straight_y < len(lines) and 0 <= straight_x < len(lines[0]):
                straight_path = path[:]
                straight_loss = loss + int(lines[straight_y][straight_x])
                straight_path.append((straight_y,straight_x,"s",straight_loss))
                q.put((straight_loss,(straight_y,straight_x,dy,dx,straight+1,straight_path)))
            if straight < 4:
                continue

    
        left_dy,left_dx = turn_left(dy,dx)
        left_y, left_x = y+left_dy, x+left_dx
        if 0 <= left_y < len(lines) and 0 <= left_x < len(lines[0]):
            left_loss = loss + int(lines[left_y][left_x])
            left_path = path[:]
            left_path.append((left_y,left_x,"l",left_loss))
            q.put((left_loss,(left_y,left_x,left_dy,left_dx,1,left_path)))
    
        right_dy,right_dx = turn_right(dy,dx)
        right_y, right_x = y+right_dy, x+right_dx
        if 0 <= right_y < len(lines) and 0 <= right_x < len(lines[0]):
            right_loss = loss + int(lines[right_y][right_x])
            right_path = path[:]
            right_path.append((right_y,right_x,"r",right_loss))
            q.put((right_loss,(right_y,right_x,right_dy,right_dx,1,right_path)))
    

#p1()
p2()

ex ="""2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
"""

best_path = []
for y,l in enumerate(ex.splitlines()):
    for x,c in enumerate(l):
        if not c.isdigit():
            best_path.append((y,x))



