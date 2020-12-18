import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def left_precedence(expr):
    if expr[1].isdigit():
        return expr[2:], int(expr[1])
    elif expr[1] == '(':
        return eval(expr[2:], left_precedence)

def eval_add(expr):
    _, tot, expr = re.split(r'(\d+)',expr, maxsplit=1)
    tot = int(tot)
    if len(expr) > 0 and expr[0] == '+':
        expr, inc = plus_precedence(expr)
        tot += inc
    return expr, tot

def plus_precedence(expr):
    if expr[1].isdigit():
        return eval_add(expr[1:])
    elif expr[1] == '(':
        new_expr, tot = eval(expr[2:], plus_precedence)
        return eval_add(str(tot) + new_expr)

def eval(expr, right_term):
    expr, tot = right_term(' ' + expr)
    while len(expr) > 0:
        if expr[0] == '+':
            expr, inc = right_term(expr)
            tot += inc
        elif expr[0] == '*':
            expr, inc = right_term(expr)
            tot *= inc
        elif expr[0] == ')':
            return expr[1:], tot
    return tot

p1 = p2 = 0
for line in lines:
    p1 += eval(line.replace(' ', ''), left_precedence)
    p2 += eval(line.replace(' ', ''), plus_precedence)

print("Part 1:", p1)
print("Part 2:", p2)
