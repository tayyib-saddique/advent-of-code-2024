import os, sys
sys.path.append(os.path.abspath('./'))

from part1 import reports, is_gradually_ascending, is_gradually_descending

def is_safe_after_removal(list):
    if is_gradually_ascending(list):
        return True
    elif is_gradually_descending(list):
        return True
    else:
        for index in range(len(list)): 
            # iterates over index in a given list, generates temp list and then removes value at indexed location
            new_list = list[:]
            new_list.pop(index)
            if is_gradually_ascending(new_list) or is_gradually_descending(new_list):
                return True

counts = 0
for report in reports:
    if is_safe_after_removal(report):
        counts += 1

print(counts)