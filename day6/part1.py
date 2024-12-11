import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(6)

data = data.splitlines()
print(data)

def find_guard(grid):
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '^':
                return row_index, col_index

position = find_guard(data)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
direction_index = 0
row, col = position
count = 0

visited = set() # sets used to store distinct visited positions

while True:
    visited.add((row, col)) # used for final distinct visited position before guard is out of scope
    new_row = row + directions[direction_index][0]
    new_col = col + directions[direction_index][1]

    # if the position of the new row or new column is outside the scope 
    # (i.e. greater than the length or less than 0), the while loop breaks
    if not (0 <= new_row < len(data) and 0 <= new_col < len(data[0])):
        break

    if data[new_row][new_col] == '#':
        direction_index = (direction_index + 1) % 4 
        # (0 + 1) % 4 = 1 - right
        # (1 + 1) % 4 = 2 - down
        # (2 + 1) % 4 = 3 - left
        # (3 + 1) % 4 = 0 - up
    else:
        visited.add((row, col))
        row, col = new_row, new_col # continue if no obstacle

print((visited))
print(len(visited))