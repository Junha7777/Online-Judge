def find_kth_number(n, k):
    left, right = 1, n * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count < k:  
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer

N = int(input())
K = int(input())
print(find_kth_number(N, K))