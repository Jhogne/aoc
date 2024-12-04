with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()


xmas = [((0,0), 'X'), ((1,0),'M'), ((2,0), 'A'), ((3,0), 'S')]
xmas_diag = [((0,0), 'X'), ((1,1),'M'), ((2,2), 'A'), ((3,3), 'S')]
mas = [((0,0), 'M'), ((0, 2), 'M'), ((1,1), 'A'), ((2,0), 'S',), ((2,2), 'S')]

def find_word(word):
    def valid(y,x):
        for (dy,dx),c in word:
            if y + dy >= len(lines) or x + dx >= len(lines[0]):
                return False
            if lines[y+dy][x+dx] != c:
                return False
        return True

    tot = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if valid(i,j):
                tot += 1
    return tot

p1 = p2 = 0
for _ in range(4):
    p1 += find_word(xmas)
    p1 += find_word(xmas_diag)
    p2 += find_word(mas)
    lines = [''.join(x) for x in list(zip(*lines[::-1]))]

print(p1)
print(p2)
