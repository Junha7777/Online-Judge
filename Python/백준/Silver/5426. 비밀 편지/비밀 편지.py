import sys
import math
input = sys.stdin.read

def decrypt_message(encrypted: str) -> str:
    length = len(encrypted)
    N = int(math.sqrt(length))

    matrix = [[''] * N for _ in range(N)]
    index = 0

    for i in range(N):
        for j in range(N):
            matrix[i][j] = encrypted[index]
            index += 1

    decrypted = []
    for col in range(N - 1, -1, -1):
        for row in range(N):
            decrypted.append(matrix[row][col])

    return ''.join(decrypted)

def main():
    input_data = input().splitlines()
    test_cases = int(input_data[0])
    results = []
    
    for i in range(1, test_cases + 1):
        encrypted_message = input_data[i]
        results.append(decrypt_message(encrypted_message))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()