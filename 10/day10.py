import math

with open('input.txt', 'r') as f:
    string = f.read().splitlines()
asteroids = []
for i,_ in enumerate(string):
    for j,_ in enumerate(string[i]):
        if string[i][j] == '#':
            asteroids.append((j,i))
        elif string[i][j] == 'X':
            best = (j,i)

def is_blocked(a1, a2):
    start = min(a1, a2, key=lambda x: x[0])
    end = a1 if start == a2 else a2

    x, y_start = start[0], start[1]
    x_end, y_end = end[0], end[1]
    min_y = min(y_start, y_end)

    if x == x_end:
        for i in range(abs(y_start - y_end)):
            if (x, min_y+i) in asteroids and (x, min_y+i) != a1 and (x, min_y+i) != a2:
                return True
        return False

    k = (y_end - y_start) / (x_end - x)
    m = y_start - k*x

    while x < x_end:
        point = (x,round(m+k*x, 1))
        if point in asteroids and point != a1 and point != a2:
            return True
        x += 1
    return False 

min_blocked = 9999
los = []
for i in asteroids:
    n_blocked = 0
    immediate = []
    for j in asteroids:
        blocked = is_blocked(i,j)
        if i != j and blocked:
            n_blocked += 1 
        elif i != j:
            immediate.append(j)
    if n_blocked < min_blocked: 
        min_blocked = n_blocked
        best = i
        los = immediate

print('Part 1: ' + str(len(asteroids) -1 - min_blocked))

h1 = [x for x in los if x[0] >= best[0]]
h2 = [x for x in los if x[0] < best[0]]

h2.sort(key=lambda x: math.atan2(best[1] - x[1], best[0] - x[0]))
no200 = h2[200-len(h1)-1] # This is true for my input. I tested it manually
print('Part 2: ' + str(no200[0] * 100 + no200[1]))
