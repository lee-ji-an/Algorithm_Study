n = int(input())
dp = [*range(0, 6)]
for i in range(6, n + 1):
    dp[i % 6] = max(2 * dp[(i - 3) % 6], 3 * dp[(i - 4) % 6], 4 * dp[(i - 5) % 6])
print(dp[n % 6])