from math import sqrt

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')

# Get the border index of adjacent tile in direction y,x
adjacent_to_edge = {(1, 0): 0, (0, -1): 1, (-1, 0): 2, (0, 1): 3}
# Gets the adjacent tile y,x facing the border with given index
edge_to_adjacent = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

SIZE = int(sqrt(len(data)))
MONSTER = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']
tiles = {}
for d in data:
    rows = d.split('\n')
    id, tile = rows[0][5:9], rows[1:]
    tiles[int(id)] = tile

def get_borders(tile):
    top, bot = tile[0], tile[-1]
    left = "".join([row[0] for row in tile])
    right = "".join([row[-1] for row in tile])
    return [top, right, bot, left]

def get_matches(tile, tiles):
    # Compare the edges of all tiles with all possible edges for given tile.
    # Returns list of ids (or None) of adjacent tiles. Order is [North, East, South, West]

    matches = [None] * 4
    my_boarders = get_borders(tile)
    my_boarders += [b[::-1] for b in my_boarders]

    for other in tiles:
        if tiles[other] == tile:
            continue

        other_borders = get_borders(tiles[other])

        for i, b in enumerate(my_boarders):
            if b in other_borders:
                matches[i % 4] = other

    return matches

def rotate(tile):
    return [''.join(ele) for ele in list(
        map(list, list(zip(*tile[::-1]))))]

def flip(tile):
    new_tile = tile.copy()
    for j, row in enumerate(tile):
        new_tile[j] = ''.join(reversed(row))
    return new_tile

def transform_tile(tile, board, y, x):
    other_tile, other_edge = [], -1

    # Find adjacent (correctly transformed) tile in the board. Use it's border for reference to
    # transform current tile properly.
    for dy, dx in adjacent_to_edge:
        if 0 <= y + dy < SIZE and 0 <= x + dx < SIZE and board[y+dy][x+dx] != None:
            other_tile = board[y+dy][x+dx]
            other_edge = adjacent_to_edge[(dy, dx)]

    assert other_tile != [] and other_edge != -1
    other_boarder = get_borders(other_tile)[other_edge]
    for _ in range(4):
        for _ in range(2):
            my_boarder = get_borders(tiles[tile])[(other_edge + 2) % 4]
            if my_boarder == other_boarder:
                return
            tiles[tile] = flip(tiles[tile])
        tiles[tile] = rotate(tiles[tile])

def assemble_board(start):
    # Initiat with start at the top left of the board:
    # 1. Get next tile
    # 2. Transform it if it isn't the first (as it needs to be used for reference)
    # 3. Add (transformed tile) to board
    # 4. Add all adjacent tiles to queue if they aren't already placed or are waiting to be placed

    q = [(start, 0, 0)]
    board = [[None for _ in range(SIZE)] for _ in range(SIZE)]

    while len(q) > 0:
        curr, y, x = q.pop(0)
        if not (x == 0 and y == 0):
            transform_tile(curr, board, y, x)

        board[y][x] = tiles[curr]
        for i, neighbour in enumerate(get_matches(tiles[curr], tiles)):
            if neighbour == None:
                continue
            dy, dx = edge_to_adjacent[i]
            if board[y+dy][x+dx] == None and (neighbour, y+dy, x+dx) not in q:
                q.append((neighbour, y+dy, x+dx))
    return board

def remove_borders(board):
    # Removes the boarders of each tile in the board
    out = []
    for row in board:
        for y in range(1, len(row[0])-1):
            line = ''
            for col in row:
                for x in range(1, len(col)-1):
                    line += col[y][x]
            out.append(line)
    return out

def is_monster(x, y, image):
    # Checks if position x,y in image is the top left pixel of a monster
    if y + len(MONSTER) > len(image) or x + len(MONSTER[0]) > len(image[0]):
        return False
    for dy, row in enumerate(MONSTER):
        for dx, cell in enumerate(row):
            if cell == '#' and image[y+dy][x+dx] != '#':
                return False
    return True

def count_monsters(image):
    # Counts the monsters in each flip/rotation combination of the image. Assuming all monsters are
    # turned the same way => this will return the number of monsters in the single orientation
    count = 0
    for _ in range(4):
        for _ in range(2):
            for y in range(len(image)):
                for x in range(len(image)):
                    if(is_monster(x, y, image)):
                        count += 1
            image = flip(image)
        image = rotate(image)
    return count


part1 = 1
start = -1
for id, tile in tiles.items():
    matches = get_matches(tile, tiles)
    part1 *= id if sum([x != None for x in matches]) == 2 else 1

    # Start with an arbitrary tile that can fit in top left spot without transforming it.
    if matches[0] == None and matches[1] != None and matches[2] != None and matches[3] == None:
        start = id
assert start != -1

board = assemble_board(start)
image = remove_borders(board)
part2 = sum(row.count('#') for row in image) - \
    (count_monsters(image) * sum(row.count('#') for row in MONSTER))
print("Part 1:", part1)
print("Part 2:", part2)