import re

with open('real.in', 'r') as f:
    lines = f.read().strip().split("\n\n")

registers = {}

for l in lines[0].splitlines():
    reg,val = l.split(": ")
    val = int(val)
    registers[reg] = val

ops = set()
creates = {}
maxz = "0"
for l in lines[1].splitlines():
    [(reg1,op,reg2,reg3)] = re.findall(r"(.+) (.+) (.+) -> (.+)", l)
    ops.add((reg1,op,reg2,reg3))
    creates[reg3] = (reg1, op, reg2)
    if reg3[0] == "z":
        if reg3[1:] > maxz:
            maxz=reg3[1:]

def reg2num(prefix):
    ns = [k for k in registers.keys() if k[0] == prefix]
    num = ""
    for n in sorted(ns, reverse=True):
        num += str(registers[n])
    return int(num, base=2)

def simulate():
    done = set()
    while len(registers) < (len(lines[1].splitlines()) + len(lines[0].splitlines())):
        for (reg1,op,reg2,reg3) in ops:
            if (reg1,op,reg2,reg3) in done:
                continue
            if reg1 in registers and reg2 in registers:
                if op == "AND":
                    registers[reg3] = registers[reg1] & registers[reg2]
                if op == "OR":
                    registers[reg3] = registers[reg1] | registers[reg2]
                if op == "XOR":
                    registers[reg3] = registers[reg1] ^ registers[reg2]
                done.add((reg1,op,reg2,reg3))

    return reg2num("z") 

def ones(n):
    w = 0
    while (n):
        w += 1
        n &= n - 1
    return w


def add_bits(in0, in1, in2):
    if in1 < in2:
        var1 = frozenset([in1, "XOR", in2])
    else:
        var1 = frozenset([in2, "XOR", in1])

    out1 = frozenset([var1, "XOR", in0])

    if in1 < in2:
        var2 = frozenset([in1, "AND", in2])
    else:
        var2 = frozenset([in2, "AND", in1])

    var3 = frozenset([var1, "AND", in0])

    out2 = frozenset([var2, "OR", var3])

    return out1, out2

def transform_input(reg):
    lhs, op, rhs = creates[reg]
    if lhs[0] in "xy":
        if rhs[0] == "x":
            return frozenset([rhs, op, lhs])
        return frozenset([lhs, op, rhs])

    if rhs < lhs:
        return frozenset([transform_input(rhs), op, transform_input(lhs)])
    return frozenset([transform_input(lhs), op, transform_input(rhs)])

# part 1
print(simulate())

# part 2
# go through each error and manually swap to correct
# until all 4 swaps have been done
#carry = frozenset(["x00", "AND", "y00"])
#for z in range(1,int(maxz)):
#    zid = "z" + str(z).zfill(2)
#    lhs, op, rhs = creates[zid]
#    out1,out2 = add_bits(carry, "x"+str(z).zfill(2), "y"+str(z).zfill(2))
#    if out1 - transform_input(zid) != set():
#        print("wrong!", zid)
#        print(out1 - transform_input(zid))
#        print(transform_input(zid) - out1)
#    carry = out2


