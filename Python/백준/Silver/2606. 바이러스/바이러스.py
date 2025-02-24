import sys
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited[start] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1
    return count

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = bfs(graph, 1)

print(result)