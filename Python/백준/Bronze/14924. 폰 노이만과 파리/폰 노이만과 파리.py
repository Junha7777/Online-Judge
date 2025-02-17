S, T, D = map(int, input().split())
meeting_time = D / (2 * S)
fly_distance = T * meeting_time
print(int(fly_distance))