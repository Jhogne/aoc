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
            outs.append(p1)
            if(len(outs) == 3):
                outputs.push(outs)
                outs = []
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

def print_game(blocks, walls, ball_pos, paddle_pos):
    print('ball:',ball_pos)
    print('paddle',paddle_pos)
    for y in range(25):
        for x in range(40):
            if (x,y) in blocks:
                print('█', end='')
            elif (x,y) in walls:
                print('#', end='')
            elif (x,y) == ball_pos: 
                print('.', end='')
            elif (x,y) == paddle_pos:
                print('¨',end='')
            else: 
                print(' ', end='')
        print('')


def run_game(part2):
    code = numbers.copy()
    if part2:
        code[0] = 2
    t = threading.Thread(target = run, args = (code, inputs, outputs))
    t.start()

    blocks = []
    walls = []
    ball_pos = (-1,-1)
    paddle_pos = (-1,-1)
    while True:
        tile = outputs.pop()
        pos = (tile[0],tile[1])
        tile_id = tile[2]
        if tile_id == 1:
            walls.append(pos)
        elif tile_id== 2:
            blocks.append(pos)
        elif tile_id == 0 and pos in blocks:
            blocks.remove(pos)
        elif tile_id == 3:
            paddle_pos = pos
        elif tile_id == 4:
            ball_pos = pos
            #print_game(blocks, walls, ball_pos, paddle_pos)
            #move = input('Move: ')
        
            # if move == '1' or move == '-1':
            #     inputs.push(int(move))
            # else:
            #    inputs.push(0)

            if ball_pos[0] > paddle_pos[0]:
                move = 1
            elif ball_pos[0] < paddle_pos[0]:
                move = -1
            else:
                move = 0
            inputs.push(move)
            
        elif pos == (-1,0):
            if(len(blocks) == 0):
                return(tile[2])
        if not part2:
            if not t.is_alive():
                return len(blocks)

print('Part 1: ', run_game(False))
inputs = SyncStack()
outputs = SyncStack()
print('Part 2: ', run_game(True))
