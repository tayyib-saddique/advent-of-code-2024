import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(5)
parts = data.split("\n\n")

ordering_rules = [list(map(int, line.split('|'))) for line in parts[0].splitlines()]
page_numbers = [list(map(int, line.split(','))) for line in parts[1].splitlines()]

safe = []
for page in page_numbers:
    valid = True # restarts for each page 
    print(page)
    for i, j in zip(page, page[1:]):
        rule_found = False # restarts for each pair of numbers
        for rule in ordering_rules:
            if i == rule[0] and j == rule[1]:
                # if i and j match a given rule in the list of rules, rule_found becomes true and for loop breaks
                rule_found = True
                break
        # if rule_found is false, then the page is not valid and the loop breaks
        if not rule_found:
            valid = False
            break
    if valid:
        safe.append(page)
print(safe)

total = 0
for page in safe:
    middle_index = len(page) // 2
    middle_page = page[middle_index]
    
    total += middle_page

print(total)