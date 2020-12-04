import re

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')

passports = list(map(lambda x: re.split('\n| ', x), data))

part1 = 0
part2 = 0
for p in passports:
    if len(p) == 8 or (len(p) == 7 and not any('cid' in s for s in p)):
        part1 += 1
        valid = True
        for item in p:
            field,val = item.split(':')
            if field == 'byr':
                valid = 1920 <= int(val) <= 2002
            elif field == 'iyr':
                valid = 2010 <= int(val) <= 2020
            elif field == 'eyr':
                valid = 2020 <= int(val) <= 2030
            elif field == 'hgt':
                if('in' in val):
                    valid = 59 <= int(val[:-2]) <= 76
                elif('cm' in val):
                    valid = 150 <= int(val[:-2]) <= 193
                else:
                    valid = False
            elif field == 'hcl':
                valid = re.search("#[A-Fa-f0-9]{6}", val)
            elif field == 'ecl':
                valid = val in ['amb','blu','brn','gry','grn','hzl','oth']
            elif field == 'pid':
                valid = len(val) == 9 and val.isnumeric()
            if not valid:
                break
        if(valid):
            part2 += 1
            
print("Part 1:", part1)
print("Part 2:", part2)