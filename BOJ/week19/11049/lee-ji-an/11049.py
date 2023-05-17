import sys

input = sys.stdin.readline

N = int(input())

matrix = []
dp = [[0] * N for _ in range(N)]
cnt = float('inf')

for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(N - i):
        start, end = j, j + i
        for k in range(0, i):
            cnt = min(
                cnt, dp[start][start + k] + dp[start + k + 1][end] +
                     matrix[start][0] * matrix[start + k][1] * matrix[end][1]
            )
        dp[start][end] = cnt

print(dp[0][N - 1])
