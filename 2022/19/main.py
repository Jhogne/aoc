from functools import lru_cache
import re
import math

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

bps = []
for bp in lines:
    nums = [int(x) for x in re.findall(r"\d+", bp)]
    bps.append({
        "o": nums[1],
        "c": nums[2],
        "ob": (nums[3], nums[4]),
        "geo": (nums[5], nums[6]),
        "maxore": max(nums[1], nums[2], nums[3], nums[5]),
        })

@lru_cache(maxsize=None)
def max_ore(time, ore, clay, obsidian, orebots, claybots, obsidbots):
    if time == 1:
        return 0 

    orecost, obsidcost = BP["geo"]
    if orebots >= orecost and obsidbots >= obsidcost:
        return sum(range(time+1))

    time -= 1
    nore, nclay, nobsidian = ore + orebots, clay+claybots, obsidian+obsidbots

    if ore >= orecost and obsidian >= obsidcost:
        return time + max_ore(time,
                              nore-orecost, nclay, nobsidian-obsidcost, 
                              orebots, claybots, obsidbots)

    candidates = []
    orecost, claycost = BP["ob"]
    if ore >= orecost and clay >= claycost:
        candidates.append(max_ore(time, 
                                  nore-orecost, nclay-claycost, nobsidian, 
                                  orebots, claybots, obsidbots+1))

    if ore >= BP["o"] and orebots < BP["maxore"]:
        candidates.append(max_ore(time, 
                                  nore-BP["o"], nclay, nobsidian, 
                                  orebots+1, claybots, obsidbots))

    if ore >= BP["c"] and claybots < claycost:
        candidates.append(max_ore(time, 
                                  nore-BP["c"], nclay, nobsidian, 
                                  orebots, claybots+1, obsidbots))

    if ore < BP["maxore"] or clay < claycost or obsidian < obsidcost:
        candidates.append(max_ore(time, 
                                  nore, nclay, nobsidian, 
                                  orebots, claybots, obsidbots))

    return max(candidates)

p1, p2 = 0, 1
for (i,BP) in enumerate(bps):
    max_ore.cache_clear()
    p1 += (i+1)*max_ore(24, 0, 0, 0, 1, 0, 0)
    if i < 3:
        p2 *= max_ore(32, 0, 0, 0, 1, 0, 0)

print(p1)
print(p2)
