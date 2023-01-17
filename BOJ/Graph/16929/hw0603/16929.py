import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

ans = False

# 사이클이 존재하는지 확인하는 함수
def dfs(type: str, row: int, col: int, initPos: tuple, cnt: int=1) -> None:
    global ans
    # 이미 사이클을 찾았다면 종료
    if (ans):
        return
    # 4가지 방향에 대하여
    for i in range(4):
        # 상하좌우 인접한 다음 좌표 구함
        n_row, n_col = row + dr[i], col + dc[i]
        # 새 좌표가 board 범위를 벗어난 경우 skip
        if not (0 <= n_row < N and 0 <= n_col < M):
            continue

        # cnt(연결된 점 개수)가 4 이상이면서 사이클이 만들어진 경우
        if ((n_row, n_col) == initPos and cnt >= 4):
            # 정답 표시
            ans = True
            return
        # 해당 지점을 방문하지 않았고, 타입이 동일한 경우 -> 그 방향으로 전진 가능
        if (board[n_row][n_col] == type and not visited[n_row][n_col]):
            visited[n_row][n_col] = True  # 방문 처리
            dfs(type, *(n_row, n_col), initPos, cnt+1)
            visited[n_row][n_col] = False  # 방문 처리 해제

for i in range(N):
    for j in range(M):
        visited[i][j] = True  # 방문 처리
        dfs(board[i][j], *(i, j), (i, j))
        if (ans):
            print("Yes")
            sys.exit()

print("No")
