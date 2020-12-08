from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def run(code):
    idx = 0
    acc = 0
    visited = defaultdict(bool)
    while idx < len(code):
        op, num = code[idx].split()
        num = int(num)
        if visited[idx]:
            break
        else:
            visited[idx] = True
        if op == "acc":
            acc += num
        elif op == "jmp":
            idx += num
            continue
        idx += 1
    return (idx >= len(code)), acc

def fix_corrupted():
    for i in range(len(lines)):
        code = lines[:]
        if('jmp' in code[i]):
            code[i] = code[i].replace('jmp', 'nop')
        elif('nop' in code[i]):
            code[i] = code[i].replace('nop', 'jmp')
        else:
            continue
        terminated, acc = run(code)
        if terminated:
            return acc

print("Part 1:", run(lines)[1])
print("Part 2:", fix_corrupted())
