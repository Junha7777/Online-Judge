import copy

def move(board, direction):
    if direction == 0:  # Up
        for j in range(len(board)):
            temp = [board[i][j] for i in range(len(board)) if board[i][j] != 0]
            for i in range(len(temp) - 1):
                if temp[i] == temp[i + 1]:
                    temp[i] *= 2
                    temp[i + 1] = 0
            temp = [x for x in temp if x != 0]
            for i in range(len(board)):
                board[i][j] = temp[i] if i < len(temp) else 0
                
    elif direction == 1:  # Down
        for j in range(len(board)):
            temp = [board[i][j] for i in range(len(board)) if board[i][j] != 0]
            for i in range(len(temp) - 1, 0, -1):
                if temp[i] == temp[i - 1]:
                    temp[i] *= 2
                    temp[i - 1] = 0
            temp = [x for x in temp if x != 0]
            for i in range(len(board)):
                board[len(board) - 1 - i][j] = temp[len(temp) - 1 - i] if i < len(temp) else 0
                
    elif direction == 2:  # Left
        for i in range(len(board)):
            temp = [board[i][j] for j in range(len(board)) if board[i][j] != 0]
            for j in range(len(temp) - 1):
                if temp[j] == temp[j + 1]:
                    temp[j] *= 2
                    temp[j + 1] = 0
            temp = [x for x in temp if x != 0]
            for j in range(len(board)):
                board[i][j] = temp[j] if j < len(temp) else 0
                
    elif direction == 3:  # Right
        for i in range(len(board)):
            temp = [board[i][j] for j in range(len(board)) if board[i][j] != 0]
            for j in range(len(temp) - 1, 0, -1):
                if temp[j] == temp[j - 1]:
                    temp[j] *= 2
                    temp[j - 1] = 0
            temp = [x for x in temp if x != 0]
            for j in range(len(board)):
                board[i][len(board) - 1 - j] = temp[len(temp) - 1 - j] if j < len(temp) else 0
    return board

def dfs(board, depth):
    if depth == 5:
        return max(max(row) for row in board)
    max_block = 0
    for direction in range(4):
        new_board = move(copy.deepcopy(board), direction)
        max_block = max(max_block, dfs(new_board, depth + 1))
    return max_block

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(dfs(board, 0))