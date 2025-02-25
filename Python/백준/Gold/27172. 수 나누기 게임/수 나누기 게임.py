import sys

def solve():
    N = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))

    score = {num: 0 for num in numbers}
    
    exists = [False] * (10**6 + 1)
    
    for num in numbers:
        exists[num] = True
    
    for num in numbers:
        multiplier = 2
        while num * multiplier <= 10**6:
            if exists[num * multiplier]:
                score[num] += 1
                score[num * multiplier] -= 1
            multiplier += 1

    print(" ".join(str(score[num]) for num in numbers))
    
solve()