N, M = map(int, input().split())
fish_bread = [input() for _ in range(N)]


for row in fish_bread:
    print(row[::-1])
