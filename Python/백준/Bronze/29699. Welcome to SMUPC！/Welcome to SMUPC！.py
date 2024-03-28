def find_nth_character_in_label(N):
    label = "WelcomeToSMUPC"
    index = (N - 1) % len(label)
    return label[index]

N = int(input())
result = find_nth_character_in_label(N)
print(result)  # Output: W
