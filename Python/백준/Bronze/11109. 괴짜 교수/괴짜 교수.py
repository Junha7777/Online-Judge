import sys

input = sys.stdin.read

def main():
    data = input().splitlines()
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        d, n, s, p = map(int, data[i].split())
        parallel_cost = d + n * p
        serial_cost = n * s
        
        if parallel_cost < serial_cost:
            results.append("parallelize")
        elif parallel_cost > serial_cost:
            results.append("do not parallelize")
        else:
            results.append("does not matter")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()