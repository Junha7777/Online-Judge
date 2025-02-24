import sys
sys.setrecursionlimit(10**6)

def dfs(v, parent):
    global time
    visited[v] = True
    discovery_time[v] = low[v] = time
    time += 1

    for to in graph[v]:
        if not visited[to]:
            parent[to] = v
            dfs(to, parent)
            low[v] = min(low[v], low[to])
            if low[to] > discovery_time[v]:
                bridges.append((min(v, to), max(v, to)))
        elif to != parent[v]:
            low[v] = min(low[v], discovery_time[to])

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (V + 1)
discovery_time = [-1] * (V + 1)
low = [-1] * (V + 1)
parent = [-1] * (V + 1)
bridges = []
time = 0

for i in range(1, V + 1):
    if not visited[i]:
        dfs(i, parent)

bridges.sort()
print(len(bridges))
for u, v in bridges:
    print(u, v)