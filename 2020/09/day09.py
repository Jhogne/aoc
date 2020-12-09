from itertools import combinations 

with open('input.txt', 'r') as f:
    numbers = [int(l) for l in f.read().splitlines()]

CHUNKS = 25
def find_target(numbers):
    for i in range(CHUNKS,len(numbers)):
        if not any([x + y == numbers[i] for x,y in combinations(numbers[i-CHUNKS:i], 2)]):
            return i

def find_weakness(numbers, target):
    for end in range(1,target):
        for start in range(end):
            if sum(numbers[start:end]) == numbers[target]:
                return min(numbers[start:end]) + max(numbers[start:end])

target = find_target(numbers)
print("Part 1:",numbers[target])
print("Part 2:",find_weakness(numbers, target))