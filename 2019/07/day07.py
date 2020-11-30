from itertools import permutations
import threading

with open('input.txt', 'r') as f:
    string = f.read().split(',')
numbers = [int(x) for x in string]

lengths = [5,5,3,3,4,4,5,5]
def run(code, id, inputs, semaphores):
    i = 0
    out = []
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
            semaphores[id].acquire()
            code[code[i+1]] = inputs[id][0]
            inputs[id] = inputs[id][1:] 
            i += 2
        elif op == 4:
            out = 0 if id == 4 else id +1
            inputs[out].append(params[0])
            semaphores[out].release()
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
            print('something went wrong')

def run_series(p_min, p_max):
    phases = permutations(range(p_min,p_max+1))
    outs =  []
    for phase in phases:
        semaphores = [threading.Semaphore(1) for _ in range(0,5)]
        inputs = [[p] for p in phase]

        threads = []
        for i in range(0,5):
            t = threading.Thread(target = run, args = (numbers.copy(), i, inputs, semaphores))
            threads.append(t)
            t.start()

        inputs[0].append(0)
        semaphores[0].release()

        for t in threads:
            t.join()

        outs.append(inputs[0][0])
    return max(outs)

print('Part 1: ' + str(run_series(0,4)))
print('Part 2: ' + str(run_series(5, 9)))