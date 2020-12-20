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


def edge_comp(edge1,edge2):
    if edge1 == edge2:
        return True
    elif edge1[::-1] == edge2:
        return True
    else:
        return False


def rotate_cell(edges, id):
    olds = edges[id].copy()

    for edge in olds:
        if edge == "W":
            new = olds.get("S")
        elif edge == "N":
            new = olds.get("W")
        elif edge == "E":
            new = olds.get("N")
        elif edge == "S":
            new = olds.get("E")
        edges[id][edge] = new

def flip_cell(edges, id, yaxis):
    olds = edges[id].copy()

    for edge in olds:
        if yaxis:
            if edge == "W":
                new = olds.get("E")
            elif edge == "E":
                new = olds.get("W")
            elif edge == "N":
                new = olds.get("N")
            elif edge == "S":
                new = olds.get("S")
        else:
            if edge == "N":
                new = olds.get("S")
            elif edge == "S":
                new = olds.get("N")
            elif edge == "W":
                new = olds.get("W")
            elif edge == "E":
                new = olds.get("E")
        edges[id][edge] = new

def rotate_edge(edge):
    if edge == "W":
        return "N"
    elif edge == "N":
        return "E"
    elif edge == "E":
        return "S"
    elif edge == "S":
        return "W"

def flip_edge(edge):
    if edge == "W":
        return "E"
    elif edge == "N":
        return "S"
    elif edge == "E":
        return "W"
    elif edge == "S":
        return "N"

def pretty_print(img):
    for row in img:
        for elem in row:
            print(elem, end=' ') 
        print()
    print()



matches = defaultdict(dict)
start = 0
for id in edges:
    for edge in edges[id]:
        for other_id in edges:
            for edge2 in edges[other_id]:
                same = edge_comp(edges[id][edge],edges[other_id][edge2])
                if id != other_id and same:
                    matches[id][edge] = other_id
                else:
                    if not matches[id].get(edge):
                        matches[id][edge] = None
    if matches[id].get('S') != None and matches[id].get('N') != None and matches[id].get('W') != None and matches[id].get('E') != None:
        start = id

# print(edges)
# print(matches)
# print(start)
# print(edges[start])
# rotate_cell(edges, start)
# print(edges[start])
def exact_edge_comp(edge1,edge2):
    if edge1 == edge2:
        return 2
    elif edge1[::-1] == edge2:
        return 1
    else:
        return 0    

size = int(math.sqrt(len(edges)))
img = [[0 for _ in range(size)] for _ in range(size)]
def fill_neighbours(y, x, curr, img, matches, edges):
    print("Currently at",curr, matches[curr])
    for edge in matches[curr]:
        neighbour = matches[curr][edge]
        if neighbour == None:
            continue
        e1 = edges[curr][edge]
        e2 = edges[neighbour][flip_edge(edge)]
        #print(e1, e2)
        #print("Before rotation of",neighbour, matches[neighbour])
        print("Before translation:",neighbour, matches[neighbour])
        while exact_edge_comp(e1,e2) == 0:
            rotate_cell(edges, neighbour)
            rotate_cell(matches, neighbour)
            e2 = edges[neighbour][flip_edge(edge)]
        print("After Rotation:",neighbour, matches[neighbour])
        if exact_edge_comp(e1,e2) == 1:
            if edge == "N" or edge == "S":
                flip_cell(edges, neighbour, False)
                flip_cell(matches, neighbour, False)
            elif edge == "E" or edge == "W":
                flip_cell(edges, neighbour, True)
                flip_cell(matches, neighbour, True)
        print("After translation:",neighbour, matches[neighbour])
        #print("After rotation of",neighbour, matches[neighbour])
        #print(e1,e2)
        print(edge, neighbour)
        if edge == "N":
            img[y-1][x] = neighbour
        elif edge == "S":
            img[y+1][x] = neighbour
        elif edge == "W":
            img[y][x-1] = neighbour
        elif edge == "E":
            img[y][x+1] = neighbour


print(matches)
print(start)
done = set()
done.add(None)
curr = start
x = y = 1
while len(done) < len(matches) and curr != None:
    pretty_print(img)
    print(y,x, curr)
    done.add(curr)
    if img[y][x] == 0:
        img[y][x] = curr
    fill_neighbours(y,x,curr,img,matches,edges)
    for edge in matches[curr]:
        if matches[curr][edge] not in done:
            curr = matches[curr][edge]
            if edge == "N":
                y -= 1
            elif edge == "S":
                y += 1
            elif edge == "E":
                x += 1
            elif edge == "W":
                x -= 1
            break
    # print(curr)
    # print(y,x)
    # print(done)
pretty_print(img)