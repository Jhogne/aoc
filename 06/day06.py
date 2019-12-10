with open('input.txt', 'r') as f:
    strings = f.read().splitlines()
inputs = [s.split(')') for s in strings]

graph = {}
for center,orbit in inputs:
    graph[orbit] = center

def length(node):
    if node == 'COM':
        return 0
    return length(graph[node]) + 1

def path(node):
    if(node == 'COM'):
        return []
    return [node] + path(graph[node])
    
sum = 0
for i in graph:
    sum += length(i)
print("Part 1: " + str(sum))

li1, li2 = path('YOU')[1:], path('SAN')[1:]
li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
print("Part 2: " + str(len(li_dif)))