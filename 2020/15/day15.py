numbers = [11,18,0,20,1,7,16]
test = [0,3,6]

def count_n(iterations, starters):
    spoken = { n:i for i,n in enumerate(starters) }
    say = starters[-1]
    for i in range(len(starters)-1,iterations-1):
        last = say
        say = i - spoken.get(last,i)
        spoken[last] = i
    return say

print("Part 1:",count_n(2020, numbers))
print("Part 2:", count_n(30000000, numbers))
