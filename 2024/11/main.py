from functools import lru_cache

with open('real.in', 'r') as f:
    line = [int(x) for x in f.read().split()]

@lru_cache(maxsize=100000)
def blink(d,its):
    if its == 0:
        return 1

    elif d == 0:
        return blink(1,its-1)
    elif len(str(d)) % 2 == 0:
        d = str(d)
        first = int(d[:len(d)//2])
        snd =  int(d[len(d)//2:])
        return blink(first, its-1) + blink(snd, its-1)
    else:
        return blink(d * 2024, its-1)

print(sum(blink(d,25) for d in line))
print(sum(blink(d,75) for d in line))
