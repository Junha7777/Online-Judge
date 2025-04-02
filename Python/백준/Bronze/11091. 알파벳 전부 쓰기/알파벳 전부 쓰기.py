import sys
import string

def check_pangram(sentence):
    sentence = sentence.lower()
    alphabet_set = set(string.ascii_lowercase)
    present_letters = set(sentence) & alphabet_set
    
    if present_letters == alphabet_set:
        return "pangram"
    else:
        missing_letters = "".join(sorted(alphabet_set - present_letters))
        return f"missing {missing_letters}"

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        sentence = sys.stdin.readline().strip()
        print(check_pangram(sentence))
