import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

import regex as re

data = load_data(3)
matches = re.findall('mul\(\d+,\d+\)', data)

number_list = []
for match in matches:
    number_list.append(re.findall(r'(\d+,\d+)', match))
    
products = []

for numbers in number_list:
    i, j = map(int, numbers[0].split(','))
    products.append(i * j)

print(sum(products))