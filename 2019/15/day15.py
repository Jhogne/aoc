import threading
import random
from collections import deque

class SyncStack:
    def __init__(self):
        self.stack = []
        self.semaphore = threading.Semaphore(0)
    def pop(self):
        self.semaphore.acquire()
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val
    def push(self, val):
        self.stack.append(val)
        self.semaphore.release()
    def print(self):
        print(self.stack)

with open('input.txt', 'r') as f:
    string = f.read().split(',')
numbers = [int(x) for x in string]

lengths = [5,5,3,3,4,4,5,5,3]
extra_memory = {}
inputs = SyncStack()
outputs = SyncStack()

def get_value(val, code):
    if val >= len(code):
        if val in extra_memory:
            return extra_memory[val]
        else:
            extra_memory[val] = 0
            return 0
    else:
        return code[val]

def write_value(val, idx, code, mode, rel_base):
    if mode == 2:
        idx += rel_base
    if len(code) <= idx:
        extra_memory[idx] = val
    else:
        code[idx] = val
    
def get_modes(operation):
    op = operation % 100
    for i in range(2, lengths[op-1]):
        mode = operation // 10**i % 10
        yield mode

def get_params(code, pc, rel_base):
    for offset,m in enumerate(get_modes(code[pc]), start=1):
        val = code[pc+offset]
        if offset != 3:
            if m == 0:
                val = get_value(code[pc+offset], code)
            elif m == 2:
                val = get_value(rel_base + code[pc+offset], code)
        yield val

def run(code, inputs, outputs):
    rel_base = 0
    pc = 0
    outs = []
    while code[pc] != 99:
        opmodes = str(code[pc])[::-1]
        op = code[pc] % 10        
        params = get_params(code, pc, rel_base)
        modes = get_modes(code[pc])
        try:
            p1 = next(params)
            p2 = next(params)
            out = next(params) 
        except StopIteration as e:
            pass
        try: 
            m1 = next(modes)
            m2 = next(modes)
            m3 = next(modes)
        except StopIteration as e:
            pass

        if op == 1:
            write_value(p1 + p2, out, code, m3, rel_base)
            pc += 4
        elif op == 2:
            write_value(p1 * p2, out, code, m3, rel_base)
            pc += 4            
        elif op == 3:
            write_value(inputs.pop(), code[pc+1], code, m1, rel_base)
            pc += 2
        elif op == 4:
            outputs.push(p1)
            pc += 2
        elif op == 5:
            pc = p2 if p1 != 0 else pc + 3
        elif op == 6:
            pc = p2 if p1 == 0 else pc + 3
        elif op == 7:
            less = 1 if p1 < p2 else 0
            write_value(less, out, code, m3, rel_base)
            pc += 4
        elif op == 8:
            equals = 1 if p1 == p2 else 0
            write_value(equals, out, code, m3, rel_base)
            pc += 4
        elif op == 9:
            rel_base += p1
            pc += 2
        else:
            break

directions = [1,3,2,4]
coords = {1:(0,-1),2:(0,1),3:(-1,0),4:(1,0)}
def get_pos(droid,move_dir):
    return tuple(map(sum, zip(droid, coords[move_dir])))

def next_dir(droid,walls, move_dir):
    idx = (directions.index(move_dir) - 1) % 4
    for _ in range(len(directions)):
        if not get_pos(droid,directions[idx]) in walls:
            return directions[idx]
        idx = (idx + 1) % 4

def find_paths(walls, droid_pos):
    amt = 0
    for i in range(1,5):
        inputs.push(i)
        out = outputs.pop()
        if out == 0:
            walls.append((get_pos(droid_pos, i)))
        else:
            amt += 1
            inputs.push(directions[(directions.index(i) + 2) % 4])
            outputs.pop()
    return amt

def find_adjacent(pos, walkable):
    res = []
    for i in directions:
        if get_pos(pos, i) in walkable:
            res.append(get_pos(pos,i))
    return res

def fill_o2(path, pos, o2, time):
    if not pos in o2:
        adjacent = find_adjacent(pos, path)
        o = o2 + [pos]
        lengths = []
        for i in adjacent:
            lengths.append(fill_o2(path, i, o, time + 1))
        return max(lengths)
    return time

def run_droid():
    t = threading.Thread(target = run, args = (numbers, inputs, outputs))
    t.start()

    path = {}
    walls = []
    droid_pos = (0,0)
    start_pos = droid_pos
    o2_system = (-1,-1)
    move_dir = 1
    visited = [(25, 25)]
    while True:        
        move_dir = next_dir(droid_pos, walls, move_dir)
        inputs.push(move_dir)
        status = outputs.pop()

        if status == 0:
            walls.append(get_pos(droid_pos, move_dir))
        else:
            old_pos = droid_pos
            droid_pos = get_pos(droid_pos, move_dir)

            if find_paths(walls,droid_pos) > 2 and droid_pos in visited: 
                path[droid_pos] = path[droid_pos]
            else:
                visited.append(droid_pos)
                path[droid_pos] = old_pos

        if status == 2:
            o2_system = droid_pos
            length = 0
            curr = o2_system 
            while curr != start_pos:
                curr = path[curr]
                length += 1
            print('Part 1:',length)     

        if o2_system != (-1,-1) and droid_pos == start_pos:
            print('Part 2:',fill_o2(visited,o2_system, [], 0)-1)
            return
     
run_droid()
