import sys

n = int(sys.stdin.readline().strip())
board = [b for b in map(int, sys.stdin.readline().split())]
dp = [float('inf')] * n
dp[0] = 0
for i in range(n):
    for j in range(1, board[i] + 1):        # board[i]에 있는 숫자만큼 점프할 수 있음
        if i + j < n:       # 범위를 벗어나지 않는다면
            dp[i + j] = min(dp[i + j], dp[i] + 1)       # i + j까지 가는데 기존에 점프한 횟수와 dp[i]에서 한 번 점프하는 것을 비교

if dp[n - 1] == float('inf'):
    print(-1)
else:
    print(dp[n - 1])
