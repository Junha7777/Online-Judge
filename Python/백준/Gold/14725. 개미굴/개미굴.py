import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        node = self.root
        for part in path:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.is_end = True

    def display(self, node=None, depth=0):
        if node is None:
            node = self.root
        for key in sorted(node.children.keys()):
            print("--" * depth + key)
            self.display(node.children[key], depth + 1)

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    trie = Trie()
    for i in range(1, n + 1):
        path = data[i].split()[1:]
        trie.insert(path)
    trie.display()

if __name__ == "__main__":
    main()