import sys
input = sys.stdin.readline

input_string = input().rstrip()
N = len(input_string)

palindrome = [[False] * N for _ in range(N)]

# 길이가 1인 팰린드롬 검사
for i in range(0, N):
    palindrome[i][i] = True
# 길이가 2인 팰린드롬 검사
for i in range(0, N - 1):
    if input_string[i] == input_string[i + 1]:
        palindrome[i][i + 1] = True

# 길이가 3 이상인 팰린드롬 검사
for i in range(2, N):
    for j in range(0, N - i):
        if palindrome[j + 1][j + i - 1] and input_string[j] == input_string[j + i]:
            palindrome[j][j + i] = True

# dp로 최소 팰린드롬 갯수 구함
dp = [i for i in range(1, N + 1)]
for i in range(N):
    for e in range(N):
        if not palindrome[i][e]:
            continue

        if i == 0:
            dp[e] = min(dp[e], 1)
        else:
            dp[e] = min(dp[e], dp[i - 1] + 1)

print(dp[N - 1])
