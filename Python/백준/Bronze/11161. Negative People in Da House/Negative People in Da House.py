def minimum_initial_people(test_cases):
    results = []
    for case in test_cases:
        M, movements = case
        min_people = 0
        current_people = 0
        for P1, P2 in movements:
            current_people += P1
            current_people -= P2
            if current_people < 0:
                min_people = max(min_people, -current_people)
        results.append(min_people)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    M = int(input())
    movements = [tuple(map(int, input().split())) for _ in range(M)]
    test_cases.append((M, movements))

results = minimum_initial_people(test_cases)

for result in results:
    print(result)