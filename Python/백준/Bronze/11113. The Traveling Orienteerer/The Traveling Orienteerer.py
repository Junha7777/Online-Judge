import math
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1

    v = []
    for _ in range(N):
        x, y = map(float, (data[idx], data[idx + 1]))
        v.append((x, y))
        idx += 2

    M = int(data[idx])
    idx += 1

    results = []
    for _ in range(M):
        K = int(data[idx])
        idx += 1

        u = list(map(int, data[idx:idx + K]))
        idx += K

        ans = 0
        for i in range(1, K):
            x1, y1 = v[u[i - 1]]
            x2, y2 = v[u[i]]
            ans += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        results.append(round(ans))

    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()