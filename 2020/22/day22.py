from collections import deque

with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n\n')

player1 = deque([int(c) for c in lines[0].splitlines()[1:]])
player2 = deque([int(c) for c in lines[1].splitlines()[1:]])

def combat(d1, d2):
    while len(d1) > 0 and len(d2) > 0:
        c1, c2  = d1.popleft(), d2.popleft()
        if c1 > c2:
            d1.extend([c1,c2])
        else:
            d2.extend([c2,c1])
    return d1 if len(d1) > 0 else d2

def rec_combat(d1, d2):
    seen = set()
    while len(d1) > 0 and len(d2) > 0:
        if (tuple(d1), tuple(d2)) in seen:
            return True

        seen.add((tuple(d1), tuple(d2)))
        c1, c2 = d1.popleft(), d2.popleft()

        if c1 <= len(d1) and c2 <= len(d2):
            c1_won = rec_combat(deque(list(d1)[:c1]), deque(list(d2)[:c2]))
            first, second, deck = (c1, c2, d1) if c1_won else (c2, c1, d2)
        else:
            first, second, deck = (c1, c2, d1) if c1 > c2 else (c2, c1, d2)
        deck.extend([first, second])
    return len(d1) > 0

winner = combat(player1.copy(), player2.copy())
p1 = sum(i*c for i, c in enumerate(list(winner)[::-1], start=1))

winner = player1 if rec_combat(player1, player2) else player2
p2 = sum(i*c for i, c in enumerate(list(winner)[::-1], start=1))

print("Part 1:", p1)
print("Part 2:", p2)
