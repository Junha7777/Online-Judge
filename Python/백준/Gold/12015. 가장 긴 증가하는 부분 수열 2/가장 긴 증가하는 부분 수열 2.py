from bisect import bisect_left
import sys

def longest_increasing_subsequence(arr):

    if not arr:
        return 0

    lis = []
    for num in arr:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

    return len(lis)

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(longest_increasing_subsequence(A))