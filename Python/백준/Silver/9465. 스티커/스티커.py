import sys

input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1
results = []

for _ in range(T):
    n = int(data[idx])
    idx += 1
    sticker = [list(map(int, data[idx:idx + n])), list(map(int, data[idx + n:idx + 2 * n]))]
    idx += 2 * n

    if n == 1:
        results.append(str(max(sticker[0][0], sticker[1][0])))
        continue

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]

    results.append(str(max(dp[0][n - 1], dp[1][n - 1])))

sys.stdout.write("\n".join(results) + "\n")