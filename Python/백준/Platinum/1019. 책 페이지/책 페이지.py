def count_digits(n):
    counts = [0] * 10
    factor = 1
    while n > 0:
        while n % 10 != 9:
            for i in str(n):
                counts[int(i)] += factor
            n -= 1
        if n < 10:
            for i in range(n + 1):
                counts[i] += factor
            counts[0] -= factor
            break
        else:
            for i in range(10):
                counts[i] += (n // 10 + 1) * factor
        counts[0] -= factor
        factor *= 10
        n //= 10
    return counts

n = int(input())
result = count_digits(n)
print(' '.join(map(str, result)))