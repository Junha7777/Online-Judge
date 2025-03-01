MOD = 1000000007

def sum_of_differences(arr):
    arr.sort()
    n = len(arr)
    pow2 = [1] * n

    for i in range(1, n):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    result = 0
    for i in range(n):
        result = (result + arr[i] * (pow2[i] - pow2[n - 1 - i])) % MOD

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    print(sum_of_differences(arr))