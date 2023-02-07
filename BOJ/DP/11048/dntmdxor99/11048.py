import sys

n, m = map(int, sys.stdin.readline().split())
board = [[b for b in map(int, sys.stdin.readline().split())] for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]      # 맨 위쪽, 맨 왼쪽으로만 이동해야 하는 경우도 있으므로 한 칸 더 추가해줌
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = board[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])      # 항상 최댓값을 찾아가면 됨
print(dp[n][m])