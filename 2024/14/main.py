import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

maxx, maxy = 101, 103
initial_state = set()
for l in lines:
    nums = tuple(int(x) for x in re.findall(r"-?\d+", l))
    initial_state.add(nums)

def print_grid(poss):
    for y in range(maxy):
        for x in range(maxx):
            if (x,y) in poss:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def simulate_seconds(robots, seconds, visualize=False):
    for i in range(seconds):
        if visualize and i % 101 == 79:
            print('=====', i, '=====')
            print_grid(set((x,y) for x,y,_,_ in robots))
        new_state = set()
        for x,y,vx,vy in robots:
            newx, newy = x+vx, y+vy
            if newx >= maxx:
                newx -= maxx
            elif newx < 0:
                newx += maxx
            if newy >= maxy:
                newy -= maxy
            elif newy < 0:
                newy += maxy
            new_state.add((newx,newy,vx,vy))

        robots = new_state
    return robots

def saftey_factor(robots):
    midx, midy = maxx // 2, maxy // 2
    topl, topr, botl, botr = 0,0,0,0

    for x,y,_,_ in robots:
        if x < midx and y < midy:
            topl += 1
        elif x < midx and y  > midy:
            topr += 1
        elif x > midx and y < midy:
            botl += 1
        elif x > midx and y > midy:
            botr += 1
    return topl * topr * botl * botr


print(saftey_factor(simulate_seconds(initial_state, 100)))
# after looking at the visualizations there was some pattern emerging 
# at a regular interval, print those states and watch until the picture appears
simulate_seconds(initial_state, 10000, True)
