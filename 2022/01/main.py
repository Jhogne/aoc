with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n\n')

carrying = [sum(int(c) for c in elf.splitlines()) for elf in lines]

print(sorted(carrying)[-1])
print(sum(sorted(carrying)[-3:]))
