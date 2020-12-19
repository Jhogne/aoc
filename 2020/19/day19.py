import regex

with open('input.txt', 'r') as f:
    rules, msgs = f.read().strip().split('\n\n')

rules1 = dict([rule.split(': ') for rule in rules.splitlines()])

rules2 = rules1.copy()
rules2['8'] = "(?<eight> 42 | 42 (?&eight) )"
rules2['11'] = "(?<eleven> 42 31 | 42 (?&eleven) 31 )"

def rule_to_regex(num, rules):
    if num in (")", "(?<eight>", "(?&eight)", "(?<eleven>", "(?&eleven)") or num.startswith("\""):
        return num.replace('\"', "")
    terms = rules[num].split(" | ")
    # Call rule_to_regex for each value in term and put in a string
    res = ["".join(rule_to_regex(v, rules) for v in vals.split(" "))
           for vals in terms]
    return "(" + "|".join(res) + ")"

p1 = regex.compile(rule_to_regex('0', rules1))
p2 = regex.compile(rule_to_regex('0', rules2))
print("Part 1:", sum([bool(p1.fullmatch(msg)) for msg in msgs.split('\n')]))
print("Part 2:", sum([bool(p2.fullmatch(msg)) for msg in msgs.split('\n')]))
