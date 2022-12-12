with open('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()

def sacks_prio(sacks):
    item = set.intersection(*map(set,sacks)).pop()

    if item.isupper():
        return ord(item) - 38;
    else:
        return ord(item) - 96;

def split_halves(s):
    return [s[:len(s)//2], s[len(s)//2:]]

def chunks(l):
    return [l[i:i+3] for i in range(0, len(l), 3)]

p1 = sum(map(sacks_prio, map(split_halves, lines)))
p2 = sum(map(sacks_prio, chunks(lines)))

print(p1)
print(p2)
