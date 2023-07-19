import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    phone_number = []
    ans = "YES"
    for j in range(N):
        phone_number.append(input().rstrip())
    phone_number.sort()

    for i in range(N - 1):
        if phone_number[i] == phone_number[i + 1][:len(phone_number[i])]:
            ans = "NO"
            break

    print(ans)
