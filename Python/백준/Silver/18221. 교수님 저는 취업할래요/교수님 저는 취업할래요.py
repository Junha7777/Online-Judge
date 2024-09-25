import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def can_escape(N, grid, s_pos, p_pos):
    s_row, s_col = s_pos
    p_row, p_col = p_pos
    
    # Check if distance between professor and Sungkyu is >= 5
    if distance(s_row, s_col, p_row, p_col) < 5:
        return 0
    
    # Check rectangular condition
    r1 = min(p_row, s_row)
    r2 = max(p_row, s_row)
    c1 = min(p_col, s_col)
    c2 = max(p_col, s_col)
    
    student_count = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 1:
                student_count += 1
    
    if student_count >= 3:
        return 1
    
    # Check row or column conditions if the professor and Sungkyu are in the same row or column
    if p_row == s_row:
        student_count = 0
        for c in range(min(p_col, s_col), max(p_col, s_col) + 1):
            if grid[p_row][c] == 1:
                student_count += 1
        if student_count >= 3:
            return 1
    
    if p_col == s_col:
        student_count = 0
        for r in range(min(p_row, s_row), max(p_row, s_row) + 1):
            if grid[r][p_col] == 1:
                student_count += 1
        if student_count >= 3:
            return 1
    
    return 0

# Input parsing
N = int(input())
grid = []
s_pos = p_pos = None

for r in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
    if 2 in line:
        s_pos = (r, line.index(2))
    if 5 in line:
        p_pos = (r, line.index(5))

# Determine if Sungkyu can escape
result = can_escape(N, grid, s_pos, p_pos)
print(result)