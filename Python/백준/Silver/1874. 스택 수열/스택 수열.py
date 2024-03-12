n = int(input())
seq = [int(input()) for _ in range(n)]  
st = []  
result = []  
c = 1  
for num in seq:
    while c <= num:
        st.append(c)
        result.append('+')
        c += 1
    if st[-1] == num:
        st.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    for op in result:
        print(op)
