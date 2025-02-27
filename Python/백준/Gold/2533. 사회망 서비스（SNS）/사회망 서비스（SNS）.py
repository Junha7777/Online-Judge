import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = 1
    
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

n = int(input().strip())
tree = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1, -1)
print(min(dp[1][0], dp[1][1]))