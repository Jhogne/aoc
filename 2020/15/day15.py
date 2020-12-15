import time

start = time.time()

numbers = [11,18,0,20,1,7,16]
test = [0,3,6]


def count(starters, iterations):
    spoken = {}
    last = -1
    say = -1
    first_time = False
    for i in range(0,iterations):
        last = say
        if i < len(starters):
            say = starters[i]  
            first_time = say not in spoken  
            spoken[say] = i
        elif first_time:
            say = 0
            first_time = say not in spoken
        else:
            say = i - 1 - spoken[last]
            first_time = say not in spoken
            if first_time:
                spoken[say] = i
            spoken[last] = i - 1
    return say




print("Part 1:",count(numbers, 2020))
print("Part 2:", count(numbers, 30000000))
print(time.time() - start)