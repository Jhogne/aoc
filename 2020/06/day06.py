with open('input.txt', 'r') as f:
    groups = f.read().strip().split('\n\n')

part1 = 0
part2 = 0
for group in groups:
    yes = [set(person) for person in group.split('\n')]
    part1 += len(set.union(*yes))
    part2 += len(set.intersection(*yes))

print("Part 1:",part1)
print("Part 2:",part2)