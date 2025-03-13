import sys

sys.setrecursionlimit(100000)

def dfs(v, graph, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(v)

def reverse_dfs(v, reverse_graph, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in reverse_graph[v]:
        if not visited[neighbor]:
            reverse_dfs(neighbor, reverse_graph, visited, component)

def find_sccs(n, graph):
    stack = []
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited, stack)
    
    reverse_graph = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        for neighbor in graph[v]:
            reverse_graph[neighbor].append(v)
    
    visited = [False] * (n + 1)
    sccs = []
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            reverse_dfs(v, reverse_graph, visited, component)
            sccs.append(sorted(component))
    
    return sorted(sccs, key=lambda x: x[0])

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        index += 2
    
    sccs = find_sccs(n, graph)
    
    print(len(sccs))
    for scc in sccs:
        print(' '.join(map(str, scc)) + ' -1')

if __name__ == "__main__":
    main()