with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

pipes = {}
start = (-1,-1)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        match lines[i][j]:
            case "S": start = (i,j)
            case "|": pipes[(i,j)] = ((i+1,j),(i-1,j))
            case "-": pipes[(i,j)] = ((i,j+1),(i,j-1))
            case "L": pipes[(i,j)] = ((i,j+1),(i-1,j))
            case "J": pipes[(i,j)] = ((i,j-1),(i-1,j))
            case "7": pipes[(i,j)] = ((i,j-1),(i+1,j))
            case "F": pipes[(i,j)] = ((i,j+1),(i+1,j))

N,E,S,W = (-1,0),(0,1),(1,0),(0,-1)
def move_dir(curr, d):
    return (curr[0]+d[0], curr[1]+d[1])

def right_of_pipe():
    seen, right = set(), set()
    curr = start
    rh = S # for my input
    
    while curr not in seen:
        seen.add(curr)

        right.add(move_dir(curr, rh))
        match lines[curr[0]][curr[1]]:
            case "7": rh = N if rh == E else W
            case "J": rh = N if rh == W else E
            case "L": rh = S if rh == W else E
            case "F": rh = S if rh == E else W

        right.add(move_dir(curr, rh))
        for n in pipes[curr]:
            if n not in seen:
                curr = n

    return right - main_pipe

def find_cluster(s):
    seen = set()
    q = {s}
    while len(q) > 0:
        c = q.pop()
        seen.add(c)
        for n in [move_dir(c,N), move_dir(c,E), move_dir(c,S),move_dir(c,W)]:
            if n not in seen and n not in main_pipe:
                q.add(n)
    return seen

q = [start]
pipes[start] = [(115, 41),(114,40)] # for my input
main_pipe = set()
ds = {q[0]: 0}
while len(q) > 0:
    c = q.pop(0)
    main_pipe.add(c)
    for n in pipes[c]:
        if n not in main_pipe:
            q.append(n)
            ds[n] = ds[c] + 1

print(max(ds.values()))
print(len(set.union(*[find_cluster(s) for s in right_of_pipe()])))
