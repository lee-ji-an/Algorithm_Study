import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
board = []
target = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

for i in range(h):
    tmp = list(input().rstrip())
    for j in range(w):
        if tmp[j] == 'C':
            target.append((i, j))
    board.append(tmp)

q = deque()
# 이 점에 방문할 때까지의 최소 커브 횟수
visited = [[float('inf')] * w for _ in range(h)]

q.append((target[0][0], target[0][1], 0, None))
visited[target[0][0]][target[0][1]] = 0

while q:
    # was_vertical : 이전의 움직임이 수직, 즉 상하 움직임이었는지의 True/False
    cy, cx, curves, was_vertical = q.popleft()

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] in ('.', 'C'):
                # 이전이 None이거나 (첫 시행이거나), 이전이 수직이고 이번도 수직 or 이전이 수직이아니고 이번도 수직이아님
                # 이 경우에는 커브 횟수를 증가시키지 않고 넣는다
                if (was_vertical is None) or ((was_vertical and i in (0, 3)) or (not was_vertical and i in (1, 2))):
                    # 만약 더 적게 커브를 돌고 방문 가능하다면
                    if visited[ny][nx] > curves:
                        visited[ny][nx] = curves
                        q.append((ny, nx, curves, True if i in (0, 3) else False))
                # 이전이 수직이고 이번이 수직이아님 or 이전이 수직이아니고 이번이 수직
                else:
                    # 만약 더 적게 커브를 돌고 방문 가능하다면
                    if visited[ny][nx] > curves:
                        visited[ny][nx] = curves + 1
                        q.append((ny, nx, curves + 1, True if i in (0, 3) else False))

print(visited[target[1][0]][target[1][1]])