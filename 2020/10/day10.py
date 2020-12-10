with open('input.txt', 'r') as f:
    jolts = [int(l) for l in f.read().splitlines()]

jolts.append(0)
jolts.sort()
jolts.append(jolts[-1]+3)

# Part 1
jolt1 = 0
jolt3 = 0
last = 0
for i in jolts:
    if(i - last == 1):
        jolt1 += 1
    elif(i - last == 3):
        jolt3 += 1
    last = i

# Part 2
# 1. Find all removable adapters
chunks = [jolts[i:i+3] for i in range(len(jolts)-2)]
removable = []
for a,b,c in chunks:
    if c - a <= 3:
        removable.append((a,b,c))

# 2. Find adapters that can be removed when the previous removable adapter is removed
removable_without_prev = []
new_pre = removable[0][0]
for pre,curr,post in removable[1:]:
    if post - new_pre <= 3:
        removable_without_prev.append(curr)
    new_pre = pre

# Count the number of ways to remove adapters and still have a valid sequence
count = 2
two_removable_before = False
for (pre,curr,_),prev_seen in zip(removable, [0]+[x[1] for x in removable]):
    if curr in removable_without_prev or pre != prev_seen:
        if pre == prev_seen and two_removable_before:
            count += 3 * count / 4 # Do not add the cases where previous two are removed 
        else:
            count *= 2
    else:
        count += (count // 2) - 1 # Not the one case where previous two are removed
    two_removable_before = curr in removable_without_prev

print("Part 1:",jolt1*jolt3)
print("Part 2:",int(count))
