e = input()

n = len(e) + 2
cnt = 0
for s in e:
  if s == '_':
    cnt += 1

print(n + cnt * 5)