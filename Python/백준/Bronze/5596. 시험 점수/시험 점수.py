min_gook_scores = list(map(int, input().split()))
man_se_scores = list(map(int, input().split()))

min_gook_total = sum(min_gook_scores)
man_se_total = sum(man_se_scores)

print(max(min_gook_total, man_se_total))
