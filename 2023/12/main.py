import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def is_valid(s, start, num):
    if start + num > len(s):
        return False
    if "." in s[start:start+num]:
        return False
    if start + num < len(s) and s[start+num] == "#":
        return False
    return True

def groups(s):
    gs = [[0,0]]
    for c in s:
        if c == "#":
            gs[-1][0] += 1
            continue
        if c == ".":
            gs[-1][0] = 0
        elif c == "?":
            gs[-1][1] += 1
        gs.append([0,0])
    gs = [g for g in gs if g[0]>0]
    return gs

def groups_valid(s,nums):
    damaged_groups = groups(s)
    for num in nums:
        while damaged_groups and num > 0:
            g,qs = damaged_groups[0]
            if num < g:
                break
            del damaged_groups[0]
            num -= g
            if qs == 0:
                break
            num -= qs
    return len(damaged_groups) == 0

def arrangements(springs, nums):
    starts = []
    for i,n in enumerate(nums):
        possible = set()
        for start in range(len(springs)+1):
            if springs[:start].count("#") > sum(nums[:i]):
                continue
  
            if springs[start+n+1:].count("#") > sum(nums[i+1:]):
                continue
  
            if not groups_valid(springs[:start], nums[:i]):
                continue

            if not groups_valid(springs[start+n+1:], nums[i+1:]):
                continue
             
            if is_valid(springs, start, n):
                possible.add(start)
        starts.append((n,possible))
  
    amts = {ls: 1 for ls in starts[-1][1]}
    for l,ss in reversed(starts[:-1]):
        next_amt = {}
        for s in ss:
            amt = 0
            for after in amts:
                if s+l < after and not "#" in springs[s+l+1:after]:
                    amt += amts[after]
            next_amt[s] = amt
        amts = next_amt
    return sum(amts.values())

p1, p2 = 0, 0
for l in lines:
    springs, nums = l.split(' ')
    nums = [int(x) for x in re.findall(r"\d+", nums)]
    p1 += arrangements(springs, nums)

    springs = ((springs + "?") * 5)[:-1]
    nums = nums * 5
    p2 += arrangements(springs, nums)

print(p1)
print(p2)
