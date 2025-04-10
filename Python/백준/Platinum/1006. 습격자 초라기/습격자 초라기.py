import sys
input = sys.stdin.read
sys.setrecursionlimit(100000)

def expand(N, W, cost):
    a = [0] * N
    b = [0] * N
    c = [0] * N

    if cost[0][0] + cost[1][0] <= W:
        a[0] = b[0] = c[0] = 1
    else:
        a[0] = 2
        b[0] = c[0] = 1

    for i in range(1, N):
        a[i] = a[i - 1] + 2
        b[i] = c[i] = a[i - 1] + 1

        if cost[0][i] + cost[0][i - 1] <= W:
            b[i] = min(b[i], c[i - 1] + 1)

        if cost[1][i] + cost[1][i - 1] <= W:
            c[i] = min(c[i], b[i - 1] + 1)

        a[i] = min(a[i], b[i] + 1)
        a[i] = min(a[i], c[i] + 1)

        if cost[0][i] + cost[1][i] <= W:
            a[i] = min(a[i], a[i - 1] + 1)

        if i >= 2 and cost[0][i] + cost[0][i - 1] <= W and cost[1][i] + cost[1][i - 1] <= W:
            a[i] = min(a[i], a[i - 2] + 2)
        elif i == 1 and cost[0][i] + cost[0][i - 1] <= W and cost[1][i] + cost[1][i - 1] <= W:
            a[i] = min(a[i], 2)

    return a, b, c

def solve_single_case(N, W, cost):
    a, b, c = expand(N, W, cost)
    ans = a[N - 1]

    if N > 1:
        if cost[1][0] + cost[1][N - 1] <= W:
            original = (cost[1][0], cost[1][N - 1])
            cost[1][0], cost[1][N - 1] = W, W
            _, b_temp, _ = expand(N, W, cost)
            ans = min(ans, b_temp[N - 1])
            cost[1][0], cost[1][N - 1] = original

        if cost[0][0] + cost[0][N - 1] <= W:
            original = (cost[0][0], cost[0][N - 1])
            cost[0][0], cost[0][N - 1] = W, W
            _, _, c_temp = expand(N, W, cost)
            ans = min(ans, c_temp[N - 1])
            cost[0][0], cost[0][N - 1] = original

        if (cost[0][0] + cost[0][N - 1] <= W and cost[1][0] + cost[1][N - 1] <= W):
            original = (cost[0][0], cost[0][N - 1], cost[1][0], cost[1][N - 1])
            cost[0][0], cost[0][N - 1] = W, W
            cost[1][0], cost[1][N - 1] = W, W
            a_temp, _, _ = expand(N, W, cost)
            ans = min(ans, a_temp[N - 2])
            cost[0][0], cost[0][N - 1], cost[1][0], cost[1][N - 1] = original

    return ans

def main():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        W = int(data[idx + 1])
        idx += 2
        cost = [[], []]
        for i in range(2):
            cost[i] = list(map(int, data[idx:idx + N]))
            idx += N
        results.append(solve_single_case(N, W, cost))

    for res in results:
        print(res)

if __name__ == "__main__":
    main()