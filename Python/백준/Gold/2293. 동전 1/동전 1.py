def count_coin_cases(n, k, coins):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, k + 1):
            dp[j] += dp[j-coin]

    return dp[k]

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
print(count_coin_cases(n, k, coins))