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
    # prev : 이전의 움직임
    cy, cx, curves, prev = q.popleft()

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] != '*':
                if prev is not None and i == 3 - prev:
                    continue

                # 이전이 None이거나 (첫 시행이거나), 이전과 같은 방향으로의 진행
                # 이 경우에는 커브 횟수를 증가시키지 않고 넣는다
                if prev is None or i == prev:
                    if visited[ny][nx] >= curves:
                        visited[ny][nx] = curves
                        q.append((ny, nx, curves, i))

                # 이전과 다른 방향으로의 진행
                else:
                    if visited[ny][nx] >= curves + 1:
                        visited[ny][nx] = curves + 1
                        q.append((ny, nx, curves + 1, i))

print(visited[target[1][0]][target[1][1]])