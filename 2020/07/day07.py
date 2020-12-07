from collections import defaultdict
import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

rules = defaultdict(list)
for line in lines:
    outer, inner = re.split(' bags contain ', line)
    for numbag in inner.split(', '):
        if(numbag == 'no other bags.'):
            break
        rules[outer].append((int(numbag[0]), numbag.rsplit(' ',1)[0][2:]))
        
def holds_bag(target):
    bags = set()
    outer = [bag for bag in rules.keys() if target in [tup[1] for tup in rules[bag]]]
    for bag in outer:
        bags.add(bag)
        bags.update(holds_bag(bag))
    return bags

def bags_contained(target):
    if not rules[target]:
        return 0
    tot = 0
    for num,color in rules[target]:
        tot += num + num * bags_contained(color)
    return tot

print("Part 1:",len(holds_bag('shiny gold')))
print("Part 2:",bags_contained('shiny gold'))