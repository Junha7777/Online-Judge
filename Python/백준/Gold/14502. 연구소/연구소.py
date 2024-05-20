from itertools import combinations
from collections import deque
import copy

def spread_virus(lab, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx, ny))

def get_safe_area(lab, N, M):
    return sum(row.count(0) for row in lab)

def solve(N, M, lab):
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
    max_safe_area = 0

    for walls in combinations(empty_spaces, 3):
        new_lab = copy.deepcopy(lab)
        for wx, wy in walls:
            new_lab[wx][wy] = 1
        spread_virus(new_lab, N, M)
        max_safe_area = max(max_safe_area, get_safe_area(new_lab, N, M))
    
    return max_safe_area

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, M, lab))
