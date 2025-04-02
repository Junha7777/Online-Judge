def count_leftcoming_cars(n, test_cases):
    results = []
    for i in range(n):
        m, left_times, right_times = test_cases[i]
        left_times_set = set(left_times)
        right_times_set = set(right_times)
        count = 0
        for t in left_times:
            if (t + 1000) in right_times_set and (t + 1500) in right_times_set:
                count += 1
        results.append(count)
    return results

import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
test_cases = []
for _ in range(n):
    m = int(data[index])
    index += 1
    left_times = list(map(int, data[index:index + m]))
    index += m
    right_times = list(map(int, data[index:index + m]))
    index += m
    test_cases.append((m, left_times, right_times))

results = count_leftcoming_cars(n, test_cases)
for result in results:
    print(result)