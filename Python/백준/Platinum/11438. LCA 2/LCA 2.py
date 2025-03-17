import sys
import math
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def preprocess_lca(n, edges):
    LOG = math.ceil(math.log2(n))
    parent = [[-1] * (LOG + 1) for _ in range(n + 1)]
    depth = [-1] * (n + 1)
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(root):
        queue = deque([root])
        depth[root] = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if depth[neighbor] == -1:
                    depth[neighbor] = depth[node] + 1
                    parent[neighbor][0] = node
                    queue.append(neighbor)

    bfs(1)

    for j in range(1, LOG + 1):
        for i in range(1, n + 1):
            if parent[i][j - 1] != -1:
                parent[i][j] = parent[parent[i][j - 1]][j - 1]

    return parent, depth, LOG

def lca(u, v, parent, depth, LOG):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(LOG, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = parent[u][i]

    if u == v:
        return u

    for i in range(LOG, -1, -1):
        if parent[u][i] != -1 and parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]

def main():
    input_data = input().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    edges = []
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        edges.append((u, v))
        idx += 2

    parent, depth, LOG = preprocess_lca(n, edges)

    m = int(input_data[idx])
    idx += 1
    results = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        results.append(lca(u, v, parent, depth, LOG))
        idx += 2

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()