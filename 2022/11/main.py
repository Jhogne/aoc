import re 
import math
import copy

with open('input.txt', 'r') as f:
    lines = [l.splitlines() for l in f.read().split('\n\n')]

nums = lambda s: [int(x) for x in re.findall(r"\d+", s)]

monkeys = []
for _,a,b,c,d,e in lines:
    items = nums(a)
    operation = b[19:]
    divider = nums(c)[0]
    valid = nums(d)[0]
    invalid = nums(e)[0]

    monkeys.append([items, operation, divider, valid, invalid, 0])

def monkey_inspect(n, monkeys, limit_worry):
    for _ in range(n):
        for (m, [itms, op, div, val, inval, _]) in enumerate(monkeys):
            for old in itms:
                worry = limit_worry(eval(op))
                to = val if worry % div == 0 else inval

                monkeys[to][0].append(worry)
                monkeys[m][-1] += 1
        
            monkeys[m][0].clear()
     
    inspected = sorted([x[-1] for x in monkeys])
    return inspected[-1] * inspected[-2]

lcm = math.prod([m[2] for m in monkeys])
print(monkey_inspect(20, copy.deepcopy(monkeys), lambda x: x // 3))
print(monkey_inspect(10000, monkeys, lambda x: x % lcm))
