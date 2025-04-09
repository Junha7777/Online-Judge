import math
import sys
input = sys.stdin.readline

segment_tree = []
lazy = []

def update_lazy(left, right, node):
    if lazy[node] % 2 == 1:
        segment_tree[node] = (right - left + 1) - segment_tree[node]
        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def update_range(left, right, range_left, range_right, node):
    update_lazy(left, right, node)
    if range_right < left or right < range_left:
        return
    if range_left <= left and right <= range_right:
        segment_tree[node] = (right - left + 1) - segment_tree[node]
        if left != right:
            lazy[node * 2] += 1
            lazy[node * 2 + 1] += 1
        return
    mid = (left + right) // 2
    update_range(left, mid, range_left, range_right, node * 2)
    update_range(mid + 1, right, range_left, range_right, node * 2 + 1)
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

def sum_on_switch(left, right, range_left, range_right, node):
    update_lazy(left, right, node)
    if range_right < left or right < range_left:
        return 0
    if range_left <= left and right <= range_right:
        return segment_tree[node]
    mid = (left + right) // 2
    return sum_on_switch(left, mid, range_left, range_right, node * 2) + \
           sum_on_switch(mid + 1, right, range_left, range_right, node * 2 + 1)

def main():
    switch_num, M = map(int, input().split())
    tree_height = math.ceil(math.log2(switch_num))
    size = 1 << (tree_height + 1)
    global segment_tree, lazy
    segment_tree = [0] * size
    lazy = [0] * size
    for _ in range(M):
        O, S, T = map(int, input().split())
        if O == 0:
            update_range(1, switch_num, S, T, 1)
        else:
            print(sum_on_switch(1, switch_num, S, T, 1))

if __name__ == '__main__':
    main()