from itertools import combinations

def find_combinations(N, M):
    numbers = range(1, N + 1)
    for combination in combinations(numbers, M):
        print(" ".join(map(str, combination)))

N, M = map(int, input().split())

find_combinations(N, M)
