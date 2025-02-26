import sys
import bisect

input = sys.stdin.read
data = list(map(int, input().split()))

n = data[0]
arr = data[1:]

dp = []
lis = []

for num in arr:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
        lis.append((pos, num))
    else:
        dp[pos] = num
        lis.append((pos, num))

length = len(dp)
result = []
for i in range(len(lis) - 1, -1, -1):
    if lis[i][0] == length - 1:
        result.append(lis[i][1])
        length -= 1

result.reverse()
print(len(result))
print(' '.join(map(str, result)))