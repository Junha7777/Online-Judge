import sys

def count_pairs(heights):
    stack = []
    count = 0

    for height in heights:
        same_height_count = 1

        while stack and stack[-1][0] <= height:
            h, c = stack.pop()
            count += c
            if h == height:
                same_height_count += c

        if stack:
            count += 1

        stack.append((height, same_height_count))

    return count

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    heights = list(map(int, data[1:]))

    print(count_pairs(heights))