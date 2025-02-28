# 입력 받기
s = input().strip()
bomb = input().strip()

stack = []

for char in s:
    stack.append(char)
    if stack[-len(bomb):] == list(bomb):
        for _ in range(len(bomb)):
            stack.pop()

# 결과 출력
print(''.join(stack) if stack else "FRULA")