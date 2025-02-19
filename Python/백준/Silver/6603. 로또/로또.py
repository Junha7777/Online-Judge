def generate_lotto(numbers, selected, start, target): 
    if len(selected) == target:  
        print(' '.join(map(str, selected)))
        return

    for i in range(start, len(numbers)):
        selected.append(numbers[i])
        generate_lotto(numbers, selected, i + 1, target)
        selected.pop()

while True:
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break

    k = input_data[0]
    numbers = input_data[1:]
    generate_lotto(numbers, [], 0, 6)
    print()