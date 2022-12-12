with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def tick(x):
    global cycle, signal, crt

    # part 1
    cycle += 1
    if cycle % 40 == 20:
        signal += x * cycle

    # part 2
    pixel = (cycle - 1) % 40
    if abs(pixel - x) < 2:
        crt += '#'
    else:
        crt += ' '

    pixel += 1

    if pixel % 40 == 0:
        crt += '\n'

cycle = signal = 0
x = 1
crt = ""
for line in lines:
    tick(x)

    if line == "noop":
        continue

    tick(x)

    x += int(line.split()[1])

print(signal)
print(crt)
