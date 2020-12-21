from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


atof = defaultdict(set)
all_items = set()
for l in lines:
    items, allergens = l.split(' (contains ')
    allergens = allergens[:-1]
    items = items.split(" ")
    all_items.update(items)
    allergens = allergens.split(", ")
    for a in allergens:
        if len(atof[a]) == 0:
            atof[a] = set(items)
        else:
            candidates = set(items) & atof[a]
            atof[a] = candidates
            if len(candidates) == 1:
                for k in atof:
                    if k != a:
                        atof[k] = atof[k] - candidates

for k in atof:
    all_items -= atof[k]
print(atof)
print(all_items)
count = 0
for l in lines:
    items, _ = l.split(' (contains ')
    for item in items.split(' '):
        if item in all_items:
            count += 1


keys = atof.keys()
keys = sorted(keys)
print(keys)
p2 = ''
for key in keys:
    p2 += atof[key].pop()
    p2 += ','

print("Part 1:", count)
print("Part 2:", p2[:-1])
