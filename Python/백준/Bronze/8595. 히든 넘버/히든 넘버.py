n = int(input())
s = input()

current_number = 0
total_sum = 0

for char in s:
    if char.isdigit():  # 주어진 문자가 숫자인지 확인하는 조건
        current_number = current_number * 10 + int(char)  # 연속된 숫자 만들어 주기
        if current_number > 999999:  # 히든 넘버는 6자리를 넘지 않음
            current_number = 999999
    else:
        total_sum += current_number  # 합계
        current_number = 0

total_sum += current_number  # 마지막 숫자가 존재할 경우 합산

print(total_sum)