import sys

initial_string = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

left_stack = list(initial_string)
right_stack = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    
    if command == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    
    elif command == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    
    elif command == "B":
        if left_stack:
            left_stack.pop()
    
    elif command.startswith("P"):
        _, char = command.split()
        left_stack.append(char)

sys.stdout.write("".join(left_stack + right_stack[::-1]) + "\n")