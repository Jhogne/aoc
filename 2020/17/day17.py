from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

state = [[l for l in lines]]

def get_neighbours(x,y,z):
    neighbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if not i == j == k == 0:
                   neighbours.append((x+i,y+j,z+k))
    return neighbours                            

def count_active(state,positions):
    count = 0
    for pos in positions:
        if pos[0] >= 0 and pos[1] >= 0 and pos[2] >= 0 and pos[0] < len(state) and pos[1] < len(state[0]) and pos[2] < len(state[0][0]):
            count += state[pos[0]][pos[1]][pos[2]] == '#'
    return count

def step(state):

    new_state = [[ ['.' for col in range(len(state[0])+2)] for col in range(len(state[0])+2)] for row in range(len(state))] 

    for x in range(len(new_state)):
        for y in range(len(new_state[x])):
            for z in range(len(new_state[x][y])):
                active = count_active(state,get_neighbours(x,y-1,z-1))
                if 0 < z <= len(state[0][0]) and 0 < x <= len(state) and 0 < y <= len(state[0]):
                    if state[x][y-1][z-1] == '#' and (active == 2 or active == 3):
                        new_state[x][y][z] = '#'
                    elif state[x][y-1][z-1] == '.' and active == 3:
                        new_state[x][y][z] = '#'
                elif active == 3:
                        new_state[x][y][z] = '#'
    return new_state

def pretty_print(state):
    for z in range(len(state)):
        print("z = {}".format(z))
        for x in state[z]:
            print(x)


for i in range(6):
    #print("Old state:",state)
    new_layer = state[0].copy()
    new_layer = ['.' * len(new_layer[0]) for _ in new_layer]
    state.insert(0,new_layer)
    state.append(new_layer)
    pretty_print(state)

    state = step(state)    


print(sum(x.count('#') for y in state for x in y))
print("Part 1:")
print("Part 2:")
