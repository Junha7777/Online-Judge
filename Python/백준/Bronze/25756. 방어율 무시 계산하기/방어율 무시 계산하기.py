import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])

A = list(map(int, data[1:]))

current_ignore = 0.0

results = []

for a in A:
    percentage = a / 100
    current_ignore = 1 - (1 - current_ignore) * (1 - percentage)
    results.append(f"{current_ignore * 100:.6f}")

sys.stdout.write("\n".join(results) + "\n")