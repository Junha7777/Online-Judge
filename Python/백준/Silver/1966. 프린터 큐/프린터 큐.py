from collections import deque

def get_print_order(documents, target_index):
    queue = deque(enumerate(documents))
    priority_list = sorted(documents, reverse=True)
    print_order = 0
    
    while queue:
        doc_index, priority = queue.popleft()
        if priority == priority_list[0]:
            print_order += 1
            priority_list.pop(0)
            if doc_index == target_index:
                return print_order
        else:
            queue.append((doc_index, priority))

test_cases = int(input())

for _ in range(test_cases):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    print(get_print_order(documents, M))
