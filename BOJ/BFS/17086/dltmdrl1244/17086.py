import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
board = []
sharks = []
q = deque()
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
visited = [[0] * w for _ in range(h)]
for i in range(h):
    tmp = list(map(int, input().split()))
    for j in range(w):
        if tmp[j] == 1:
            q.append((i, j))
            visited[i][j] = 0
    board.append(tmp)

ans = 0
while q:
    cy, cx = q.popleft()

    for i in range(8):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if 0 <= ny < h and 0 <= nx < w:
            if not board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = visited[cy][cx] + 1
                ans = max(ans, visited[cy][cx] + 1)
                q.append((ny, nx))

print(ans)