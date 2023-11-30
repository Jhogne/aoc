from functools import lru_cache
import re
import math

with open('input.txt', 'r') as f:
    lines = list(map(int,f.read().splitlines()))

#lines = list(map(int,"""1
#2
#-3
#3
#-2
#0
#4""".splitlines()))

#lines = [(False,l) for l in lines]
#
#changed = True
#while changed:
#    changed = False 
#    for i,(moved,n) in enumerate(lines):
#        if not moved:
#            del lines[i]
#            pos = (i+n)%len(lines)
#            lines = lines[:pos]+[(True,n)]+lines[pos:]
#            changed = True
#
#            break
#        
#zero = lines.index((True,0))
#num1, num2, num3 = lines[(zero+1000)%len(lines)][1], lines[(zero+2000)%len(lines)][1], lines[(zero+3000)%len(lines)][1]
#print(num1, num2, num3)
#print(num1 + num2 + num3)

#lines = [(False,l*811589153) for l in lines]
#working = lines.copy()
#
#changed = True
#while changed:
#    changed = False 
#    for i,(_,n) in enumerate(lines):
#        i, (_, n) = working.index(False, n)
#        del working[i]
#        pos = (i+n)%len(working)
#        working = working[:pos]+[(True,n)]+working[pos:]
#        changed = True
#
#        break
#print(working)
#print(lines)
#        
#zero = working.index((False,0))
#num1, num2, num3 = lines[(zero+1000)%len(lines)][1], lines[(zero+2000)%len(lines)][1], lines[(zero+3000)%len(lines)][1]
#print(num1, num2, num3)
#print(num1 + num2 + num3)


#lines = [(False,l) for l in lines]
lines = [l*811589153 for l in lines]
lines = [l for l in lines]
order = list(range(len(lines)))
for k in range(10):
    print(k)
    #norder = []

    for j in range(len(order)):
        i = order[j]
        n = lines[i]
        del lines[i]
        pos = (i+n)%len(lines)
        lines = lines[:pos]+[n]+lines[pos:]
        #norder.append(pos)
        lo,hi = min(i, pos), max(i,pos)
        if pos - i > 0:#(n > 0 and i+n < len(lines)) or i + n < 0:
            diff = -1
        else:
            diff = 1
        #print(i,pos,n,diff)
        order = [(n+diff)%len(lines) if lo<=n<=hi else n for n in order]
        order[j] = pos
        #norder = [(n-1)%len(lines) if lo<=n<=hi else n for n in norder]
    #order = norder
        
zero = lines.index(0)
num1, num2, num3 = lines[(zero+1000)%len(lines)], lines[(zero+2000)%len(lines)], lines[(zero+3000)%len(lines)]
print(num1, num2, num3)
print(num1 + num2 + num3)


