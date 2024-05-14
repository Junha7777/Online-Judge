def solve_n_queens(n):
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if not (cols[col] or diags1[row + col] or diags2[row - col]):
                cols[col] = diags1[row + col] = diags2[row - col] = True
                backtrack(row + 1)
                cols[col] = diags1[row + col] = diags2[row - col] = False
    
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)
    diags2 = [False] * (2 * n - 1)
    count = 0
    backtrack(0)
    return count

n = int(input())
print(solve_n_queens(n))