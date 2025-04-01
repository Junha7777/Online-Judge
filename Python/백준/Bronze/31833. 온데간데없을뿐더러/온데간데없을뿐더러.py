def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = data[1:N+1]
    B = data[N+1:2*N+1]
    
    X = ''.join(A)
    Y = ''.join(B)
    
    print(min(int(X), int(Y)))

if __name__ == "__main__":
    main()