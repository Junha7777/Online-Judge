import sys

h, w = map(int, input().split())
n = int(input())
s = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

r = 0
for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = s[i]
        r2, c2 = s[j]

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            r = max(r, r1 * c1 + r2 * c2)
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            r = max(r, r1 * c1 + r2 * c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            r = max(r, r1 * c1 + r2 * c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            r = max(r, r1 * c1 + r2 * c2)

print(r)