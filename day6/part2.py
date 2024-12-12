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
guard_row, guard_col = position
valid_positions = 0

def guard_move(grid, start_row, start_col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    direction_index = 0
    visited = set() # sets used to store distinct visited positions
    row, col = start_row, start_col

    while True:
        if (row, col, direction_index) in visited:
            return True # detects loop exists
        visited.add((row, col, direction_index)) 
        # direction index must be added as direction changes

        new_row = row + directions[direction_index][0]
        new_col = col + directions[direction_index][1]

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False # out of scope

        if grid[new_row][new_col] in ('#', 'O'):
            direction_index = (direction_index + 1) % 4
        else:
            row, col = new_row, new_col # continue if no obstruction


valid = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        # continue if the position is the original starting position or is not empty
        if data[row][col] != '.' or (row, col) == (guard_row, guard_col):
            continue

        # create modified grid with temporarily obstruction 'O' in place
        modified_grid = [list(line) for line in data]
        modified_grid[row][col] = 'O'
        modified_grid = [''.join(line) for line in modified_grid]
        
        if guard_move(modified_grid, guard_row, guard_col):
            valid += 1

print(valid)
