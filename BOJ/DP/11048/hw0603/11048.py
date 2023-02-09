import sys

d = ((-1, 0), (0, -1))
N, M = map(int, sys.stdin.readline().split())
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        maxval = 0
        for dr, dc in d:
            nr, nc = i+dr, j+dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            maxval = max(maxval, dp[nr][nc])
        
        dp[i][j] = candy[i][j] + maxval

print(dp[-1][-1])
