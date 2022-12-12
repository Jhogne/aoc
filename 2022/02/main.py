with open('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()

p1 = 0
p2 = 0
S1 = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
S2 = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}
for game in lines:
    p1 += S1[game]
    p2 += S2[game]

print(p1)
print(p2)


