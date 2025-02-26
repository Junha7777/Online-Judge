def fib(n):
    z_count = [1, 0]
    o_count = [0, 1]
    
    if n == 0:
        return z_count
    elif n == 1:
        return o_count
    
    for i in range(2, n + 1):
        z_count.append(z_count[i - 1] + z_count[i - 2])
        o_count.append(o_count[i - 1] + o_count[i - 2])
    
    return z_count[n], o_count[n]

t = int(input())
for _ in range(t):
    n = int(input())
    z, o = fib(n)
    print(z, o)