import sys

def determine_winner(scores):
    yonsei_score = 0
    korea_score = 0
    
    for score in scores:
        y, k = map(int, score.split())
        yonsei_score += y
        korea_score += k
    
    if yonsei_score > korea_score:
        return "Yonsei"
    elif korea_score > yonsei_score:
        return "Korea"
    else:
        return "Draw"

def main():
    input_data = sys.stdin.read
    data = input_data().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        scores = data[index:index+9]
        results.append(determine_winner(scores))
        index += 9
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()