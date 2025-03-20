import sys

sys.setrecursionlimit(100000)
input = sys.stdin.read

def find_articulation_points(v, visited, discovery, low, parent, is_articulation, graph, time):
    children = 0
    visited[v] = True
    discovery[v] = low[v] = time[0]
    time[0] += 1

    for neighbor in graph[v]:
        if not visited[neighbor]:
            parent[neighbor] = v
            children += 1
            find_articulation_points(neighbor, visited, discovery, low, parent, is_articulation, graph, time)

            low[v] = min(low[v], low[neighbor])

            if parent[v] == -1 and children > 1:
                is_articulation[v] = True
            if parent[v] != -1 and low[neighbor] >= discovery[v]:
                is_articulation[v] = True
        elif neighbor != parent[v]:
            low[v] = min(low[v], discovery[neighbor])

def solve():
    input_data = input().splitlines()
    V, E = map(int, input_data[0].split())
    graph = [[] for _ in range(V + 1)]

    for i in range(1, E + 1):
        u, v = map(int, input_data[i].split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V + 1)
    discovery = [-1] * (V + 1)
    low = [-1] * (V + 1)
    parent = [-1] * (V + 1)
    is_articulation = [False] * (V + 1)
    time = [0]

    for i in range(1, V + 1):
        if not visited[i]:
            find_articulation_points(i, visited, discovery, low, parent, is_articulation, graph, time)

    articulation_points = [i for i in range(1, V + 1) if is_articulation[i]]
    print(len(articulation_points))
    print(*articulation_points)

if __name__ == "__main__":
    solve()