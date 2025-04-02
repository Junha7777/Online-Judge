def can_spell_word(cookie_letters, word):
    from collections import Counter
    cookie_count = Counter(cookie_letters)
    word_count = Counter(word)
    for letter, count in word_count.items():
        if cookie_count[letter] < count:
            return "NO"
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    index = 0
    T = int(data[index].strip())
    index += 1
    results = []
    for _ in range(T):
        cookie_letters = data[index].strip()
        index += 1
        W = int(data[index].strip())
        index += 1
        for _ in range(W):
            word = data[index].strip()
            index += 1
            results.append(can_spell_word(cookie_letters, word))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()