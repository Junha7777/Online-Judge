import sys
import math

input = sys.stdin.read
sys.setrecursionlimit(100000)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = (data[start], start)
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = (value, idx)
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, value, 2 * node + 1, start, mid)
            else:
                self.update(idx, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return (math.inf, -1)
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_query = self.query(L, R, 2 * node + 1, start, mid)
        right_query = self.query(L, R, 2 * node + 2, mid + 1, end)
        return min(left_query, right_query)

def main():
    input_data = input().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    m = int(input_data[n+1])
    queries = input_data[n+2:]

    seg_tree = SegmentTree(arr)

    result = []
    idx = 0
    while idx < len(queries):
        q_type = int(queries[idx])
        if q_type == 1:
            i = int(queries[idx + 1]) - 1
            v = int(queries[idx + 2])
            seg_tree.update(i, v, 0, 0, n - 1)
            idx += 3
        elif q_type == 2:
            l = int(queries[idx + 1]) - 1
            r = int(queries[idx + 2]) - 1
            result.append(seg_tree.query(l, r, 0, 0, n - 1)[1] + 1)
            idx += 3

    for res in result:
        print(res)

if __name__ == "__main__":
    main()