n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for coin in reversed(coins):
    if k == 0:
        break
    count += k // coin
    k %= coin

print(count)