with open('input.txt', 'r') as f:
    lines = [int(l) for l in f.read().splitlines()]

# Part 1
lines.sort()
jolt1 = 0
jolt3 = 1 # Since the last adapter and the device always differs by three
last = 0
for i in lines:
    if(i - last == 1):
        jolt1 += 1
    elif(i - last == 3):
        jolt3 += 1
    last = i

# Part 2
device = last + 3 

chunks = [lines[i:i+3] for i in range(len(lines)-2)]
removable = []
if lines[1] <= 3:
    removable.append((0,lines[0],lines[1]))

for a,b,c in chunks:
    if c - a <= 3:
        removable.append((a,b,c))

if device - lines[-2] <= 3:
    removable.append((lines[-2],lines[-1],device))

removable_pop_prev = []
previous = removable[0][0]
for pre,curr,post in removable[1:]:
    if post - previous <= 3:
        removable_pop_prev.append(curr)
    previous = pre

count = 2
two_removable_before = False
for (pre,curr,_),prev_seen in zip(removable, [x[1] for x in [(0,0,0)] + removable]):
    if curr in removable_pop_prev or pre != prev_seen:
        if pre == prev_seen and two_removable_before:
            count += 3 * count / 4 # Do not add the cases where previous two are removed 
        else:
            count *= 2
    else:
        count += (count // 2) - 1 # Not the case where previous two are removed
    two_removable_before = curr in removable_pop_prev

print("Part 1:",jolt1*jolt3)
print("Part 2:",int(count))
