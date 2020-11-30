from itertools import product

part2 = True
msg = "Part2: " if part2 else "Part1: "

with open('input.txt', 'r') as f:
    input = f.read().split(',')
numbers = [int(x) for x in input]

def run(noun, verb, code):
    code[1] = noun
    code[2] = verb

    i = 0
    while code[i] != 99:
        x,y,pos = code[i+1],code[i+2], code[i+3]
        if code[i] == 1:
            code[pos] = code[x] + code[y]
            i += 4
        elif code[i] == 2:
            code[pos] = code[x] * code[y]
            i += 4

code = numbers.copy()
run(12,2, code)
print("Part 1: " + str(code[0]))

for i,j in product(range(100), range(100)):
        code = numbers.copy()
        run(i,j, code)
        if(code[0] == 19690720):
            print("Part 2: " + str(100*code[1] + code[2]))
            break