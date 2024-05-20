def generate_sequences(N, M):
    def backtrack(start, sequence):
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return
        for i in range(start, N + 1):
            sequence.append(i)
            backtrack(i, sequence)
            sequence.pop()

    backtrack(1, [])

N, M = map(int, input().split())
generate_sequences(N, M)
