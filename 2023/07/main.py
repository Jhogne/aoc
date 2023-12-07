from itertools import groupby

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def group_hand(hand):
    groups = [''.join(g) for _, g in groupby(sorted(hand))]
    return sorted(groups, key=lambda x: len(x))

def hand_value(groups):
    if len(groups) == 5:
        return '1'
    elif len(groups) == 4:
        return '2'
    elif len(groups) == 3 and len(groups[-1]) == 2:
        return '3'
    elif len(groups) == 3:
        return '4'
    elif len(groups) == 2 and len(groups[-1]) == 3:
        return '5'
    elif len(groups) == 2:
        return '6'
    else:
        return '7'

def score(hands):
    for i,(_,b) in enumerate(sorted(hands)):
         yield (i+1)*b

def p1():
    hs = []
    for l in lines:
        h,b = l.split()
        h = h.translate(str.maketrans("TJQKA","abcde"))
        hs.append((hand_value(group_hand(h))+h, int(b)))

    return sum(score(hs))
   
def p2():
    hs = []
    for l in lines:
        h,b = l.split()
        h = h.translate(str.maketrans("TJQKA","a0cde"))
        groups = group_hand(h)
        for i in range(len(groups)):
            if "0" in groups[i]:
                groups[-1] += groups[i]
                del groups[i]
                break

        hs.append((hand_value(groups)+h, int(b)))
    
    return sum(score(hs))

print(p1())
print(p2())
