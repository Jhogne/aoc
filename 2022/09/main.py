with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

sign = lambda x: complex((x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0))
DIRS = {'R': 1, 'U': 1j, 'L': -1, 'D': -1j}

rope = [0+0j] * 10
visited = [{0} for _ in rope]

for line in lines:
    d, amt = line.split()
    for _ in range(int(amt)):
        rope[0] += DIRS[d]

        for i in range(1, len(rope)):
            if abs(rope[i-1] - rope[i]) >= 2:
                rope[i] += sign(rope[i-1] - rope[i])

            visited[i].add(rope[i])

print(len(visited[1]))
print(len(visited[-1]))
