import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

from itertools import combinations
import math

data = load_data(8)

data = data.split()

antennas = {}
for index_row, row in enumerate(data):
    for index_col, cell in enumerate(row):
        if cell != '.':
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((index_row, index_col))

locations = []
bounds = len(data[0])

