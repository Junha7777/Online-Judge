
a = int(input())
w, v = map(int, input().split())

ampere_adapter = w // v

if ampere_adapter >= a:
    print(1)
else:
    print(0)
