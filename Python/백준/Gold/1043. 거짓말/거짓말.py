class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 첫 줄
    N = int(data[0])
    M = int(data[1])
    
    # 두 번째 줄
    truth_count = int(data[2])
    truth_people = list(map(int, data[3:3 + truth_count]))
    
    # 파티 정보
    parties = []
    index = 3 + truth_count
    while index < len(data):
        party_size = int(data[index])
        party = list(map(int, data[index + 1: index + 1 + party_size]))
        parties.append(party)
        index += 1 + party_size
    
    # 유니온 파인드 초기화
    uf = UnionFind(N + 1)
    
    # 진실을 아는 사람들 연결
    if truth_count > 0:
        first_truth = truth_people[0]
        for person in truth_people[1:]:
            uf.union(first_truth, person)
    
    # 파티 참석자들을 하나의 그룹으로 연결
    for party in parties:
        first_person = party[0]
        for person in party[1:]:
            uf.union(first_person, person)
    
    # 진실 그룹의 대표 찾기
    truth_group = set(uf.find(person) for person in truth_people)
    
    # 과장된 이야기를 할 수 있는 파티 개수 계산
    count = 0
    for party in parties:
        if uf.find(party[0]) not in truth_group:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()