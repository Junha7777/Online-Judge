MAX = 10001
arr_apartment = [0] * MAX

N, M = map(int, input().split())
for i in range(1, M + 1):
    hand1, hand2 = map(int, input().split())
    arr_apartment[hand1] = i
    arr_apartment[hand2] = i

N %= (2 * M)
if N == 0:
    N = 2 * M

floor = 1
for i in range(1, MAX):
    if arr_apartment[i] != 0:
        if floor == N:
            print(arr_apartment[i])
            break
        else:
            floor += 1