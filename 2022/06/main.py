with open('input.txt', 'r') as f:
    line = f.read()

def unique_after_n(n):
    for i in range(n, len(line)):
        if len(set(line[i-n:i])) == n:
            return(i)
 
print(unique_after_n(4)) 
print(unique_after_n(14)) 
