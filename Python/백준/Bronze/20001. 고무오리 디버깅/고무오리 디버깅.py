import sys

def rubber_duck_debugging():
    input()
    problem_count = 0
    
    while True:
        command = sys.stdin.readline().strip()
        
        if command == "고무오리 디버깅 끝":
            break
        elif command == "문제":
            problem_count += 1
        elif command == "고무오리":
            if problem_count > 0:
                problem_count -= 1
            else:
                problem_count += 2
    
    if problem_count == 0:
        print("고무오리야 사랑해")
    else:
        print("힝구")

rubber_duck_debugging()