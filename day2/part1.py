import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(2)
reports = [[int(x) for x in line.split()] for line in data.split('\n')[:-1]]

def is_gradually_ascending(list):
    for i, j in zip(list, list[1:]):
        if i >= j or abs(i - j) > 3:
            return False
    return True

def is_gradually_descending(list):
    for i, j in zip(list, list[1:]):
        if i <= j or abs(i - j) > 3:
            return False
    return True

counts = 0
for report in reports:
    if is_gradually_ascending(report) or is_gradually_descending(report):
        counts += 1
print(counts)
