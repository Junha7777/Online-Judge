from collections import Counter

socks = [int(input()) for _ in range(5)]
count = Counter(socks)

for number, cnt in count.items():
    if cnt % 2 == 1:
        print(number)
        break