import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for length in range(2, n):
    for i in range(n - length):
        j = i + length
        if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

output = []
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    output.append(str(dp[s - 1][e - 1]))

sys.stdout.write("\n".join(output) + "\n")