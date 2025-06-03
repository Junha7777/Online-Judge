import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
seq = []

def dfs(cur, d):
    if cur > n: return
    dfs(cur * 2, d + 1)
    seq.append((cur, d))
    dfs(cur * 2 + 1, d + 1)

dfs(1, 0)

md = seq[-1][1]
inf = 0x3f3f3f3f
res = -inf

for i in range(n):
    res = max(res, a[i])
if res <= 0:
    print(res)
    exit(0)

res = 0
for i in range(md + 1):
    for j in range(i, md + 1):
        val = 0
        for k in range(n):
            if seq[k][1] < i or seq[k][1] > j: continue
            val = max(val + a[seq[k][0] - 1], 0)
            res = max(res, val)

print(res)
