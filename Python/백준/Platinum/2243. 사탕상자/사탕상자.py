import sys

input = sys.stdin.read

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def find_kth(self, k):
        idx = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask != 0:
            t_idx = idx + bit_mask
            if t_idx <= self.size and self.tree[t_idx] < k:
                k -= self.tree[t_idx]
                idx = t_idx
            bit_mask >>= 1
        return idx + 1

def main():
    input_data = input().split()
    n = int(input_data[0])
    commands = input_data[1:]
    
    max_candy = 1000000
    fenwick_tree = FenwickTree(max_candy)
    
    index = 0
    while index < len(commands):
        command = int(commands[index])
        if command == 1:
            k = int(commands[index + 1])
            idx = fenwick_tree.find_kth(k)
            print(idx)
            fenwick_tree.update(idx, -1)
            index += 2
        elif command == 2:
            flavor = int(commands[index + 1])
            count = int(commands[index + 2])
            fenwick_tree.update(flavor, count)
            index += 3
if __name__ == '__main__':
    main()