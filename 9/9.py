with open('9.txt', 'r') as f:
    string = f.read().split(',')
numbers = [int(x) for x in string]

lengths = [5,5,3,3,4,4,5,5,3]
extra_memory = {}

def get_value(val, code):
    if val > len(code):
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
    if len(code) < idx:
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

def run(code):
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
            write_value(int(input("Enter value: ")), code[pc+1], code, m1, rel_base)
            pc += 2
        elif op == 4:
            print(p1)
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
run(numbers)
