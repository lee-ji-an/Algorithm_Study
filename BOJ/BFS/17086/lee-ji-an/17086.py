import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
babyShark = []
dx = (0, 0, -1, 1, -1, 1, 1, -1)
dy = (-1, 1, 0, 0, -1, -1, 1, 1)

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            board[i][j] = 1
            babyShark.append((i, j))


def bfs():      # 아기 상어의 모든 위치에서 multisourceBFS
    visited = [[False] * M for _ in range(N)]
    maxDist = 0
    q = deque()
    for shark in babyShark:
        q.append((shark[0], shark[1], 0))
        visited[shark[0]][shark[1]] = True
    while q:
        y, x, cnt = q.popleft()
        for i in range(8):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= M:
                continue
            if not visited[movey][movex]:
                maxDist = max(maxDist, cnt+1)
                q.append((movey, movex, cnt+1))
                visited[movey][movex] = True
    return maxDist
print(bfs())