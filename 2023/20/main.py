import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict
import sys

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

modules = {}
imodules = defaultdict(lambda: [])
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

    for d in dest:
        imodules[d].append(f)
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
        if at == "rx" and not high:
            print("yay!")
    
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
                print(at + "-" + shigh +"->" + d)
                continue

            if modules[d][1] and modules[d][1][0] == "&":
                modules[d][1][1][at] = high
 
            shigh = "high" if high else "low"
            print(at + "-" + shigh +"->" + d)
            q.append((d, high))

    return hi, lo


def reverse(q, sent):
    if not q:
        return {}
    at, high = q.pop(0)
    if at == "broadcaster":
        assert not high
        return {}
    fs = imodules[at]
    if at not in modules:
        t = None
    else:
        _, t = modules[at]
    print(at, high)
    flipflops = {}
    if t == None:
        print(at)
        for f in fs:
            flipflops |= reverse(q + [(f, high)], sent|{(at, high, f)})# | flipflops
        return flipflops
    elif t[0] == "%":
        high = not high
        flipflops[at] = high
        for f in fs:
            if (at, False, f) not in sent:
                flipflops |= reverse(q + [(f, False)], sent|{(at, False, f)})# | flipflops
        return flipflops
    elif t[0] == "&":
        if not high:
            for f in fs:
                flipflops |= reverse(q + [(f, True)], sent|{(at, True, f)})# | flipflops
            return flipflops
        else:
            if len(fs) == 1:
                flipflops |= reverse(q + [(fs[0], False)] , sent|{(at, high, fs[0])})# | flipflops
                return flipflops 
            print("what to do?")
            print(at, fs)
            assert False

    print("nothing to do", at, t)
    assert False
#hi, lo = press_button()
#seen = {flip_flop_states()}
#
#pressed = 1
#for i in range(999):
#    hi1, lo1 = press_button()
#    #states = flip_flop_states()
#    #print(states)
#    #if states in seen:
#    #    break
#    hi += hi1
#    lo += lo1
#    pressed += 1


#config = {'gt': False, 'pp': False, 'ps': True, 'rf': True, 'nm': True, 'gv': False, 'gd': True, 'gc': True, 'pv': True, 'gn': True, 'tn': True, 'pf': True, 'xz': False, 'bg': True, 'rq': False, 'jl': True, 'jn': True, 'nz': True, 'hh': True, 'ms': True, 'rb': True, 'mt': True, 'sx': True, 'ts': False, 'fp': False, 'rp': False, 'fz': True, 'zq': True, 'xm': False, 'cs': False, 'vx': True, 'td': True, 'kz': False, 'jb': True, 'gb': True, 'gh': True, 'fr': False, 'ks': False, 'df': False, 'lq': True, 'gq': False, 'vg': True, 'dj': True, 'nl': True, 'ch': True, 'qr': True, 'cc': True, 'lc': False}
#config = {'df': True, 'fr': True, 'vg': True, 'cc': True, 'nl': False, 'dj': True, 'qr': True, 'gq': False, 'lq': True, 'ks': False, 'lc': False, 'ch': True, 'xm': True, 'zq': True, 'fz': True, 'jb': True, 'fp': True, 'vx': True, 'cs': False, 'kz': False, 'td': True, 'rp': False, 'gb': False, 'gh': True, 'xz': True, 'ms': True, 'hh': True, 'nz': True, 'jn': True, 'jl': True, 'sx': True, 'mt': True, 'rb': True, 'rq': False, 'bg': False, 'ts': False, 'gt': True, 'nm': True, 'rf': True, 'ps': True, 'pv': True, 'gc': True, 'gd': True, 'pp': False, 'gv': False, 'pf': True, 'tn': True, 'gn': True}

config = {'df': False, 'fr': False, 'vg': False, 'cc': True, 'nl': False, 'dj': True, 'gq': False, 'lq': True, 'ks': False, 'lc': False, 'qr': True, 'ch': True, 'xm': True, 'zq': False, 'fz': True, 'jb': True, 'fp': False, 'vx': True, 'cs': False, 'kz': False, 'td': True, 'rp': False, 'gb': False, 'gh': True, 'xz': False, 'ms': True, 'hh': False, 'nz': True, 'jn': False, 'jl': True, 'sx': True, 'mt': True, 'rb': False, 'rq': False, 'bg': False, 'ts': False, 'gt': False, 'nm': True, 'rf': True, 'ps': False, 'pv': True, 'gc': True, 'gd': True, 'pp': False, 'gv': False, 'gn': True, 'pf': True, 'tn': True}


#for m in modules:
#    if m in config:
#        modules[m][1][1] = config[m]
#print(modules)
#press_button()
print(reverse([("rx", False)], set()))

#hi, lo = reverse([("rx", False)])
#lo += 1
#for i in range(999):
#    hi1, lo1 = reverse([("rx", False)])
#    lo1 += 1
#    hi += hi1
#    lo += lo1
#
#print(lo, hi)
#print(hi * lo)

#presses = 0
#while not press_button():
#    if presses % 1000 == 0:
#        print(presses)
#    #print(flip_flop_states())
#    presses += 1
#
#print(presses)
