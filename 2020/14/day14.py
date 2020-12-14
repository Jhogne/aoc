import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def apply_mask(mask, num, target):
    masked = ''
    for m,n in zip(mask,num):
        if m == target:
            masked += n
        else:
            masked += m
    return masked

def p1(mem, mask, idx, val):
    val = "{:036b}".format(int(val))
    mem[idx] = int(apply_mask(mask,val,'X'), 2)

def replace_x(string):
    if not 'X' in string:
        return [string]
    else:
        return replace_x(string.replace('X','1',1)) + \
               replace_x(string.replace('X','0',1))

def p2(mem, mask, idx, val):
    idx = "{:036b}".format(int(idx))
    for i in replace_x(apply_mask(mask,idx,'0')):
        mem[i] = int(val)

def solve(update_memory):
    mask = ''
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split('= ')[1]
        else:
            idx,val = re.search(r'\[(\d+)\] = (\d+)', line).groups()
            update_memory(mem, mask, idx, val)
    return sum(mem.values())

print("Part 1:",solve(p1))
print("Part 2:",solve(p2))
