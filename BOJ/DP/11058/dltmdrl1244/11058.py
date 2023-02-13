n = int(input())
dp = [i for i in range(n+1)]

for i in range(3, n+1):
    for j in range(3, i-2):
        dp[i] = max(dp[i], dp[i-j] * (j-1))

print(dp[n])
