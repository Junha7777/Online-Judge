def min_waiting_time(n, times):
    times.sort()
    
    total_waiting_time = 0
    current_waiting_time = 0
    
    for time in times:
        current_waiting_time += time
        total_waiting_time += current_waiting_time
    
    return total_waiting_time

n = int(input())
times = list(map(int, input().split()))

print(min_waiting_time(n, times))