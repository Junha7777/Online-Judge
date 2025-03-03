import sys
import math

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
arr = list(map(int, data[2:n+2]))
queries = data[n+2:]

class SegmentTree:
    def __init__(self, data, func, default):
        self.n = len(data)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        res = self.default
        while left < right:
            if left % 2:
                res = self.func(res, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                res = self.func(res, self.tree[right])
            left //= 2
            right //= 2
        return res

min_tree = SegmentTree(arr, min, float('inf'))
max_tree = SegmentTree(arr, max, float('-inf'))

result = []
for i in range(m):
    left, right = int(queries[2 * i]) - 1, int(queries[2 * i + 1])
    min_val = min_tree.query(left, right)
    max_val = max_tree.query(left, right)
    result.append(f"{min_val} {max_val}")

print("\n".join(result))