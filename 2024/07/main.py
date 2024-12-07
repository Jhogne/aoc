import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def can_reach_target(target, nums, concat=False):
    if len(nums) == 1:
        return nums[0] == target

    ops = [[nums[0] + nums[1]] + nums[2:], [nums[0] * nums[1]] + nums[2:]]
    if concat:
        ops.append([int(str(nums[0]) + str(nums[1]))] + nums[2:])
    return any(can_reach_target(target, ns, concat) for ns in ops)
    
p1 = p2 = 0
for l in lines:
    ds = [int(x) for x in re.findall(r"\d+", l)]
    target, nums = ds[0], ds[1:]
    if can_reach_target(target, nums):
        p1 += target
    if can_reach_target(target, nums, concat=True):
        p2 += target

print(p1)
print(p2)
