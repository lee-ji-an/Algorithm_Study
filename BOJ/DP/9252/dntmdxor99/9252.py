s1, s2 = input().strip(), input().strip()
l1, l2 = len(s1), len(s2)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]        # dp[s1][s2]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if s1[i - 1] == s2[j - 1]:      # 같다면 이전 수열의 값 + 1
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:       # 다르다면 이전 수열 중에 최댓값을 찾으면 됨
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

max_str = ''
sy, sx = l1, l2
while True:     # 역추적해서 문자열을 찾음
    if sy == 0 or sx == 0:
        break
    if dp[sy][sx] == dp[sy - 1][sx]: sy -= 1        # 값이 같다면 위로
    elif dp[sy][sx] == dp[sy][sx - 1]: sx -= 1      # 값이 같다면 아래로
    else:       # 대각선과 값이 같다는 것은 문자도 공통된 것이므로 문자열에 추가함
        sy -= 1
        sx -= 1
        max_str = s1[sy] + max_str


print(dp[l1][l2])
print(max_str)