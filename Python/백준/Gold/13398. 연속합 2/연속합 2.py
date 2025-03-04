def max_consecutive_sum(n, arr):
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = arr[0]  
    dp2[0] = 0

    result = dp1[0]

    for i in range(1, n):
        dp1[i] = max(dp1[i-1] + arr[i], arr[i])

        dp2[i] = max(dp1[i-1], dp2[i-1] + arr[i])

        result = max(result, dp1[i], dp2[i])

    return result

n = int(input())
arr = list(map(int, input().split()))
print(max_consecutive_sum(n, arr))