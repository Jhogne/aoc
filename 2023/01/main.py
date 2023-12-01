import re

with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def p1():
    total = 0
    for line in lines:
        matches = re.findall(r"\d", line)
        total += int(matches[0]+matches[-1])
    return total

def p2():
    total = 0
    for line in lines:
        matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        i = ""
        for x in matches[0], matches[-1]:
            if x.isdigit():
                i += x
            else:
                i += str(digits.index(x)+1)
        total += int(i)
    return total

print(p1())
print(p2())
