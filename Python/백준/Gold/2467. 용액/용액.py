import sys

def find_closest_to_zero(N, solutions):
    left, right = 0, N - 1
    best_pair = (solutions[left], solutions[right])
    min_abs_sum = abs(solutions[left] + solutions[right])

    while left < right:
        current_sum = solutions[left] + solutions[right]

        if abs(current_sum) < min_abs_sum:
            min_abs_sum = abs(current_sum)
            best_pair = (solutions[left], solutions[right])

        if current_sum == 0:
            return best_pair

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return best_pair

N = int(sys.stdin.readline().strip())
solutions = list(map(int, sys.stdin.readline().split()))

result = find_closest_to_zero(N, solutions)
print(result[0], result[1])