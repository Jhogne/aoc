with open('input.txt', 'r') as f:
    seats = f.read().splitlines()

def step(state, surrounding, max_sur):
    new_state = [['.' for _ in state[row]] for row in range(len(state))]
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == ".":
                continue
            sur = surrounding(state,row,col)
            if state[row][col] == "L" and sur == 0:
                new_state[row][col] = "#"
            elif state[row][col] == "#" and sur >= max_sur:
                new_state[row][col] = "L"
            else:
                new_state[row][col] = state[row][col]
    return new_state

def get_adjacent(state,row,col):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == dy == 0:
                continue
            x = row + dx
            y = col + dy
            if 0 <= x < len(state) and 0 <= y < len(state[row]):
                count += state[x][y] == '#'
    return count

def get_visible(state, row, col):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == dy == 0:
                continue
            x = row + dx
            y = col + dy
            while 0 <= x < len(state) and 0 <= y < len(state[row]):
                if state[x][y] != ".":
                    count += state[x][y] == '#'
                    break
                x += dx
                y += dy
    return count

def simulate(adj_func, max_adj):
    old_state = seats
    while True:
        new_state = step(old_state, adj_func, max_adj)
        if new_state == old_state:
            break
        old_state = new_state
    return sum(x.count('#') for x in new_state)

print("Part 1:",simulate(get_adjacent, 4))
print("Part 2:",simulate(get_visible, 5))
