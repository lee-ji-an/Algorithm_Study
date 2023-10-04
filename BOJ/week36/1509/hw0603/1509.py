import sys

S = sys.stdin.readline().strip()
L = len(S)

dp = [sys.maxsize for _ in range(L)]
isPalindrome = [[False]*L for _ in range(L)]

# 길이가 1인 팰린드롬
for i in range(L):
    isPalindrome[i][i] = True

# 길이가 2인 팰린드롬
for i in range(1, L):
    if (S[i-1] == S[i]):
        isPalindrome[i-1][i] = True

# 길이가 3 이상인 팰린드롬 -> 점화식 사용
# 처음과 끝이 동일하고 그 사이가 팰린드롬이면 전체가 팰린드롬
for l in range(3, L+1):  # 길이: 3~L
    for start in range(L-l+1):
        end = start + l - 1
        if (S[start] == S[end] and isPalindrome[start+1][end-1]):
            isPalindrome[start][end] = True

# 분할에 대한 DP
# start~end가 팰린드롬이면 (start 전까지의 분할 수)+1, 아니면 (end 전까지의 분할 수)+1
for end in range(L):
    # 0~end가 이미 팰린드롬이면 더 볼 필요도 없이 1로 확정
    if (isPalindrome[0][end]):
        dp[end] = 1
        continue

    for start in range(1, end+1):
        dp[end] = min(
            dp[end],
            dp[start-1]+1 if isPalindrome[start][end] else dp[end-1]+1
        )

print(dp[-1])
