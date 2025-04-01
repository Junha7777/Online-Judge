import sys

def count_zeros(n, m):
    count = 0
    for i in range(n, m + 1):
        count += str(i).count('0')
    return count

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(count_zeros(n, m))