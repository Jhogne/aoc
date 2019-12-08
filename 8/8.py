with open('8.txt', 'r') as f:
    string = f.read().strip()
layers = [string[i:i+25*6] for i in range(0, len(string), 25*6)] 

min_zero = min(layers, key=lambda x: x.count('0'))
print('Part 1: ' + str(min_zero.count('1')*min_zero.count('2')))

top_layer = list(layers[0])
for idx, value in enumerate(top_layer):
    if value == '2':
        for other_layer in layers[1:]:
            if other_layer[idx] != '2':
                top_layer[idx] = other_layer[idx]
                break
            
rows = [top_layer[i:i+25] for i in range(0, len(top_layer), 25)]
print('Part 2:')
for row in rows:
    print(''.join(row).replace('0', ' ').replace('1', '█'))