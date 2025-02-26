import heapq
import sys
input = sys.stdin.read

def max_stolen_value(N, K, jewels, bags):
    jewels.sort()
    bags.sort()
    
    max_value = 0
    jewel_index = 0
    value_heap = []
    
    for bag in bags:
        while jewel_index < N and jewels[jewel_index][0] <= bag:
            heapq.heappush(value_heap, -jewels[jewel_index][1])
            jewel_index += 1
        if value_heap:
            max_value -= heapq.heappop(value_heap)
    
    return max_value

data = input().split()
N = int(data[0])
K = int(data[1])
jewels = [(int(data[i*2+2]), int(data[i*2+3])) for i in range(N)]
bags = [int(data[N*2+2+i]) for i in range(K)]

print(max_stolen_value(N, K, jewels, bags))
