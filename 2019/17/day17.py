import threading
import random
from collections import deque
import queue

class SyncStack:
    def __init__(self):
        self.stack = queue.Queue()
        self.semaphore = threading.Semaphore(0)
    def pop(self):
        val = self.stack.get()
        return val
    """ 
    def push(self, val):
        self.stack += (val)
        self.semaphore.release()
    """   
    def push(self, val):
        self.stack.put(val)
    def print(self):
        print(self.stack)
    def empty(self):
        return self.stack.empty()

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
"""     if mode == 2:
        idx += rel_base

    if isinstance(val, int):
        limit = idx
    else:
        limit = idx + len(val)
    if limit >= len(code):
        write_to = extra_memory
    else:
        write_to = code
    if isinstance(val, int):
        write_to[idx] = val
    else:
        write_to[idx:idx+len(val)] = val
 """
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

def handle_output():
    scaffolds = []
    coord = (0,0)
    start = (-1,-1)
    dust = -1
    while True:
        if coord == (51,56):
            coord = (0,0)
        out = outputs.pop()
        if out == 35:
            if not coord in scaffolds:
                scaffolds.append(coord)
            coord = (coord[0]+1,coord[1])
        elif out == 46:
            coord = (coord[0]+1,coord[1])
        elif out == 10:
            coord = (0,coord[1]+1)
        else:
            dust = out
            start = coord
            coord = (coord[0]+1,coord[1])
        if not t.is_alive() and outputs.empty():
            param = 0
            for i in list(set(scaffolds)):
                if (i[0]+1,i[1]) in scaffolds and (i[0]-1,i[1]) in scaffolds and (i[0],i[1]+1) in scaffolds and (i[0],i[1]-1) in scaffolds:
                    param += i[0]*i[1]
            break
    return(dust,param)         # For findind answer
    #return (start, scaffolds) # For finding dequence

code = numbers.copy()
t = threading.Thread(target = run, args = (code, inputs, outputs))
t.start()

start, x= handle_output()
# <1> 
# Find sequence of moves. Remember to use correct return in  handle_output()
# To use this part remove comments and add comments around block <2>
"""
clockwise = [(0,-1), (1,0), (0,1), (-1,0)]
def turn_right(direction):
    return clockwise[(clockwise.index(direction)+1) % 4]
def turn_left(direction):
    return clockwise[(clockwise.index(direction)-1) % 4]
curr = start
amt = 0
direction = (1,0)
hand = 'r'
seq = []
while True:
    if (curr[0]+direction[0],curr[1]+direction[1]) in x:
        amt += 1
        curr = (curr[0]+direction[0], curr[1]+direction[1])
    else:
        seq.append((hand,amt))
        amt = 0
        right = turn_right(direction)
        left = turn_left(direction)
        if (curr[0]+right[0],curr[1]+right[1]) in x:
            direction = turn_right(direction)
            hand = 'r'
        elif (curr[0]+left[0],curr[1]+left[1]) in x:
            direction = turn_left(direction)
            hand = 'l'
        else:
            break
print(seq) 
# </1>
"""
# <2>
# Find the answer when sequence is known. Remember to use correct return in  handle_output()
# To use this part remove comments and add comments around block <1>
numbers[0] = 2
t = threading.Thread(target = run, args = (numbers, inputs, outputs))
t.start()

def push_string(str):
    for i in str:
        inputs.push(ord(i))
    inputs.push(10)

# The sequence found by hand and the commented code above
push_string('C,B,C,A,B,A,B,A,C,A') # Main
push_string('R,12,L,10,L,6,R,10')  # A
push_string('L,8,L,6,L,10')        # B
push_string('R,12,L,6,R,12')       # C
push_string('n')                   # Live feed?

dust,_ = handle_output()

print('Part 1:',x)
print('Part 2:',dust)
# </2>
