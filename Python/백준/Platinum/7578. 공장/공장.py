import sys

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

def count_inversions(arr):
    max_val = max(arr)
    fenwick_tree = FenwickTree(max_val)
    inversions = 0

    for i in range(len(arr) - 1, -1, -1):
        inversions += fenwick_tree.query(arr[i] - 1)
        fenwick_tree.update(arr[i], 1)

    return inversions

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    A = list(map(int, data[1:n+1]))
    B = list(map(int, data[n+1:2*n+1]))
    
    pos = {value: idx + 1 for idx, value in enumerate(A)}
    mapped_B = [pos[value] for value in B]
    
    result = count_inversions(mapped_B)
    print(result)

if __name__ == "__main__":
    main()