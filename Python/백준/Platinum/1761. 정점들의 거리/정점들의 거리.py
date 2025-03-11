import sys
import collections

sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(node, parent, depth):
    depths[node] = depth
    parents[node][0] = parent
    for next_node, weight in graph[node]:
        if next_node != parent:
            distances[next_node] = distances[node] + weight
            dfs(next_node, node, depth + 1)

def lca(u, v):
    if depths[u] < depths[v]:
        u, v = v, u
    diff = depths[u] - depths[v]
    for i in range(MAX_LOG):
        if diff & (1 << i):
            u = parents[u][i]
    if u == v:
        return u
    for i in range(MAX_LOG - 1, -1, -1):
        if parents[u][i] != parents[v][i]:
            u = parents[u][i]
            v = parents[v][i]
    return parents[u][0]

input_data = input().split()
n = int(input_data[0])
graph = collections.defaultdict(list)
index = 1
for _ in range(n - 1):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    w = int(input_data[index + 2])
    graph[u].append((v, w))
    graph[v].append((u, w))
    index += 3

MAX_LOG = 17
depths = [0] * (n + 1)
distances = [0] * (n + 1)
parents = [[0] * MAX_LOG for _ in range(n + 1)]

dfs(1, 0, 0)

for j in range(1, MAX_LOG):
    for i in range(1, n + 1):
        parents[i][j] = parents[parents[i][j - 1]][j - 1]

m = int(input_data[index])
index += 1
results = []
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    ancestor = lca(u, v)
    distance = distances[u] + distances[v] - 2 * distances[ancestor]
    results.append(str(distance))
    index += 2

print("\n".join(results))