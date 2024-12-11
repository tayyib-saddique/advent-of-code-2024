import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(4)
data = data.split()
print(data)

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    # Check for the "X-MAS" pattern
    def is_xmas(x, y):
        if x - 1 < 0 or x + 1 >= rows or y - 1 < 0 or y + 1 >= cols:
            return False
        # Check the "X" shape:
        # Top-left "MAS" (forward or reversed)
        mas1 = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1] # top left, centre, bottom right
        mas1_reversed = mas1[::-1]
        # Top-right "MAS" (forward or reversed)
        mas2 = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1] # top right, centre, bottom left
        mas2_reversed = mas2[::-1]
        # Return True if both patterns are valid
        return ("MAS" in (mas1, mas1_reversed) and "MAS" in (mas2, mas2_reversed))

    # Iteratively check each row and column (excluding first and last - centre cannot be either)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_xmas(r, c):
                xmas_count += 1

    return xmas_count

patterns = count_xmas_patterns(data)
print(patterns)