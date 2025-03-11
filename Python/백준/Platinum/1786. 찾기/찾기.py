import sys

def get_pi(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = get_pi(pattern)
    j = 0
    result = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                result.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return result

def main():
    input = sys.stdin.read
    data = input().split('\n')
    text = data[0]
    pattern = data[1]
    result = kmp_search(text, pattern)
    print(len(result))
    for idx in result:
        print(idx + 1)

if __name__ == "__main__":
    main()