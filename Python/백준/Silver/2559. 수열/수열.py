n, k = map(int, input().split())
array = list(map(int, input().split()))

t = sum(array[:k])
r = t
for i in range(k, n):
    t += array[i] - array[i-k]
    r = max(r, t)

print(r)