a = int(input())
b = list(map(int, input().split()))
result = 0
for i in range(len(b)):
    result = result^b[i]
if(result == 0):
    print('cubelover')
else:
    print('koosaga')