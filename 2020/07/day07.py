from collections import defaultdict
import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

contains = defaultdict(list)
parent = defaultdict(list)
for line in lines:
    outer, inner = re.split(' bags contain ', line)
    for amt_color in inner.split(', '):
        if(amt_color != 'no other bags.'):
            color = amt_color.rsplit(' ',1)[0][2:]
            contains[outer].append((int(amt_color[0]), color))
            parent[color].append(outer)

def holds_bag(target):
    bags = set()
    for bag in parent[target]:
        bags.add(bag)
        bags.update(holds_bag(bag))
    return bags

def bags_contained_in(target):
    return sum(num + num * bags_contained_in(color) for num,color in contains[target])

print("Part 1:",len(holds_bag('shiny gold')))
print("Part 2:",bags_contained_in('shiny gold'))
