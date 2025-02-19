def check_numbers(n, cards, m, numbers):
    card_set = set(cards)
    result = []

    for num in numbers:
        if num in card_set:
            result.append(1)
        else:
            result.append(0)

    return ' '.join(map(str, result))

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

print(check_numbers(N, cards, M, numbers))