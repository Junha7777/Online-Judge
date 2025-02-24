import math

D, H, W = map(int, input().split())

k = D / math.sqrt(H**2 + W**2)

height = H * k
width = W * k

print(math.floor(height), math.floor(width))
