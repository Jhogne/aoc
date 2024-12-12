with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

grid = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        grid[(y,x)] = c

def neighbours(y,x):
    return [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]

def all_neighbours(y,x):
    return neighbours(y,x) + [(y+1, x+1), (y-1, x+1), (y+1, x-1), (y-1, x-1)]

def bfs(start):
    q = [start]
    shape = set()
    while q:
        pos = q.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        shape.add(pos)

        for n in neighbours(*pos):
            if n in grid and grid[start] == grid[n] and grid[n] not in seen:
                q.append(n)
    return shape

def count_perim(points):
    tot = 0
    for (y,x) in points:
        for (dy,dx) in neighbours(y,x):
            if (dy,dx) not in points:
                tot += 1
    return tot


def find_perim(points):
    fences = set()
    for (y,x) in points:
        for (dy,dx) in all_neighbours(y,x):
            if (dy,dx) not in points:
                fences.add((y,x))

    return fences 

def get_direction(curr, prev):
    dy,dx = curr[0]-prev[0], curr[1]-prev[1]
    return (min(1,max(-1,dy)), min(1,max(-1,dx)))

def count_edges(perim):
    tot = 0
    while perim:
        miny = min(y for (y,_) in perim)
        start = (miny, min(x for (y1,x) in perim if y1 == miny))
        q = [start]
        seen = set()
        prev = (start, (0,0))
        while q:
            curr = q.pop()
            if curr in seen:
                continue

            seen.add(curr)
            di = get_direction(curr, prev[0])
            if di != prev[1]:
                tot += 1
            prev = (curr,di)

            for n in neighbours(*curr):
                if n in perim and n not in seen:
                    q.append(n)
                    break

        perim -= seen
    return tot

p1 = 0
seen = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        shape = bfs((y,x))
        if len(shape) > 0:
            perim = count_perim(shape)
            p1 += perim * (len(shape))

grid = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        for dx in [0,1,2]:
            for dy in [0,1,2]:
                grid[(3*y+dy,3*x+dx)] = c

p2 = 0
seen = set()
for y in range(3*len(lines)):
    for x in range(3*len(lines[0])):
        shape = bfs((y,x))
        if len(shape) > 0:
            perim = find_perim(shape)
            edges = count_edges(perim)
            p2 += edges * (len(shape) // 9)

print(p1)
print(p2)
