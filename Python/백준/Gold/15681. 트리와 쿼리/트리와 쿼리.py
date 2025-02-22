import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dfs(node, parent):
    subtree_size[node] = 1
    for child in tree[node]:
        if child != parent:
            subtree_size[node] += dfs(child, node)
    return subtree_size[node]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
subtree_size = [0] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

dfs(R, -1)

for _ in range(Q):
    U = int(input())
    print(subtree_size[U])