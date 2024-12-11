import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(5)
parts = data.split("\n\n")

ordering_rules = [list(map(int, line.split('|'))) for line in parts[0].splitlines()]
page_numbers = [list(map(int, line.split(','))) for line in parts[1].splitlines()]

unsafe = []
for page in page_numbers:
    valid = True # restarts for each page 
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

    if not valid:
        unsafe.append(page)

ordering_dict = {}
for first, second in ordering_rules:
    if first not in ordering_dict:
        ordering_dict[first] = set()
    ordering_dict[first].add(second)


for page in unsafe:
    swapped = True
    while swapped: # while loop to ensure swaps continue until the entire page has no violations
        swapped = False
        for i, j in zip(page, page[1:]): 
            rule_found = False
            # rule_found is used to identify where swaps need to be made
            for rule in ordering_rules:
                if i == rule[0] and j == rule[1]:
                    rule_found = True
                    break
            if not rule_found:
                index_i = page.index(i)
                index_j = page.index(j)
                print(f'Original page {page}')
                page[index_i], page[index_j] = page[index_j], page[index_i]
                print(f'Swapped {page}')
                swapped = True  # swap is set to true to recheck for further violations
                
def retrieve_total(pages):
    total = 0
    for page in pages:
        middle_index = len(page) // 2
        middle_page = page[middle_index]
        total += middle_page
    return total

print(retrieve_total(unsafe))