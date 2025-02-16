from itertools import combinations

def solution(N, K, words):
    if K < 5:
        return 0

    basic = {'a', 'n', 't', 'i', 'c'}

    alpha = set()
    for word in words:
        for c in word:
            alpha.add(c)
    alpha = alpha - basic

    candidates = []
    for c in combinations(alpha, min(len(alpha), K-5)):
        learned = basic | set(c)

        count = 0
        for word in words:
            can_read = True
            for char in word:
                if char not in learned:
                    can_read = False
                    break
            if can_read:
                count += 1
        candidates.append(count)

    return max(candidates) if candidates else 0

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]
print(solution(N, K, words))