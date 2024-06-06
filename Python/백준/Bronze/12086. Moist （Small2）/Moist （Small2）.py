from bisect import bisect_left

def calculate_sorting_cost(cards):
    sorted_list = []
    cost = 0
    for card in cards:
        idx = bisect_left(sorted_list, card)
        if idx < len(sorted_list):
            cost += 1
        sorted_list.insert(idx, card)
    return cost

def main():
    T = int(input().strip())
    results = []
    for t in range(1, T + 1):
        N = int(input().strip())
        cards = [input().strip() for _ in range(N)]
        cost = calculate_sorting_cost(cards)
        results.append(f"Case #{t}: {cost}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()