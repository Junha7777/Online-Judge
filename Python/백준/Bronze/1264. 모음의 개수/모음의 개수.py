def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count

while True:
    line = input().strip()
    if line == '#':
        break
    print(count_vowels(line))
