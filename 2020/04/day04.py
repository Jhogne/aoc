import re

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')

part1 = part2 = 0
for d in data:
    pp = re.split(r'\s', d)
    if len(pp) == 8 or (len(pp) == 7 and not any('cid' in field for field in pp)):
        part1 += 1
        valid = True
        for item in pp:
            key,val = item.split(':')
            if key == 'byr':
                valid = 1920 <= int(val) <= 2002
            elif key == 'iyr':
                valid = 2010 <= int(val) <= 2020
            elif key == 'eyr':
                valid = 2020 <= int(val) <= 2030
            elif key == 'hgt':
                if('in' in val):
                    valid = 59 <= int(val[:-2]) <= 76
                elif('cm' in val):
                    valid = 150 <= int(val[:-2]) <= 193
                else:
                    valid = False
            elif key == 'hcl':
                valid = re.search("#[a-f0-9]{6}", val)
            elif key == 'ecl':
                valid = val in ['amb','blu','brn','gry','grn','hzl','oth']
            elif key == 'pid':
                valid = len(val) == 9 and val.isnumeric()
            if not valid:
                break
        if(valid):
            part2 += 1
            
print("Part 1:", part1)
print("Part 2:", part2)