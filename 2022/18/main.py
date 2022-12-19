with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

DIRS = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

pts = set()
for line in lines:
    pt = tuple(map(int, line.split(',')))
    pts.add(pt)

outside = (max(pt[0] for pt in pts) + 1, 0, 0)

def get_adjecent(x,y,z):
    for (dx,dy,dz) in DIRS:
        pt = (x+dx, y+dy, z+dz) 
        if pt not in pts:
            yield pt


cache = {}
def is_inside(start):
    seen, q = set(start), [start]
    while q:
        pt = q.pop(0)
        if pt == outside:
            return False 
        if pt in cache:
            return cache[pt]
        for adj in get_adjecent(*pt):
            if adj not in seen:
                seen.add(adj)
                q.append(adj)

    return True 


p1 = p2 = 0
for turn, (x,y,z) in enumerate(pts):
    for (dx,dy,dz) in DIRS:
        pt = (x+dx, y+dy, z+dz)
        if pt not in pts:
            p1 += 1
            inside = is_inside(pt)
            cache[pt] = inside
            p2 += not inside

print(p1)
print(p2)
