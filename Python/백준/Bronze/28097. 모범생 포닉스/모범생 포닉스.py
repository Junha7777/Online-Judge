N = int(input())
study_times = list(map(int, input().split()))

total_study_time = sum(study_times)
total_rest_time = 8 * (N - 1)
total_time = total_study_time + total_rest_time

days = total_time // 24
hours = total_time % 24

print(days, hours)