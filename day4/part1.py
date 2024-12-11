import os, sys
sys.path.append(os.path.abspath('./'))

from functions import load_data

data = load_data(4)
data = data.split()
print(data)

def count_all_occurrences(grid, word = 'XMAS'):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    total_count = 0

    def search_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True
    
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Diagonal down then right 
        (1, -1),  # Diagonal down then left
        (-1, 1),  # Diagonal up then right
        (-1, -1)  # Diagonal up then left
    ]

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if search_direction(r, c, dx, dy):
                    total_count += 1

    return total_count

occurences = count_all_occurrences(data, 'XMAS')
print(occurences)