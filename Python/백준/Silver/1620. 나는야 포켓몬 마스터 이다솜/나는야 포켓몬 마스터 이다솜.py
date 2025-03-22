import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    index_to_name = [None] * (N + 1)
    name_to_index = {}
    for i in range(1, N + 1):
        name = input().strip()
        index_to_name[i] = name
        name_to_index[name] = i
    result = []
    for _ in range(M):
        query = input().strip()
        if query.isdigit():
            result.append(index_to_name[int(query)])
        else:
            result.append(str(name_to_index[query]))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
