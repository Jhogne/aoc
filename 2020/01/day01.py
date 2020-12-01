with open('input.txt', 'r') as f:
    input = f.read().splitlines()

values = {int(i) : True for i in input}

for v in values.keys():
    if(values.get(2020 - v)):
        print("Part 1: {}".format(v * (2020 - v)))
    for v2 in values.keys() :
        if(values.get(2020 - v - v2)):
            print("Part 2: {}".format(v * v2 * (2020 - v -v2)))
