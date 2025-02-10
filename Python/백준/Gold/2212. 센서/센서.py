def min_sensor_range(n, k, sensors):
    sensors.sort()
    distances = []
    for i in range(1, n):
        distances.append(sensors[i] - sensors[i-1])
    distances.sort()
    result = sensors[-1] - sensors[0]

    for i in range(min(k-1, n-1)):
        result -= distances[-i-1]

    return max(0, result)

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
print(min_sensor_range(n, k, sensors))