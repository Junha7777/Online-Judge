def affine_cipher(a, b, s):
    def encrypt_char(c):
        X = ord(c) - ord('A')
        return chr((a * X + b) % 26 + ord('A'))
    
    return ''.join(encrypt_char(c) for c in s)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        a, b = map(int, data[index].split())
        s = data[index + 1]
        index += 2
        results.append(affine_cipher(a, b, s))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()