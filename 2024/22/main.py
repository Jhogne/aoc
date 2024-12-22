from collections import defaultdict

with open('real.in', 'r') as f:
    lines = [int(x) for x in f.read().strip().splitlines()]

def secret(n):
    n ^= n * 64
    n %= 16777216

    n ^= n // 32
    n %= 16777216

    n ^= n * 2048
    n %= 16777216

    return n

p1 = 0
prices = []
for n in lines:
    price = [n % 10]
    for _ in range(2000):
        n = secret(n)
        price.append(n%10)
    change = [j-i for i, j in zip(price[:-1], price[1:])]
    prices.append((price, change))
    p1 += n

diffvalues = defaultdict(lambda: 0)
for j,(price,change) in enumerate(prices):
    seen = set()
    for i in range(len(change)-4):
        seq = tuple(change[i:i+4])
        if seq not in seen:
            diffvalues[seq] += price[i+4]
            seen.add(seq)

print(p1)
print(max(diffvalues.values()))

