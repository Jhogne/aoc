import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

modules = {}
invs = set()
for l in lines:
    f, dest = l.split(" -> ")
    dest = dest.split(", ")
    t = None
    if f.startswith("%"):
        t = [f[0], False] # off = False, on = True
        f = f[1:]
    elif f.startswith("&"):
        t = [f[0], {}]
        f = f[1:]
        invs.add(f)

    modules[f] = (dest, t)


for m in modules:
    for dest in modules[m][0]:
        if dest in invs:
            modules[dest][1][1][m] = False

def flip_flop_states():
    states = []
    for m in modules:
        if modules[m][1] and modules[m][1][0] == '%':
            states.append(modules[m][1][1])
    return tuple(states) 

# low = False
# high = True
def press_button():
    q = [("broadcaster", False)]
    hi, lo = 0, 1
    while q:
        at, high = q.pop(0)
    
        dests, t = modules[at]
        if t == None:
            pass
        elif t[0] == "%":
            if high:
                continue
            t[1] = not t[1]
            high = t[1]
        elif t[0] == "&":
            if all(t[1].values()):
                high = False
            else:
                high = True
    
        for d in dests:
            if high:
                hi += 1
            else:
                lo += 1

            shigh = "high" if high else "low"
            if d not in modules:
                #print(at + "-" + shigh +"->" + d)
                continue

            if modules[d][1] and modules[d][1][0] == "&":
                modules[d][1][1][at] = high
 
            shigh = "high" if high else "low"
            #print(at + "-" + shigh +"->" + d)
            if d == "rx" and not high:
                return True
            q.append((d, high))

    return False

#hi, lo = press_button()
#seen = {flip_flop_states()}
#
#pressed = 1
#for i in range(999):
#
#    print(pressed)
#    hi1, lo1 = press_button()
#    #states = flip_flop_states()
#    #print(states)
#    #if states in seen:
#    #    break
#    hi += hi1
#    lo += lo1
#    pressed += 1
#
#print(hi * lo)
#

presses = 0
while not press_button():
    if presses % 1000 == 0:
        print(presses)
    print(flip_flop_states())
    presses += 1

print(presses)
