n = int(input())
for i in range(n) :
    for _ in range(n - i - 1) :
        print(" ", end = '')
    if (i == 0 or i == n - 1) :
        if (i == 0) :
            print("*", end = '')
        else :
            for __ in range(n * 2 - 1) :
                print("*", end = '')
    else :
        print("*", end = '')
        for _ in range((i * 2) - 1) :
            print(" ", end = '')
        print("*", end = '')        
    print()