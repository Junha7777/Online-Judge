def check_cheater(n, before_cards, after_cards):
    before_cards.sort()
    after_cards.sort()
    
    if before_cards == after_cards:
        return "NOT CHEATER"
    else:
        return "CHEATER"

T = int(input())

for _ in range(T):
    n = int(input())
    before_cards = input().split()
    after_cards = input().split()
    
    print(check_cheater(n, before_cards, after_cards))
