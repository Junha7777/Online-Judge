import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축(Path Compression)
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])  # 가중치 기준으로 정렬
    parent = list(range(V + 1))  # 자기 자신을 부모로 초기화
    rank = [0] * (V + 1)  # 랭크 배열
    
    mst_weight = 0
    mst_edges = 0
    
    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):  # 사이클이 발생하지 않으면
            union(parent, rank, u, v)
            mst_weight += weight
            mst_edges += 1
            if mst_edges == V - 1:  # MST는 V-1개의 간선으로 이루어짐
                break

    return mst_weight

def main():
    data = input().split("\n")
    V, E = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:E+1]]
    print(kruskal(V, edges))

if __name__ == "__main__":
    main()