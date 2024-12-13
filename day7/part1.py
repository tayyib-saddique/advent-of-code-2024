import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data
from itertools import product
from operator import add, mul

data = load_data(7)

data = data.splitlines()
datadict = dict()
for line in data:
    datadict[line.split(':')[0]] = list(map(int, line.split()[1:]))

operations = [add, mul]

safe = []
for key, values in datadict.items():
    target = int(key)
    for combination in product(operations, repeat = len(values) - 1):
        # potential combinations when there are three values could be as follows:
        # a + b + c
        # a + b * c
        # a * b * c
        result = values[0]

        for i, operation in enumerate(combination):
            # enumerates each combination and then applies operation to result and following indexed number in values 
            # iterable is one less than length of values (given previous for loop)
            result = operation(result, values[i + 1])
        
        if result == target:
            safe.append(target)
            break

print(safe)
print(sum(safe))
