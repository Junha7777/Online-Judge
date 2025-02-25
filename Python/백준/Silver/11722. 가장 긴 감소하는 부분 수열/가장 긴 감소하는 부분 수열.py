def longest_decreasing_subsequence(n, arr):
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

n = int(input())
arr = list(map(int, input().split()))
print(longest_decreasing_subsequence(n, arr))