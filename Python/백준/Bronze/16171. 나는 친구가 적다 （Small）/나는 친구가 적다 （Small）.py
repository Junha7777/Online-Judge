S = list(input())
K = input()
new = []

for s in S:
    if ord(s) >= 65 and ord(s) < 91:
        new.append(s)
    elif ord(s) >= 97 and ord(s) < 123:
        new.append(s)

new = ''.join(new)

if K in new:
    print(1)
else:
    print(0)