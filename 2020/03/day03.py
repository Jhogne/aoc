with open('input.txt', 'r') as f:
    input = f.read().splitlines() 
needed = (8 * len(input)) / len(input[0])
duped = [l * int(needed) for l in input]

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

pos = 0
trees = [0, 0, 0, 0, 0]
for i,slope in enumerate(slopes):
    inc = slope[0]
    pos = 0
    if slope[1] == 2:
        duped = duped[::2]
    for l in duped:
        print(i)
        print(pos)
        if l[pos] == '#':
            trees[i] += 1
        pos += inc
print(trees)
part2 = 1
for num in trees:
    part2 *= num

print("Part 1:",trees)
print("Part 2:",part2)