from itertools import count

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

RL, RH = len(lines[0]) - 2, len(lines) - 2
BLIZZ_DIR = {'>':(0,1), '<': (0,-1), 'v': (1,0), '^': (-1,0)}
blizzards = set()
y = x = 0
for line in lines[1:]:
    for c in line:
        if c == '#':
            continue
        elif c in BLIZZ_DIR:
            blizzards.add(((y,x), BLIZZ_DIR[c]))
        x += 1
    y += 1

start = (-1, 0)
end = (RH, RL-1)

DIRS = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]
def get_next(pos):
    for dy,dx in DIRS:
        ny, nx = pos[0] + dy, pos[1] + dx
        if (0 <= ny < RH and 0 <= nx < RL) or (ny,nx) in [start, end]:
            yield ny,nx

def move_blizzards(i):
    newb = set()
    for (y,x),(dy,dx) in blizzards:
        y = (y + i*dy) % RH
        x = (x + i*dx) % RL
        newb.add((y,x))
    return newb

def find_path(start, end, offset):
    possible = {start}
    for i in count():
        next_possible = set()
        blizz = move_blizzards(i+offset)

        for pos in possible:
            for adj in get_next(pos):
                if not adj in blizz:
                    next_possible.add(adj)

        possible = next_possible
        if end in possible:
            return i

fst = find_path(start, end, 0)
snd = find_path(end, start, fst)
thd = find_path(start, end, fst+snd)

print(fst)
print(fst+snd+thd)
