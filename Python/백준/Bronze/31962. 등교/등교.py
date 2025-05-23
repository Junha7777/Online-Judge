n, x = map(int, input().split())
b = [tuple(map(int, input().split())) for _ in range(n)]
b.sort(reverse=True)

for k, d in b:
    if k + d <= x:
        print(k)
        break
else:
    print(-1)