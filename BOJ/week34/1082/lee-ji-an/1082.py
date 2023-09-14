import sys
input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))
M = int(input())

dp = [0] * (M + 1)

for n in range(N - 1, -1, -1):
    for j in range(price[n], M + 1):
        dp[j] = max(dp[j], n, dp[j - price[n]] * 10 + n)

print(dp[M])


# 2차원 배열을 사용하는 경우

# dp = [[0] * (M + 1) for _ in range(N + 1]
# for n in range(N - 1, -1, -1):
#     for m in range(1, min(price[n], M + 1)):
#         dp[n][m] = dp[n + 1][m]
#     for m in range(price[n], M + 1):
#         if m - price[n] >= 0:
#             dp[n][m] = max(dp[n][m - price[n]] * 10 + n,
#                            n, dp[n][m - 1], dp[n + 1][m])
#         else:
#             dp[n][m] = max(dp[n][m - 1], dp[n + 1][m])
# print(dp[M][0])