import regex
import time

start_time = time.time()
with open('input.txt', 'r') as f:
    first, msgs = f.read().strip().split('\n\n')

rules1 = {}
start = {}
for rule in first.split('\n'):
    idx, pattern = rule.split(': ')
    pattern = " " + pattern.replace("\"","") + " "
    rules1[idx] = pattern
    if pattern == ' a ' or pattern == ' b ':
        start[idx] = pattern

rules2 = rules1.copy()
rules2['8'] = "(?<eight> 42 | 42 (?&eight) )"
rules2['11'] = "(?<eleven> 42 31 | 42 (?&eleven) 31 )"


def solve(rules, to_replace):
    keep_updating = True
    while keep_updating:
        new = {}
        for rplc in to_replace:
            for rule in rules:
                updated = regex.sub(
                    f" {rplc} ", f" {to_replace[rplc]} ", rules[rule])
                rules[rule] = updated
                if not regex.search(r"\d", updated):
                    new[rule] = "(" + updated + ")"
        to_replace, keep_updating = new, len(new) != len(rules)

    return len([msg for msg in msgs.split('\n')
                if regex.fullmatch(rules['0'].replace(" ", ""), msg) != None])


print("Part 1:", solve(rules1, start))
print("Part 2:", solve(rules2, start))

print(time.time() - start_time)
