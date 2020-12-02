import re

with open('input.txt', 'r') as f:
    input = f.read().splitlines() 

valid1 = 0
valid2 = 0
for i in input:
    lo, hi, key, pwd = re.split("-|: | " , i)
    lo, hi = int(lo), int(hi)
    if lo <= pwd.count(key) <= hi:
        valid1 += 1

    if (pwd[lo - 1] == key) ^ (pwd[hi - 1] == key):
        valid2 += 1
   
print("Part 1:",valid1)
print("Part 2:",valid2)