from itertools import combinations

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

def is_valid(nums):
    if all(0 < i - j < 4 for i, j in zip(nums, nums[1:])):
        return True
    if all(0 < j - i < 4 for i, j in zip(nums, nums[1:])):
        return True

p1, p2 = 0, 0
for l in lines:
    nums = [int(n) for n in l.split()]

    if is_valid(nums):
        p1 += 1

    for nums in combinations(nums, len(nums)-1):
        if is_valid(nums):
            p2 += 1
            break

print(p1)
print(p2)
