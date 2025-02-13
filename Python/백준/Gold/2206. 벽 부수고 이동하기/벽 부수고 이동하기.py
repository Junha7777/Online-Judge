from collections import deque
import sys

def bfs(n, m, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0, 1)])  # (x, y, 벽 부숨 여부, 거리)
    visited[0][0][0] = True

    while queue:
        x, y, wall_broken, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    visited[nx][ny][wall_broken] = True
                    queue.append((nx, ny, wall_broken, dist + 1))
                    
                elif grid[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    print(bfs(n, m, grid))