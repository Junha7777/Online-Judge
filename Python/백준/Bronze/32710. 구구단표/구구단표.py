def f(n):
    s = set()
    for i in range(2, 10):
        s.add(i)
        for j in range(1, 10):
            s.add(j)
            s.add(i * j)
    return 1 if n in s else 0

n = int(input())
print(f(n))