from itertools import product
import pyparsing

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def get_next(expr):
    #print('Get next',expr)
    if expr[1].isdigit():
        return eval_add(expr[1:])
    elif expr[1] == '(':
        new_expr, tot = eval(expr[2:])
        return eval_add(str(tot)+new_expr)

# 1 + 2 * 3 + 4 * 5 + 6
def eval_add(expr):
    start = 0
    for c in expr:
        if c.isdigit():
            start += 1
        else:
            break
    tot = int(expr[0:start])
    expr = expr[start:]
    while len(expr) > 0 and expr[0] == '+':
        expr,inc = get_next(expr)
        tot += inc
    return expr,tot

def eval(expr):
    expr,tot = get_next('0'+expr)
    while len(expr) > 0:
        #print(expr,tot)
        if expr[0] == '+':
            expr, inc = get_next(expr)
            tot += inc
        elif expr[0] == '*':
            expr, inc = get_next(expr)
            tot *= inc
        elif expr[0] == ')':
            return expr[1:],tot
    return '',tot


#print(eval("(1+2)*(2+3)+1")) 
tot = 0
for line in lines:
    tot += eval(line.replace(' ',''))[1]



print("Part 1:",tot)
print("Part 2:")
