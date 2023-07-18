import sys

sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]

d = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 1


def dfs(row, col):
    global ans

    # 이미 방문한 좌표라면 그 지점의 dp값부터 시작: 조기 반환
    if (dp[row][col] != -1):
        return dp[row][col]
    dp[row][col] = 1  # 초기 방문 처리

    # 4방향 탐색
    for dr, dc in d:
        nrow, ncol = row+dr, col+dc
        if not (0 <= nrow < N and 0 <= ncol < N):  # 범위밖 Skip
            continue
        if (matrix[row][col] < matrix[nrow][ncol]):
            cnt = 1
            cnt += dfs(nrow, ncol)
            dp[row][col] = max(dp[row][col], cnt)  # 재귀 스택 풀리는 지점 기준으로 거리 갱신
            ans = max(ans, dp[row][col])  # 최댓값 갱신
    return dp[row][col]


# 각 좌표에 대해 DFS 탐색 수행
for i in range(N):
    for j in range(N):
        if (dp[i][j] == -1):
            dfs(i, j)

print(ans)
