sum = [0]*2
for c in range(264360, 746325):
    i = [int(x) for x in str(c)]
    if i != sorted(i):
        continue
    alreadyValid = [False, False]
    for digit in i:
        seq = i.count(digit)
        if seq == 2 and not alreadyValid[0]:
            sum[1] += 1
            alreadyValid[0] = True
        if seq >= 2 and not alreadyValid[1]:
            sum[0] += 1
            alreadyValid[1] = True
print("Part 1: " + str(sum[0]))
print("Part 2: " + str(sum[1]))
