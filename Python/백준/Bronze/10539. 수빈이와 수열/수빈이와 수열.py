n = int(input())
arr = list(map(int, input().split()))

res = [arr[0]]
for i in range(1, n):
    res.append(arr[i] * (i+1) - sum(res))
for i in res:
    print(i, end=' ')