import sys
import heapq

def d(s):
    global res
    dist[s][0] = 0
    q = [(0, s, 0)]
    while q:
        d0, u, v = heapq.heappop(q)
        if any(dist[u][i] < d0 for i in range(v)) or dist[u][v] < d0:
            continue
        if u == e - 1:
            res = min(res, dist[u][v])
            continue
        for nxt, w in g[u]:
            d1 = d0 + w
            if v + 1 < n and d1 < dist[nxt][v + 1]:
                dist[nxt][v + 1] = d1
                heapq.heappush(q, (d1, nxt, v + 1))

n, m, t = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())

g = [[] for _ in range(n)]
INF = 10**18
tax = []
dist = [[INF] * n for _ in range(n)]
res = INF

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    g[a - 1].append((b - 1, w))
    g[b - 1].append((a - 1, w))

for _ in range(t):
    tax.append(int(sys.stdin.readline()))

d(s - 1)
print(res)

for x in tax:
    for i in range(n):
        if dist[e - 1][i] != INF:
            dist[e - 1][i] += x * i
    print(min(dist[e - 1]))