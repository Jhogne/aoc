with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

atof, ingredients = {}, []
for l in lines:
    items, allergens = l.split(' (contains ')
    items = items.split(" ")
    ingredients += items

    for a in allergens[:-1].split(", "):
        if atof.get(a) == None:
            atof[a] = set(items)
        else:
            atof[a]  = set(items) & atof[a]
            if len(atof[a] ) == 1:
                atof.update(
                    {k: atof[k] - atof[a]  for k in atof.keys() if k != a})

no_allergens = set(ingredients).difference(*[atof[k] for k in atof])
p1 = sum([item in no_allergens for item in ingredients])
p2 = ','.join(atof[k].pop() for k in sorted(atof.keys()))

print("Part 1:", p1)
print("Part 2:", p2)
