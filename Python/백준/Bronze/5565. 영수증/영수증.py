total_price = int(input())
sum_books = sum(int(input()) for _ in range(9))
print(total_price - sum_books)