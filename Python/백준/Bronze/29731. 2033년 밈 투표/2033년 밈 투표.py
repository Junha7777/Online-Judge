N = int(input())
astley_pledge = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

changed = False

for _ in range(N):
    pledge = input().strip()
    if pledge not in astley_pledge:
        changed = True
        break

if changed:
    print("Yes")
else:
    print("No")
