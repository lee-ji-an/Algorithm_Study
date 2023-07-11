import sys

delta = ((1, 0), (0, 1))  # down, right
N, M = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = 1

graph = [[[True, True] for _ in range(M+1)] for _ in range(N+1)]  # down, right 별로 갈 수 있는 길이 있는지 체크

K = int(sys.stdin.readline())

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a, c = min(a, c), max(a, c)
    b, d = min(b, d), max(b, d)

    d = 0 if c-a > d-b else 1
    graph[a][b][d] = False

for x in range(N+1):
    for y in range(M+1):
        for i in range(2):  # down, right
            nx, ny = x + delta[i][0], y + delta[i][1]
            if (nx <= N and ny <= M and graph[x][y][i]):  # 범위 내에 있고, 갈 수 있는 길이면
                dp[nx][ny] += dp[x][y]  # dp값 누적

print(dp[N][M])
