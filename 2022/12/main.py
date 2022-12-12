import math

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

E, ES = [], []
S = None
M = [[None] * len(lines[0]) for l in lines]
for (y, line) in enumerate(lines):
    for (x, c) in enumerate(line):
        M[y][x] = ord(c)
        if c == 'S':
            S = (y, x)
            M[y][x] = ord('a')
        elif c == 'E':
            E.append((y, x))
            M[y][x] = ord('z')

        if M[y][x] == ord('a'):
            ES.append((y, x))

def get_adjecent(y,x):
    for (dy, dx) in [(1,0), (0,1), (-1,0), (0,-1)]:
        if 0 <= y + dy < len(M) and 0 <= x + dx < len(M[0]):
            yield (y+dy, x+dx)

def bfs(start):
    seen = set(start)
    q = [(*S, 0)]
    while len(q):
        (y, x, d) = q.pop(0)
        if (y, x) in E:
            return d
        for (ny,nx) in get_adjecent(y, x):
            if (ny, nx) not in seen and M[ny][nx] - M[y][x] < 2:
                seen.add((ny, nx))
                q.append((ny, nx, d+1))

    return math.inf 

print(bfs(S))
S = E.pop()
E = ES
M = [[-x for x in lines] for lines in M]
print(bfs(S))
