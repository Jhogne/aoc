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
# Count the number of ways to remove adapters from the full sequence 
# No more than two subsequent adapters can be removed at the same time, minimal example:
# 1 2 3 4 5
# if 2 3 4 are removed causes the difference to be too large (5 - 1 = 4; 4 > 3)

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

# 3. Count the number of ways to remove adapters and still have a valid sequence
count = 2 # First removable always causes two cases (Choose it or not)
two_removable_before = False
# Iterate over all removable adapters, aswell as the removable adapter to it's left
for (pre,curr,_),prev_rem in zip(removable[1:], [x[1] for x in removable]):
    # If curr is removable, and the two predecessors are also removable.
    if pre == prev_rem and two_removable_before: 
        # Double, but without the quarter of the cases where previous two are removed 
        # prev1 prev2 < ok
        # _     prev2 < ok
        # prev1 _     < ok
        # _     _     < not ok since max 2 subsequent adapters can be removed
        count += 3 * count / 4 
    # Otherwise, if predecessor isn't removable, or only the immidiate predecessor is removable
    elif pre != prev_rem or curr in removable_without_prev:
        count *= 2 # The current adapter is either added to the sequence, or not, doubling the cases
    two_removable_before = curr in removable_without_prev

print("Part 1:",jolt1*jolt3)
print("Part 2:",int(count))
