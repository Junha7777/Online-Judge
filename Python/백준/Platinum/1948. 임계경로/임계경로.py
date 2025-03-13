from collections import deque, defaultdict

def find_longest_path(n, edges, start, end):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    distance = [0] * (n + 1)

    for u, v, w in edges:
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))
        in_degree[v] += 1

    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            in_degree[neighbor] -= 1
            distance[neighbor] = max(distance[neighbor], distance[node] + weight)
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    max_distance = distance[end]
    count = 0
    visited = [False] * (n + 1)
    queue = deque([end])
    visited[end] = True

    while queue:
        node = queue.popleft()
        for neighbor, weight in reverse_graph[node]:
            if distance[node] == distance[neighbor] + weight:
                count += 1
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    return max_distance, count

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, w))
    start, end = map(int, input().strip().split())
    max_distance, count = find_longest_path(n, edges, start, end)
    print(max_distance)
    print(count)