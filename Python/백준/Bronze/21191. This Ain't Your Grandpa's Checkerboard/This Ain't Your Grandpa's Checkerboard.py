def is_correct_grid(grid):
    n = len(grid)
    for i in range(n):
        row = grid[i]
        col = [grid[j][i] for j in range(n)]
        if row.count('B') != n // 2 or col.count('B') != n // 2:
            return 0
        if 'BBB' in ''.join(row) or 'WWW' in ''.join(row):
            return 0
        if 'BBB' in ''.join(col) or 'WWW' in ''.join(col):
            return 0
    return 1

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
grid = data[1:]
print(is_correct_grid(grid))