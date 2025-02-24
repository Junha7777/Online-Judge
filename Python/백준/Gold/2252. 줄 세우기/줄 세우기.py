import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    student = queue.popleft()
    result.append(student)
    for next_student in graph[student]:
        indegree[next_student] -= 1
        if indegree[next_student] == 0:
            queue.append(next_student)

print(*result)