money = int(input())
count = 0

while money >= 0:
    if money % 5 == 0:
        count += money // 5
        print(count)
        break
    money -= 2
    count += 1
else:
    print(-1)
