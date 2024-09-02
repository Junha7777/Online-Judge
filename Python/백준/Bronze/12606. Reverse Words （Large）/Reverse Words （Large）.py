def reverse_words_in_cases():
    N = int(input().strip())
    for i in range(1, N + 1):
        words = input().strip().split()
        reversed_words = ' '.join(words[::-1])
        print(f"Case #{i}: {reversed_words}")

reverse_words_in_cases()