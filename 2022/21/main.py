with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

monkeys = {name: inst for name,inst in map(lambda l: l.split(": "), lines)}

def to_expr(monkey, p2=True):
    inst = monkeys[monkey]
    if monkey == "humn" and p2:
        return "x"

    if inst.isdigit():
        return monkeys[monkey]

    lhs, op, rhs = inst.split()
    lhs, rhs = to_expr(lhs, p2), to_expr(rhs, p2)

    if monkey == "root" and p2:
        return lhs, rhs

    return "(" + lhs + op + rhs + ")"
    

p1 = int(eval(to_expr("root", False)))

lhs, rhs = to_expr("root", True)
rhs = eval(rhs)

p2, lo, hi = 1, 0, 1
while (res := eval(lhs.replace('x', str(p2)))) != rhs:
    if res > rhs:
        lo, p2 = p2, p2 * 2
    elif res < rhs:
        hi, p2 = p2, (lo + hi) // 2

print(p1)
print(p2)

