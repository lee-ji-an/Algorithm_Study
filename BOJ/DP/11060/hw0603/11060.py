import sys

INF = float('inf')
N = int(sys.stdin.readline())
maze = list(map(int, sys.stdin.readline().split()))
dp = [0] + [INF] * (N-1)  # maze[0]은 점프 안 해도 도달할 수 있으므로
checked = set()

for i in range(N):
    for j in range(1, maze[i]+1):
        if (i+j in checked):  # 이미 방문했던 곳이면 더 보지 않음
            continue
        try:
            dp[i+j] = dp[i]+1
        except IndexError:
            sys.exit(print(dp[-1] if not dp[-1] == INF else -1))
        checked.add(i+j)  # 방문 처리
print(dp[-1] if not dp[-1] == INF else -1)
