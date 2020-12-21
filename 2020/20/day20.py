from collections import defaultdict
import math
import time

start_time = time.time()
with open('input.txt', 'r') as f:
    tiles = f.read().strip().split('\n\n')


edges = {}
pixels = {}
for tile in tiles:
    rows = tile.split('\n')
    id, data = rows[0][5:9], rows[1:]
    top, bot = data[0], data[-1]
    left = "".join([row[0] for row in data])
    right = "".join([row[-1] for row in data])
    edges[int(id)] = {"W": left, "E": right, "N": top, "S": bot}
    pixels[int(id)] = data


def edge_comp(edge1, edge2):
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
            if new != None and type(new) != int:
                new = new[::-1]
        elif edge == "E":
            new = olds.get("N")
        elif edge == "S":
            new = olds.get("E")
            if new != None and type(new) != int:
                new = new[::-1]

        edges[id][edge] = new


def flip_cell(edges, id, yaxis):
    olds = edges[id].copy()

    for edge in olds:
        if yaxis:
            if edge == "W" or edge == "E":
                new = olds.get(flip_edge(edge))
            else:
                new = olds.get(edge)
                if new != None and type(new) != int:
                    new = new[::-1]
        else:
            if edge == "N" or edge == "S":
                new = olds.get(flip_edge(edge))
            else:
                new = olds.get(edge)
                if new != None and type(new) != int:
                    new = new[::-1]
        edges[id][edge] = new


def flip_edge(edge):
    if edge == "W":
        return "E"
    elif edge == "N":
        return "S"
    elif edge == "E":
        return "W"
    elif edge == "S":
        return "N"


matches = defaultdict(dict)
start = 0
for id in edges:
    for edge in edges[id]:
        for other_id in edges:
            for edge2 in edges[other_id]:
                same = edge_comp(edges[id][edge], edges[other_id][edge2])
                if id != other_id and same:
                    matches[id][edge] = other_id
                else:
                    if not matches[id].get(edge):
                        matches[id][edge] = None
    if matches[id].get('S') != None and matches[id].get('N') == None and matches[id].get('W') == None and matches[id].get('E') != None:
        start = id


def exact_edge_comp(edge1, edge2):
    if edge1 == edge2:
        return 2
    elif edge1[::-1] == edge2:
        return 1
    else:
        return 0


def replace_char(orig, i, char):
    return orig[0:i] + char + orig[i+1:]


def flipx():
    flip_cell(edges, curr, True)
    flip_cell(matches, curr, True)
    for i in range(0, (len(pixels[curr])//2)):
        for j, row in enumerate(pixels[curr]):
            save = row[len(pixels[curr]) - 1 - i]
            row = replace_char(
                row, len(row) - 1 - i, row[i])
            row = replace_char(row, i, save)
            pixels[curr][j] = row


def flipy():
    flip_cell(edges, curr, False)
    flip_cell(matches, curr, False)

    for i in range((len(pixels[curr])//2)):
        pixels[curr][i], pixels[curr][len(
            pixels[curr]) - 1 - i] = pixels[curr][len(pixels[curr]) - 1 - i], pixels[curr][i]


def flip(e1, e2, edge):
    comp = exact_edge_comp(e1, e2)
    if comp == 1:
        if edge == "N" or edge == "S":
            flipx()
        elif edge == "E" or edge == "W":
            flipy()
        return edges[curr][flip_edge(edge)]
    elif comp == 0:
        if exact_edge_comp(edges[curr][edge], e2) != 0:
            if edge == "N" or edge == "S":
                flipy()
            else:
                flipx()
            if exact_edge_comp(edges[curr][edge], e2) == 1:
                if edge == "N" or edge == "S":
                    flipx()
                else:
                    flipy()
        return edges[curr][flip_edge(edge)]


def rotate():
    rotate_cell(edges, curr)
    rotate_cell(matches, curr)
    pixels[curr] = [''.join(ele) for ele in list(
        map(list, list(zip(*pixels[curr][::-1]))))]


def transform_cell(curr, y, x, done, matches, edges):
    for cell in done:
        for edge in done[cell]:
            if done[cell][edge] == curr:

                e1 = edges[curr][flip_edge(edge)]
                e2 = edges[cell][edge]

                comp = exact_edge_comp(e1, e2)
                while comp != 2:
                    e1 = flip(e1, e2, edge)
                    while exact_edge_comp(e1, e2) == 0:
                        rotate()
                        e1 = edges[curr][flip_edge(edge)]
                    comp = exact_edge_comp(e1, e2)


def move(x, y, dir):
    if edge == "N":
        return x, y - 1
    elif edge == "S":
        return x, y + 1
    elif edge == "E":
        return x + 1, y
    elif edge == "W":
        return x - 1, y


size = int(math.sqrt(len(edges)))
img = [['' for _ in range(size)] for _ in range(size)]

done = {}
pos = {}
q = []
q.append(start)

while len(q) > 0:
    x = y = 0
    curr = q.pop()
    for cell in done:
        for edge in done[cell]:
            if done[cell][edge] == curr:
                x, y = move(*pos[cell], edge)

    transform_cell(curr, y, x, done, matches, edges)
    done[curr] = matches[curr]
    pos[curr] = (x, y)

    if img[y][x] == '':
        img[y][x] = pixels[curr]

    for edge in done[curr]:
        if done[curr][edge] != None and done[curr][edge] not in done:
            q.append(matches[curr][edge])


monster = ['..................#.','#....##....##....###','.#..#..#..#..#..#...']
monsters = [[0]]*8
for i in range(len(monsters)):
    if i == 4:
        new = [0]*len(monster)
        for j, row in enumerate(monster):
            new[j] = row[::-1]
        monster = new

    monsters[i] = monster
    monster = list(zip(*monster[::-1]))


new_img = [['.' for _ in range(size)] for _ in range(size)]
for x, row in enumerate(img):
    for y, cell in enumerate(row):
        new = [['.' for _ in range(len(cell)-2)] for _ in range(len(cell)-2)]

        for i in range(1, len(cell[0])-1):
            for j in range(1, len(cell[0])-1):
                new[i-1][j-1] = cell[i][j]
        for i, row in enumerate(new):
            new[i] = ''.join(row)

        new_img[x][y] = new


final = ['.' for _ in range(len(new_img[0][0])*size)]
offset = 0
for row in new_img:
    for i in range(len(row[0])):
        r = []
        for cell in row:
            r.append(cell[i])
        final[offset+i] = ''.join(r)
    offset += len(new_img[0][0])

count = 0

final = [''.join(s) for s in list(zip(*final[::-1]))]
for i, row in enumerate(final):
    for j, col in enumerate(row):
        for mon in monsters:
            found = True
            candidate = []
            for y in range(len(mon)):
                for x in range(len(mon[y])):
                    if mon[y][x] == '#':
                        if 0 <= i+y < len(final) and 0 <= j+x < len(final[0]) and final[i+y][j+x] == '#':
                            found = True
                            candidate.append((i+y, j+x))
                        else:
                            found = False
                            break
                if not found:
                    break
            if found:
                count += 1

print(count)
print(sum(s.count('#') for s in final) - (count * 15))

print(time.time() - start_time)
