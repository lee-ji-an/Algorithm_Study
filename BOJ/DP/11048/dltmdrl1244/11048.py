import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j] = (i, j) 칸까지 도달할 때 먹을 수 있는 최대 사탕 개수
dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]

for i in range(n):
    for j in range(m):
        # 위와 왼쪽 칸에는 이미 대각선을 방문하여 갱신된 값이 들어가 있으므로 상, 좌만 봐도 된다
        # if i-1 >= 0 and j-1 >= 0:
        #     dp[i][j] = max(dp[i-1][j-1] + board[i][j], dp[i][j])
        if i-1 >= 0:
            dp[i][j] = max(dp[i-1][j] + board[i][j], dp[i][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j-1] + board[i][j], dp[i][j])

print(dp[n-1][m-1])