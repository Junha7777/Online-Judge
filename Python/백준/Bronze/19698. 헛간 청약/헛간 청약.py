N, W, H, L = map(int, input().split())

width_fit = W // L
height_fit = H // L
total_fit = width_fit * height_fit

max_cows = min(total_fit, N)
print(max_cows)