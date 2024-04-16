a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

sum1 = a + b + c
sum2 = a + c + d
sum3 = a + b + d
sum4 = d + b + c

arr = list()
arr.append(sum1)
arr.append(sum2)
arr.append(sum3)
arr.append(sum4)
Sum = max(arr)
arr1 = list()
arr1.append(e)
arr1.append(f)
print(Sum+ max(arr1))