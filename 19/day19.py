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

state = {}
state1 = {}
def run(code, inputs, outputs):
    original = code.copy()
    rel_base = 0
    pc = 0
    num_in = 0
    outs = []
    first = True
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
            # Instead of creating a new thread for every bot the computer resets after pushing the output
            pc = 0 
            rel_base = 0
            code = original[:] 
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

amt = 0
code = numbers.copy()
t = threading.Thread(target = run, args = (code, inputs, outputs))
t.start()

amt = 0
for i in range(50):
    for j in range(50):
        inputs.push(i)
        inputs.push(j)
        out = outputs.pop()
        if out == 1:
            amt += 1
print('Part 1:',amt)

x, y = 0,100
while True: 
    inputs.push(x)
    inputs.push(y)
    if outputs.pop() == 0:
        x += 1
        continue
    inputs.push(x+99)
    inputs.push(y-99)
    if outputs.pop() == 1:
        y -= 99
        break
    y += 1

print('Part 2:',x*10000+y)
