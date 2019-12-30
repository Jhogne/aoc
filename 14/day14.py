import networkx as nx

with open('input.txt', 'r') as f:
    strings = f.read().splitlines()
G = nx.DiGraph() 
G.add_node('ORE')

produced = {}
for s in strings:
    x = s.split(' => ')
    ins = list(map(lambda x: x.split(' '), x[0].split(', ')))
    out = x[1].split(' ')
    produced[out[1]] = int(out[0])
    for i in ins:
        G.add_edge(out[1], i[1], weight=int(i[0]))

def find_reqs(G, amt):
    elems = list(G.nodes())
    elems.remove('FUEL')
    reqs = {'FUEL':amt}
    curr = 'FUEL'

    while elems != []:
        for i in elems:
            if all([x[0] not in elems for x in list(G.in_edges(i))]):
                curr = i
        in_edges = list(G.in_edges(curr))
        elems.remove(curr)
        for i in in_edges:
            this = i[1]
            parent = i[0]
            reqs[curr] = reqs.get(curr, 0) + -(-reqs[parent] // produced[parent]) * G[parent][this]['weight']
    return reqs

def max_fuel(G):
    target = 1000000000000
    over = under = 1
    ore_over = ore_under = find_reqs(G, over)['ORE']
    while True:
        if ore_over > target and ore_under < target:
            middle = (under + over) // 2
            ore_middle = find_reqs(G, middle)['ORE']
            if ore_middle < target and target - ore_middle < target - ore_under:
                under = middle
            elif ore_middle > target and ore_middle - target < ore_over - target:
                over = middle
            else:
                return under
        else:
            under = over
            over *= 2

        ore_over = find_reqs(G, over)['ORE']
        ore_under = find_reqs(G, under)['ORE']

print('Part 1:',find_reqs(G, 1)['ORE'])
print('Part 2:', max_fuel(G))