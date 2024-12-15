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

for key in antennas:
    coordinate_list = antennas[key]
    for pair in combinations(antennas[key], 2):
        # for loop to iterate over combinations of key
        if pair[0] != pair[1]:
            dX = pair[1][0] - pair[0][0] # comparison of x 
            dY = pair[1][1] - pair[0][1] # comparison of y
            
            if pair[0] not in locations:
                locations.append(pair[0])
            if pair[1] not in locations:
                locations.append(pair[1])
            
            if math.gcd(dX, dY) != 0:
                gcd = math.gcd(dX, dY)
                dX //= gcd
                dY //= gcd

            antinode1 = (pair[0][0] - dX, pair[0][1] - dY)
            while 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                if antinode1 not in locations:
                    locations.append(antinode1)
                antinode1 = (antinode1[0] - dX, antinode1[1] - dY)
            antinode2 = (pair[0][0] + dX, pair[0][1] + dY)
            while 0 <= antinode2[0] < bounds and 0 <= antinode2[1] < bounds:
                if antinode2 not in locations:
                    locations.append(antinode2)
                antinode2 = (antinode2[0] + dX, antinode2[1] + dY)

print(locations)
print(len(locations))