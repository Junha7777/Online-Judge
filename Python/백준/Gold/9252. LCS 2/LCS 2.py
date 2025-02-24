import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
len1, len2 = len(str1), len(str2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs_length = dp[len1][len2]
sys.stdout.write(str(lcs_length) + "\n")

if lcs_length > 0:
    i, j = len1, len2
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    sys.stdout.write("".join(reversed(lcs)) + "\n")