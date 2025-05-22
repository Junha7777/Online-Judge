n = int(input())
w = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
s = 0

for _ in range(n):
    x, _ = map(int, input().split())
    s += w[x]

print(s)