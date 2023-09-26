import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


# 외부 공기와 접촉하고 있는 곳을 표시
def bfs(start_point):
    q = deque(start_point)
    for r, c in start_point:
        visited[r][c] = True
    while q:
        row, col = q.popleft()
        for d in range(4):
            mv_row, mv_col = row + dr[d], col + dc[d]
            if not (0 <= mv_row < N) or not (0 <= mv_col < M):
                continue
            if visited[mv_row][mv_col] or board[mv_row][mv_col] == 1:
                continue
            visited[mv_row][mv_col] = True
            q.append((mv_row, mv_col))


visited = [[False] * M for _ in range(N)]
cheese = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese.add((i, j))

# (0, 0)을 시작으로 외부 공기와 접촉해 있는 곳 표시
bfs([(0, 0)])

# 치즈 녹이기
time = 0
while cheese:
    time += 1
    melting_cheese = set()
    for row, col in cheese:
        cnt = 0
        for d in range(4):
            mv_row, mv_col = row + dr[d], col + dc[d]
            if visited[mv_row][mv_col]:
                cnt += 1
                # 외부 공기와 접촉해 있는 변이 2개 이상이면 녹여야 함.
                if cnt == 2:
                    melting_cheese.add((row, col))
                    break
    # 외부 공기와 접촉해 있는 곳 / cheese 갱신
    # 치즈는 초마다 한꺼번에 녹으므로 한 번에 연산해줘야 합.
    cheese = cheese - melting_cheese
    for row, col in melting_cheese:
        board[row][col] = 0
    bfs(list(melting_cheese))

print(time)
