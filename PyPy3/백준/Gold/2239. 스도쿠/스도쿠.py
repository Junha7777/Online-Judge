import sys

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]
empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(x, y, num):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False
    start_x, start_y = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_x + i][start_y + j] == num:
                return False
    return True

def solve(index=0):
    if index == len(empty_cells):
        for row in board:
            sys.stdout.write("".join(map(str, row)) + "\n")
        sys.exit(0)

    x, y = empty_cells[index]
    for num in range(1, 10):
        if is_valid(x, y, num):
            board[x][y] = num
            solve(index + 1)
            board[x][y] = 0

solve()