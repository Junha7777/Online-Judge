import sys

input = sys.stdin.read
data = input().split()

idx = 0

N = int(data[idx])
M = int(data[idx + 1])
idx += 2

A = [[0] * (N + 1) for _ in range(N + 1)]
S = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        A[i][j] = int(data[idx])
        idx += 1
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + A[i][j]

result = []
for _ in range(M):
    x1 = int(data[idx])
    y1 = int(data[idx + 1])
    x2 = int(data[idx + 2])
    y2 = int(data[idx + 3])
    idx += 4

    ans = S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1]
    result.append(str(ans))

sys.stdout.write("\n".join(result) + "\n")