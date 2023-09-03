import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for r in range(R):
    board.append(input().rstrip())

direction = [(-1, 1), (0, 1), (1, 1)]
visited = [[False] * C for _ in range(R)]
cnt = 0


def dfs(row, col):
    # 열의 제일 오른쪽에 도착했으면 파이프 설치 성공 / True를 리턴
    if col >= C - 1:
        return True

    # 가능하다면 위쪽으로 설치해야 함.
    # 오른쪽 위 / 오른쪽 / 오른쪽 아래로 탐색 -> 설치 가능한 경우의 수를 찾으면 즉시 종료
    for d in range(3):
        mv_r, mv_c = row + direction[d][0], col + 1
        if not (0 <= mv_r < R) or not (0 <= mv_c < C):
            continue
        if visited[mv_r][mv_c] or board[mv_r][mv_c] == 'x':
            continue
        visited[mv_r][mv_c] = True
        if dfs(mv_r, mv_c):
            return True  # 설치 가능한 경우의 수를 찾았으므로 즉시 종료
        # 탐색 후 visited를 False로 바꿀 필요 없음. 현재 위치에서 설치가 불가능하다면 다음 경우에도 마찬가지로 설치 불가능하기 때문
    else:
        return False


for r in range(R):
    if dfs(r, 0):
        cnt += 1

print(cnt)
