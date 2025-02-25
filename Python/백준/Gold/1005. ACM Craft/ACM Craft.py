import sys
from collections import deque

def acm_craft():
    input = sys.stdin.read
    data = input().split("\n")
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N, K = map(int, data[index].split())
        index += 1
        
        build_time = list(map(int, data[index].split()))
        index += 1
        
        graph = [[] for _ in range(N + 1)]
        indegree = [0] * (N + 1)
        dp = [0] * (N + 1)
        
        for _ in range(K):
            X, Y = map(int, data[index].split())
            index += 1
            graph[X].append(Y)
            indegree[Y] += 1
        
        W = int(data[index])
        index += 1
        
        queue = deque()
        
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = build_time[i - 1]
        
        while queue:
            current = queue.popleft()
            
            for next_building in graph[current]:
                indegree[next_building] -= 1
                dp[next_building] = max(dp[next_building], dp[current] + build_time[next_building - 1])
                
                if indegree[next_building] == 0:
                    queue.append(next_building)
        
        results.append(str(dp[W]))
    
    sys.stdout.write("\n".join(results) + "\n")
    
if __name__ == "__main__":
    acm_craft()