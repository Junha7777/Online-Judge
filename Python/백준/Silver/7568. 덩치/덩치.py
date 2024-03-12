N = int(input())
pe = []

for _ in range(N):
    w, h = map(int, input().split())
    pe.append((w, h))

ra = []

for i in range(N):
    r = 1
    for j in range(N):
        if i != j:
            if pe[i][0] < pe[j][0] and pe[i][1] < pe[j][1]:
                r += 1
    ra.append(r)
print(" ".join(map(str, ra)))
