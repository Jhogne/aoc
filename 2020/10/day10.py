with open('input.txt', 'r') as f:
    jolts = [int(l) for l in f.read().splitlines()]

jolts.append(0)
jolts.sort()
jolts.append(jolts[-1]+3)

# Part 1
diff1 = 0
diff3 = 0
last = 0
for i in jolts:
    if(i - last == 1):
        diff1 += 1
    elif(i - last == 3):
        diff3 += 1
    last = i

# Part 2
# Construct the sequence from left to right. Each optional doubles the number of 
# possible sequences, except if the two predecessors are optional, because a maximum
# of three optional can be excluded at the same time:
# Minimal example: 1 [2 3 4] 5 => 5 - 1 = 4; 4 > 3
# When the two predecessors are optional the third is no longer optional, therefore the number 
# of cases increases by 7/4 (double - 1/4):
# x... prev1 prev2 _/curr  > (2 cases)
# x... prev1 _     _/curr  > (2 cases)
# x... _     prev2 _/curr  > (2 cases)
# x... _     _       curr  > (1 case)

optional = []
for a,b,c in [jolts[i:i+3] for i in range(len(jolts)-2)]:
    if c - a <= 3:
        optional.append((a,b,c))

count = 2 # First optional always causes two cases (Choose it or not)
pre_pre_is_optional = False
for (pre,_,post),prev_optional in zip(optional[1:], [x[1] for x in optional]):
    if pre == prev_optional and pre_pre_is_optional: 
        count *= 7 / 4 
    else:
        count *= 2 
    pre_pre_is_optional = post - prev_optional <= 3

print("Part 1:",diff1*diff3)
print("Part 2:",int(count))
