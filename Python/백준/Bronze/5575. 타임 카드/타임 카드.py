arr1 = []
arr2 = []

for i in range(3):
    a = input()
    arr1.append(a.split())
for j in range(3):
    b1 = int(arr1[j][0]) * 3600 + int(arr1[j][1]) * 60 + int(arr1[j][2])
    a1 = int(arr1[j][3]) * 3600 + int(arr1[j][4]) * 60 + int(arr1[j][5])
    time = a1 - b1
    s = int(time % 60)
    m = int((time / 60) % 60)
    h = int((time / 60) / 60)
    arr2.append(h)
    arr2.append(m)
    arr2.append(s)
for k in range(0, 7, 3):
    print(arr2[k], arr2[k+1], arr2[k+2])