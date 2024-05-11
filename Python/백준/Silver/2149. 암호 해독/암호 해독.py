n = input()
k = input()

length = len(k) // len(n)
array = []

temp = list(n)
temp.sort()

for i in range(len(n)):
  array.append([temp[i], i, k[length * i : length * i + length]])

array.sort(key = lambda x : x[1])
ans = []

while array:
  for i in n:
    for j in range(len(array)):
      if array[j][0] == i:
        ans.append(array[j])
        array.pop(j)
        break

result = ''
for i in range(length):
  for j in range(len(n)):
    result += ans[j][2][i]

print(result)
