import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
board.insert(0, 0)
# dp[i] = i번째 칸까지 가는데 최소 점프 횟수
dp = [float('inf')] * (n+1)
dp[1] = 0

for i in range(1, n+1):
    for j in range(1, board[i] + 1):
        if i + j < n + 1:
            # board[i] 만큼의 다음 칸을 살펴본다. 선형 탐색하면서 dp값을 최소로 갈아엎어준다.
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[n] != float('inf'):
    print(dp[n])
else:
    print(-1)