def OA(y, m):
    d = m - y
    o = m + d
    return o

y = int(input().strip())
m = int(input().strip())

o = OA(y, m)

print(o)
