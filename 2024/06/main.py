with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

minx,miny,maxx,maxy = 0,0,len(lines),len(lines[0])
ds = [(-1,0), (0,1), (1,0), (0,-1)]
obstructions = set()

for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == '#':
            obstructions.add((y,x))
        elif c == '^':
            start = (y,x)

def find_path(obstructions):
    d, pos, seen = 0, start, set()
    while miny <= pos[0] < maxy and minx <= pos[1] < maxx:
        if (pos,d) in seen:
            return {}
        seen.add((pos, d))
        next_step = pos[0] + ds[d][0], pos[1] + ds[d][1]
        if next_step in obstructions:
            d = (d + 1) % 4
        else:
            pos = next_step
    return {pos for (pos, _) in seen}
    
path = find_path(obstructions)

p2 = 0
for (y,x) in path:
    if (y,x) in obstructions or (y,x) == start:
        continue
    if find_path(obstructions | {(y,x)}) == {}:
        p2 += 1

print(len(path))
print(p2)
