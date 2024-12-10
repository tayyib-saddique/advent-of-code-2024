import os, sys
sys.path.append(os.path.abspath('./'))

from part1 import data

import regex as re

print(data)

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
print(matches)

enabled = True # by default, instructions are enabled
number_list = []
for match in matches:
    if match == 'do()':
        enabled = True # enable instructions 
    elif match == "don't()":
        enabled = False  # disable all instructons which include don't
    
    if match.startswith('mul(') and enabled:
        number_list.append(re.findall(r'(\d+,\d+)', match))

products = []
for numbers in number_list:
    i, j = map(int, numbers[0].split(','))
    products.append(i * j)

print(sum(products))
