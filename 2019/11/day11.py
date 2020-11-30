import threading

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

def run_robot(whites):
    t = threading.Thread(target = run, args = (numbers.copy(), inputs, outputs))
    t.start()
    cur = (0,0)
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    next_i = 0
    painted = []
    while len(threading.enumerate()) > 1:
        color = 1 if cur in whites else 0
        inputs.push(color)
        paint = outputs.pop()

        direction = outputs.pop()
        if cur not in painted:
            painted.append(cur)

        if paint == 1 and not cur in whites:
            whites.append(cur)

        elif paint == 0 and cur in whites:
            whites.remove(cur)

        if direction == 1:
            next_i = 0 if next_i == 3 else next_i + 1
        else:
            next_i = 3 if next_i == 0 else next_i - 1
        cur = (cur[0] + dirs[next_i][0], cur[1] + dirs[next_i][1])
    return painted
print('Part 1: ', len(run_robot([])))

print('Part 2:')
whites = [(0,0)]
run_robot(whites)

for y in reversed(range(6)):
    for x in range(40):
        if((x,y-5) in whites):
            print('█', end='')
        else: 
            print(' ', end='')
    print('')