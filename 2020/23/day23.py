import time
start = time.time()

test = [3,8,9,1,2,5,4,6,7]
cups = [6,4,3,7,1,9,2,5,8]


cups = cups + list(range(max(cups)+1,1000000+1))

MAX = max(cups)
def move(cups, current):
    a = cups[current]
    b = cups[a]
    c = cups[b]

    if current > 1:
        dest = current - 1
    else:
        dest = MAX

    while dest == a or dest == b or dest == c:
        if dest > 1:
            dest = dest - 1
        else:
            dest = MAX

    tmp_dest = cups[dest]
    tmp_c = cups[c]
    cups[dest] = a
    cups[c] = tmp_dest
    cups[current] = tmp_c

    

ring = {}
for i in range(len(cups)):
    ring[cups[i]] = cups[(i+1) % len(cups)]

current = cups[0]
for i in range(10000000):
    move(ring, current)
    current = ring[current]

n = ring[1]
nn = ring[n]
print(n * nn)

print(time.time() - start)