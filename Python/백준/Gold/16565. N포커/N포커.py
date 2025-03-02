import sys

MOD = 10007

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def combination(n, k):
    if k > n:
        return 0
    return (factorial(n) * pow(factorial(k), MOD-2, MOD) * pow(factorial(n-k), MOD-2, MOD)) % MOD

def solve(n):
    result = 0
    sign = 1
    for k in range(1, 14):
        if k * 4 > n:
            break
        result = (result + sign * combination(13, k) * combination(52 - 4 * k, n - 4 * k)) % MOD
        sign *= -1
    return result

if __name__ == "__main__":
    input = sys.stdin.read
    n = int(input().strip())
    print(solve(n))