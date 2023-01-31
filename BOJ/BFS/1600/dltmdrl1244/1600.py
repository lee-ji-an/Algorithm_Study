import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

hdy = [-2, -1, 1, 2, 2, 1, -1, -2]
hdx = [1, 2, 2, 1, -1, -2, -2, -1]

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def bfs():
    q = deque()
    # '말 이동' 을 한 횟수
    visited = [[float('inf')] * w for _ in range(h)]
    q.append((0, 0, 0))
    visited[0][0] = 0

    while q:
        cy, cx, cnt = q.popleft()

        if visited[cy][cx] < k:
            for i in range(8):
                ny = cy + hdy[i]
                nx = cx + hdx[i]

                if 0 <= ny < h and 0 <= nx < w:
                    # 말 이동 횟수를 줄일 수 있으면 큐에 넣는다
                    if board[ny][nx] != 1 and visited[ny][nx] > visited[cy][cx] + 1:
                        if (ny, nx) == (h-1, w-1):
                            return cnt + 1

                        visited[ny][nx] = visited[cy][cx] + 1
                        q.append((ny, nx, cnt + 1))

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if board[ny][nx] != 1 and visited[ny][nx] > visited[cy][cx]:
                    if (ny, nx) == (h-1, w-1):
                        return cnt + 1

                    visited[ny][nx] = visited[cy][cx]
                    q.append((ny, nx, cnt + 1))

    return -1

if (w, h) == (1, 1):
    print(0)
else:
    print(bfs())