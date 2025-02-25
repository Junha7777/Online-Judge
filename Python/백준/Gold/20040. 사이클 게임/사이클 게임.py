import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def cycle_game(n, m, edges):
    uf = UnionFind(n)
    
    for i, (a, b) in enumerate(edges, start=1):
        if not uf.union(a, b):
            return i
    
    return 0

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:m+1]]
    
    print(cycle_game(n, m, edges))
