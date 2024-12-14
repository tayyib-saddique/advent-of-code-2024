import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

from itertools import combinations

data = load_data(8)

# Split the input data into a list of rows
data = data.split()
print(data)

antennas = {}
for index_row, row in enumerate(data):
    for index_col, cell in enumerate(row):
        if cell != '.':
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((index_row, index_row))

locations = []
bounds = len(data[0])

for key in antennas:
    coordinate_list = antennas[key]
    for pair in combinations(antennas[key], 2):
        # for loop to iterate over combinations of key
        if pair[0] != pair[1]:
            dX = pair[1][0] - pair[0][0] # comparison of x 
            dY = pair[1][1] - pair[0][1] # comparison of y
            
            antinode1 = (pair[0][0] - dX, pair[0][1] - dY) # defining antinode1 using distances based on dX and dY
            print(antinode1) 
            # if antinode is within bounds and not in locations, append
            if 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                if antinode1 not in locations:
                    locations.append(antinode1)

            antinode2 = (pair[1][0] + dX, pair[1][1] + dY) # defining antinode2 using distances based on dX and dY
            print(antinode2)
            # if antinode is within bounds and not in locations, append
            if 0 <= antinode2[0] < bounds and 0 <= antinode2[1] < bounds:
                if antinode2 not in locations:
                    locations.append(antinode2)

print(len(locations))