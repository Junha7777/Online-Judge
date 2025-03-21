import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
power_strips = list(map(int, data[1:]))
max_devices = sum(power_strips) - (n - 1)
print(max_devices)
