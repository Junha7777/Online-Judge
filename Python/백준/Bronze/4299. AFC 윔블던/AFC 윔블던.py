S, D = map(int, input().split())

x = (S + D) // 2
y = (S - D) // 2

if x < 0 or y < 0 or (S + D) % 2 == 1:
    print(-1)
else:
    print(max(x, y), min(x, y))
