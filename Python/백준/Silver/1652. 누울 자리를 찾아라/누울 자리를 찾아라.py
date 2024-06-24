import sys
input = sys.stdin.readline

n = int(input())
b = [list(input().rstrip()) for _ in range(n)]

a = [0, 0]
for i in range(n):
    r, c = 0,0
    for j in range(n):
        # 가로
        if b[i][j] == '.':
            r+=1
        else:
            r=0
        if r==2:
            a[0] += 1
        
        # 세로
        if b[j][i] == '.':
            c+=1
        else:
            c=0
        if c==2:
            a[1] += 1
print(*a)