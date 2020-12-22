with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n\n')

player1 = [int(c) for c in lines[0].splitlines()[1:]]
player2 = [int(c) for c in lines[1].splitlines()[1:]]

def combat(d1, d2, rec):
    seen = set()
    while len(d1) > 0 and len(d2) > 0:
        if (tuple(d1), tuple(d2)) in seen:
            return True

        seen.add((tuple(d1), tuple(d2)))
        c1, c2 = d1.pop(0), d2.pop(0)
        player1_won = c1 > c2
        if rec and c1 <= len(d1) and c2 <= len(d2):
            player1_won = combat(d1[:c1], d2[:c2], True)

        if player1_won:
            d1 += [c1, c2]
        else:
            d2 += [c2, c1]
    return len(d1) > 0

def winner_score(rec):
    deck1, deck2 = player1.copy(), player2.copy()
    winner = deck1 if combat(deck1, deck2, rec) else deck2
    return sum(i*c for i, c in enumerate(winner[::-1], start=1))

print("Part 1:", winner_score(False))
print("Part 2:", winner_score(True))
