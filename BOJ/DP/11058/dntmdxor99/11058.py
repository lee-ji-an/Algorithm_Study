n = int(input())
dp = [*range(0, n + 1)]
for i in range(6, n + 1):
    dp[i] = max(2 * dp[i - 3], 3 * dp[i - 4], 4 * dp[i - 5])
print(dp[n])