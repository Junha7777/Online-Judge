from collections import deque

def is_prime(n):
    # 소수 판별 함수
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_min_steps(start, target):
    # BFS로 최소 단계 찾기
    visited = {start: 0}  # 방문한 숫자와 단계 수 저장
    q = deque([start])
    
    while q:
        curr = q.popleft()  # 현재 숫자
        curr_str = str(curr)  # 문자열로 변환
        
        if curr == target:
            return visited[curr]
            
        # 각 자릿수 변경
        for i in range(4):
            prefix = curr_str[:i]  # 현재 자리 이전 숫자들
            suffix = curr_str[i+1:]  # 현재 자리 이후 숫자들
            digit = int(curr_str[i])  # 현재 자리 숫자
            
            for j in range(10):
                if i == 0 and j == 0:  # 첫 자리는 0이 될 수 없음
                    continue
                if j == digit:  # 현재 숫자와 같으면 건너뛰기
                    continue
                    
                # 새로운 숫자 생성
                next_num = int(prefix + str(j) + suffix)
                if is_prime(next_num) and next_num not in visited:
                    visited[next_num] = visited[curr] + 1  # 단계 수 증가
                    q.append(next_num)
    
    return "Impossible"

# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    start, target = map(int, input().split())
    print(find_min_steps(start, target))