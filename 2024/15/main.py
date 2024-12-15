with open('real.in', 'r') as f:
    lines = f.read().strip().split('\n\n')

grid = [list(s) for s in lines[0].splitlines()]

dirs = {"<": (0,-1), "v": (1,0), ">": (0,1), "^": (-1,0)}
other_box = {'[': 1, ']': -1}

def close_box(c):
    return {'[': ']', ']': '['}[c]

def can_move(y,x,di):
    ny,nx = y+di[0],x+di[1]
    if grid[ny][nx] == '.':
        return True
    if grid[ny][nx] == '#':
        return False

    if di[0] == 0 or grid[ny][nx] == 'O':
        return can_move(ny,nx,di)

    if grid[ny][nx] == '[':
        return can_move(ny,nx,di) and can_move(ny,nx+1,di)
    return can_move(ny,nx,di) and can_move(ny,nx-1,di)

def hmove(y,x,di):
    nx = x + di[1] * 2
    if grid[y][nx] == grid[y][x]:
        move_box(y,nx,di)
        if grid[y][nx] == grid[y][x]:
            return
    grid[y+di[0]][x+di[1]] = grid[y][x]
    grid[y+di[0]][nx] = close_box(grid[y][x])

def vmove(y,x,di):
    ny = y + di[0]
    otherx = x+other_box[grid[y][x]]
    if grid[ny][x] in '[]':
        move_box(ny,x,di)
    if grid[ny][otherx] in '[]':
        move_box(ny,otherx,di)

    grid[ny][x+di[1]] = grid[y][x]
    grid[ny][otherx+di[1]] = close_box(grid[y][x])
    grid[y][otherx] = '.'

def move_box(y,x, di):
    if grid[y][x] == 'O':
        if not can_move(y,x,di):
            return

        if grid[y+di[0]][x+di[1]] == 'O':
            move_box(y+di[0],x+di[1],di)
            if grid[y+di[0]][x+di[1]] == 'O':
                return

        grid[y+di[0]][x+di[1]] = 'O'
        grid[y][x] = '.'

    if grid[y][x] in '[]':
        if not can_move(y,x,di) or not can_move(y,x+other_box[grid[y][x]],di):
            return
        if di == (0,1) or di == (0,-1):
            hmove(y,x,di)
        else:
            vmove(y,x,di)

        grid[y][x] = '.'
    
def step(pos, di):
    ny,nx = pos[0]+di[0], pos[1]+di[1]
    if grid[ny][nx] == '.':
        return ny,nx
    if grid[ny][nx] == '#':
        return pos

    move_box(ny, nx, di)

    if grid[ny][nx] in '[]O':
        return pos
    else:
        return ny,nx


def move_robot(grid):
    ry,rx = -1, -1
    for y,l in enumerate(grid):
        for x,c in enumerate(l):
            if c == '@':
                ry,rx = y,x

    for d in ''.join(lines[1:]).replace('\n',''):
        ny,nx = step((ry,rx), dirs[d])
        if ny != ry or nx != rx:
            grid[ny][nx] = "@"
            grid[ry][rx] = "."
        ry,rx = ny,nx

p1 = 0
move_robot(grid)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            p1 += 100 * y + x

lines[0] = lines[0].replace("O", "[]")
lines[0] = lines[0].replace("#", "##")
lines[0] = lines[0].replace(".", "..")
lines[0] = lines[0].replace("@", "@.")
grid = [list(s) for s in lines[0].splitlines()]
move_robot(grid)

p2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '[':
            p2 += 100 * y + x

print(p1)
print(p2)
