n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
for i in range(1, k + 1):       # k + 1까지 찾아야 함
    mins = float('inf')     # 최소를 위해
    for j in c:
        if j <= i and dp[i - j] != -1:      # 찾을 수 없거나, j가 i보다 크면 min 값을 갱신하지 않음
            mins = min(mins, dp[i - j])
    dp[i] = mins + 1 if mins != float('inf') else -1        # 만약 갱신이 안 되었다면, 찾을 수 없는 것이므로 -1
print(dp[k])
