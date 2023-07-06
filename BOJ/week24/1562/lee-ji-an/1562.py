import sys
input = sys.stdin.readline

N = int(input())

dp = [[[0] * 10 for _ in range((1 << 10) + 1)] for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][1 << i][i] = 1

for i in range(2, N + 1):
    for j in range(1 << 10):
        for k in range(10):
            if dp[i - 1][j][k] == 0:
                continue
            if 0 <= k + 1 <= 9:
                dp[i][j | (1 << (k + 1))][k + 1] += dp[i - 1][j][k]
            if 0 <= k - 1 <= 9:
                dp[i][j | (1 << (k - 1))][k - 1] += dp[i - 1][j][k]

print(sum(dp[N][0b1111111111]) % 1000000000)

