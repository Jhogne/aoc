with open('input.txt', 'r') as f:
    string = f.read().split(',')
numbers = [int(x) for x in string]

lengths = [5,5,3,3,4,4,5,5]

def run(code):
    i = 0
    while code[i] != 99:
        opmodes = str(code[i])[::-1]
        op = int(opmodes[:1])
        for _ in range(0, lengths[op - 1] - len(opmodes)):
            opmodes += '0'
        params = []
        for offset,m in enumerate(opmodes[2:], start=1):
            if offset == 3: # write to is always immediate mode and always third parameter 
                val = code[i+offset]
            else:
                val = code[code[i+offset]] if int(m) == 0 else code[i+offset]
            params.append(val)
        if op == 1:
            code[params[2]] = params[1] + params[0]
            i += 4
        elif op == 2:
            code[params[2]] = params[1] * params[0]
            i += 4
        elif op == 3:
            code[code[i+1]] = int(input("Enter value: "))
            i += 2
        elif op == 4:
            print(params[0])
            i += 2
        elif op == 5:
            i = params[1] if params[0] != 0 else i + 3
        elif op == 6:
            i = params[1] if params[0] == 0 else i + 3
        elif op == 7:
            code[params[2]] = 1 if params[0] < params[1] else 0
            i += 4
        elif op == 8:
            code[params[2]] = 1 if params[0] == params[1] else 0
            i += 4
        else:
            break
run(numbers)
