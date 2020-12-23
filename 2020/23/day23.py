#cups = [3, 8, 9, 1, 2, 5, 4, 6, 7] # Testing 
cups = [6, 4, 3, 7, 1, 9, 2, 5, 8]  # Input 

def play(ring, rounds):
    current = cups[0] 
    MAX = max(ring)
    for _ in range(rounds):
        a = ring[current]
        b = ring[a]
        c = ring[b]

        dest = current - 1 if current != 1 else MAX
        while dest == a or dest == b or dest == c:
            dest = dest - 1 if dest != 1 else MAX

        tmp_c = ring[c]
        ring[c] = ring[dest]
        ring[dest] = a
        ring[current] = tmp_c

        current = ring[current]

def init_ring():
    # Create list representing linked list, where [idx:value] -> [cup:next]
    # The first element is irrelevant, as the cups are indexed from 1

    ring = [i+1 for i in range(len(cups)+1)]

    for i in range(len(cups)):
        if i + 1 == len(cups):
            ring[cups[i]] = cups[0] 
        else:
            ring[cups[i]] = cups[i+1]

    ring[cups[-1]] = cups[0]
    return ring

ring1 = init_ring()
play(ring1, 100)

p1 = ''
curr = ring1[1]
while curr != 1:
    p1 += str(curr)
    curr = ring1[curr]

ring2 = init_ring()
ring2[cups[-1]] = max(cups) + 1 # Remove the initial loop 
ring2 += list(range(len(ring2) + 1, 1000000 + 2)) # +2 since we want inclusive and indexed from 1
ring2[-1] = cups[0]
play(ring2, 10000000)

n = ring2[1]
nn = ring2[n]

print("Part 1:",p1)
print("Part 2:",n * nn)

