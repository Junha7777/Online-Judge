s = list(input())
r = s.index("@")
b = s.index("#")
f = s.index("!")

if (r < b < f) or (r > b > f):
    c1 = abs(b - r) - 1
    c2 = abs(f - b)
    print(c1 + c2)
else:
    print(-1)