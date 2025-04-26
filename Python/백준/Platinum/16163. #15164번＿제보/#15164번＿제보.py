def count_palindromes(s):
    T = ['#']
    for c in s:
        T.append(c)
        T.append('#')

    n = len(T)
    p = [0] * n
    center = right = 0
    result = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and T[i - p[i] - 1] == T[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
        result += (p[i] + 1) // 2

    return result

if __name__ == "__main__":
    s = input().strip()
    print(count_palindromes(s))
