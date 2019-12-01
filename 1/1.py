import math

part2 = False
msg = "Part2: " if part2 else "Part1: "

with open('1.txt', 'r') as f:
    input = f.read().splitlines()

sum = 0
for i in input:
    fuel = math.floor(int(i)/3) - 2
    if(fuel > 0): 
        sum+= fuel
        if(part2): input.append(fuel) 
print(msg + str(sum))