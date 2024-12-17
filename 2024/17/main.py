import re

with open('real.in', 'r') as f:
    lines = f.read().strip()

nums = [int(x) for x in re.findall(r"\d+", lines)]
registers = {"A": nums[0], "B": nums[1], "C": nums[2]}
ops = nums[3:]

def run(registers):
    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return registers["A"]
        if operand == 5:
            return registers["B"]
        if operand == 6:
            return registers["C"]
        assert False

    pc = 0
    output = []
    while pc < len(ops):
        operation = ops[pc]
        operand = ops[pc+1]

        if operation == 0:
            registers["A"] //= (2**combo(operand))
        elif operation == 1:
            registers["B"] ^= operand
        elif operation == 2:
            registers["B"] = combo(operand) % 8
        elif operation == 3:
            if registers["A"] != 0:
                pc = operand
                continue
        elif operation == 4:
            registers["B"] ^= registers["C"]
        elif operation == 5:
            output.append(combo(operand) % 8)
        elif operation == 6:
            registers["B"] = registers["A"] // (2**combo(operand))
        elif operation == 7:
            registers["C"] = registers["A"] // (2**combo(operand))

        pc += 2
    return output

p2 = 8 ** (len(ops)-1)
while True:
    output = run({"A": p2, "B": nums[1], "C": nums[2]})

    for i,out in reversed(list(enumerate(output))):
        if ops[i] != out:
             p2 += 8 ** i
             break

    if output == ops:
        break

print(','.join(map(str, run(registers))))
print(p2)
