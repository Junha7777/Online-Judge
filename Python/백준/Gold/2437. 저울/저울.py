def find_min_unmeasurable_weight(weights):
    weights.sort()
    min_weight = 1
    for weight in weights:
        if weight > min_weight:
            break
        min_weight += weight
    return min_weight

input()
weights = list(map(int, input().split()))
print(find_min_unmeasurable_weight(weights))