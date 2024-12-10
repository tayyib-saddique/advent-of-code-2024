import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(1)

list1 = []
list2 = []
nums = [line.split() for line in data.split('\n')[:-1]]

for list in nums:
    list1.append(int(list[0]))
    list2.append(int(list[1]))

differences = []
for x, y in zip(sorted(list1), sorted(list2)):
    differences.append(abs(x-y))

print(sum(differences))