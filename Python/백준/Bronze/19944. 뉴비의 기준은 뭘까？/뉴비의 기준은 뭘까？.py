def classify_student(N, M):
    if M == 1 or M == 2:
        return "NEWBIE!"
    elif M <= N:
        return "OLDBIE!"
    else:
        return "TLE!"

N, M = map(int, input().split())

print(classify_student(N, M))
