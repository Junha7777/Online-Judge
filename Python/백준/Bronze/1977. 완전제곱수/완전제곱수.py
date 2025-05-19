import math

M = int(input())
N = int(input())

perfect_squares = [i for i in range(M, N+1) if math.isqrt(i)**2 == i]

if perfect_squares:
    print(sum(perfect_squares))
    print(min(perfect_squares))
else:
    print(-1)