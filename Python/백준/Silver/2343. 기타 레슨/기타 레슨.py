def can_record(lessons, m, size):
    count = 1
    current_sum = 0

    for lesson in lessons:
        if lesson > size:
            return False
        if current_sum + lesson > size:
            count += 1
            current_sum = 0
        current_sum += lesson

    return count <= m

def min_bluray_size(n, m, lessons):
    left = max(lessons)
    right = sum(lessons)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_record(lessons, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

N, M = map(int, input().split())
lessons = list(map(int, input().split()))
print(min_bluray_size(N, M, lessons))