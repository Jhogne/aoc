import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def apply_mask(mask,num,target):
    num_mask = list(mask)[::-1]
    for i, c in enumerate(num[::-1]):
        if num_mask[i] == target:
            num_mask[i] = c
    return num_mask[::-1]

def p1(mem,mask,idx,val):
    val = bin(int(val)).replace("0b","")
    idx = int(idx)
    new_val = ''.join(apply_mask(mask,val,'X')).replace('X','0')
    mem[idx] = int(new_val,2)

def replace_x(string):
    if not 'X' in string:
        yield string
    else:
        yield from replace_x(string.replace('X','1',1))
        yield from replace_x(string.replace('X','0',1))

def p2(mem,mask,idx,val):
    val = int(val)
    idx = bin(int(idx)).replace("0b","")
    idx_mask = apply_mask(mask,idx,'0')
    for i in replace_x(''.join(idx_mask)):
        mem[i] = val

def solve(update_memory):
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    mem = {}
    for line in lines:
        if 'mask' in line:
            mask = line.split('= ')[1]
        else:
            idx,val = re.findall(r'\[(\d+)\] = (\d+)', line)[0]
            update_memory(mem,mask,idx,val)
    return sum(mem.values())

print("Part 1:",solve(p1))
print("Part 2:",solve(p2))

