from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mv(x, y, dx, dy, bd):
    cnt = 0
    while bd[x+dx][y+dy] != '#' and bd[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(bd, rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    v = set()
    v.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, d = q.popleft()

        if d >= 10:
            return -1

        for i in range(4):
            nrx, nry, rcnt = mv(rx, ry, dx[i], dy[i], bd)
            nbx, nby, bcnt = mv(bx, by, dx[i], dy[i], bd)

            if bd[nbx][nby] == 'O':
                continue

            if bd[nrx][nry] == 'O':
                return d + 1

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in v:
                v.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, d + 1))

    return -1

n, m = map(int, input().split())
bd = [list(input().strip()) for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if bd[i][j] == 'R':
            rx, ry = i, j
        if bd[i][j] == 'B':
            bx, by = i, j

res = bfs(bd, rx, ry, bx, by)
print(res)
