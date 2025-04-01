t = int(input())

for _ in range(t):
    answer = 0
    n,c = map(int, input().split())
    answer = n // c
    if n % c > 0: answer +=1
    print(answer)