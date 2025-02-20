from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
houses = []
chickens = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

chicken_combinations = list(combinations(chickens, m))
min_chicken_distance = float('inf')

for selected_chickens in chicken_combinations:
    city_chicken_distance = 0
    
    for hr, hc in houses:
        house_chicken_distance = min(abs(hr - cr) + abs(hc - cc) for cr, cc in selected_chickens)
        city_chicken_distance += house_chicken_distance
    
    min_chicken_distance = min(min_chicken_distance, city_chicken_distance)

print(min_chicken_distance)