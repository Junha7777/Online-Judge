# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스를 처리
for _ in range(T):
    n = int(input())
    
    cities = set()
    
    for _ in range(n):
        city = input().strip()
        cities.add(city)
    
    print(len(cities))