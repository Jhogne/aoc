from collections import defaultdict
import math

with open('test.txt', 'r') as f:
    tiles = f.read().strip().split('\n\n')

edges = {}
for tile in tiles:
    rows = tile.split('\n')
    id,data = rows[0][5:9], rows[1:]
    top,bot = data[0],data[-1]
    left = "".join([row[0] for row in data])
    right = "".join([row[-1] for row in data])
    edges[int(id)] = {"W":left, "E":right, "N":top, "S":bot} 
    #print(id,data)

def edge_comp(edge1,edge2):
    if edge1 == edge2:
        return True, False
    elif edge1[::-1] == edge2:
        return True, True
    else:
        return False, False

def rotate_edge(edge):
    if edge == "W":
        return "N"
    elif edge == "N":
        return "E"
    elif edge == "E":
        return "S"
    elif edge == "S":
        return "W"

def rotate_edge_amt(edge, amt):
    for _ in range(amt):
        edge = rotate_edge(edge)
    return edge

def flip_edge(edge):
    if edge == "W":
        return "E"
    elif edge == "N":
        return "S"
    elif edge == "E":
        return "W"
    elif edge == "S":
        return "N"
print(edges)
matches = defaultdict(dict)
first = 0
print("id matches flippedx flippedy rotation")
for id in edges:
    flippedx = False
    flippedy = False
    rotation = 0
    for edge in edges[id]:
        for other_id in edges:
            for edge2 in edges[other_id]:
                same, inv = edge_comp(edges[id][edge],edges[other_id][edge2])
                if id != other_id and same:
                    if inv and edge == 'N' or edge == 'S':
                        flippedy = True
                    elif inv and edge == 'W' or edge == 'E':
                        flippedx = True

                    comp = flip_edge(edge2)
                    if edge == "N" or edge == "S" and flippedx:
                        comp = edge2
                    elif edge == "E" or edge == "W" and flippedy:
                        comp = edge2
                        
                    if edge != comp:
                        i = 0
                        tmp = edge
                        while tmp != flip_edge(edge2):
                            tmp = rotate_edge(tmp)
                            i += 1
                        rotation = i
                    matches[id][edge] = other_id
    print(id, matches[id], flippedx, flippedy, rotation)
    if flippedy:
        temp = matches[id].get("E")
        matches[id]["E"] = matches[id].get("W")
        matches[id]["W"] = temp
    if flippedx:
        temp = matches[id].get("N")
        matches[id]["N"] = matches[id].get("S")
        matches[id]["S"] = temp
    old = matches[id].copy()
    for edge in old:
        matches[rotate_edge_amt(edge, rotation)] = old[edge]
        
    if matches[id].get("S") != None and matches[id].get("E") != None and matches[id].get('N') == None and matches[id].get('W') == None:
        print("Hello")
        first = id
print(matches)

def pretty_print(img):
    for row in img:
        for elem in row:
            print(elem, end=' ') 
        print()

def rotate(id, edges):
    new = {}
    for edge in edges:
        new[rotate_edge(edge)] = edges[edge]
    return new


def verify_spot(x,y, img, dirs):
    for edge in dirs:
        dx = dy = 0
        if edge == "N":
            dy -= 1
        elif edge == "S":
            dy += 1
        elif edge == "E":
            dx += 1
        elif edge == "W":
            dx -= 1

        if not(0 <= x+dx < size and 0 <= y+dy < size):
            return False
    return True
print(matches)
size = int(math.sqrt(len(edges)))
img = [[0 for _ in range(size)] for _ in range(size)]
curr = first
img[0][0] = first
x = y = 0
while curr != 0:
    nextx, nexty, nextcurr = 0,0,0
    my_edges = matches[curr].copy()
    pretty_print(img)
    print(curr, my_edges)
    while not verify_spot(x,y,img, my_edges):
        my_edges = rotate(curr, my_edges)
    print(curr,my_edges)
    for edge in my_edges:
        dx = dy = 0
        if edge == "N":
            dy -= 1
        elif edge == "S":
            dy += 1
        elif edge == "E":
            dx += 1
        elif edge == "W":
            dx -= 1
        if img[x+dx][y+dy] == 0:
            nextx,nexty,nextcurr = x+dx,y+dy,my_edges[edge]
            img[x+dx][y+dy] = my_edges[edge]
    x,y,curr = nextx,nexty,nextcurr

p1 = 1
# for id in matches:
#     if len(matches[id]) == 2:
#         print(id, matches[id])

print("Part 1:",p1)
print("Part 2:")
