import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sx, sy, ex, ey = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, +1, -2, +2, -1, +1]

def bfs():
    q = deque([(sx, sy, 0)])
    visited = [[False] * n for _ in range(n)]

    while q:
        cx, cy, cnt = q.popleft()

        if cx == ex and cy == ey:
            return cnt

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0<= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
    return -1

print(bfs())