import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = []
visited = [[-1] * M for _ in range(N)]
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
DAY, NIGHT = True, False
for _ in range(N):
    board.append(list(map(int, list(input().rstrip()))))

def bfs():
    q = deque()
    q.append((0, 0, 1, K, DAY))
    visited[0][0] = K
    while q:
        y, x, cnt, wall, check = q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= M:
                continue
            if movey == N-1 and movex == M-1:
                return cnt+1
            if board[movey][movex] == 1 and wall > 0:
                if visited[movey][movex] < wall-1:
                    if check == DAY:
                        q.append((movey, movex, cnt+1, wall-1,  NIGHT))
                        visited[movey][movex] = wall-1
                    else:
                        q.append((y, x, cnt+1, wall, DAY))              # 벽을 부숴야하는데 밤이면
            elif board[movey][movex] == 0:
                if visited[movey][movex] < wall:
                    q.append((movey, movex, cnt+1, wall, not check))
                    visited[movey][movex] = wall
    return -1

def bfs2():
    q = deque()
    q.append((0, 0, 1, K))
    visited[0][0] = K
    while q:
        y, x, cnt, wall = q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= M:
                continue
            if movey == N-1 and movex == M-1:
                return cnt+1
            if board[movey][movex] == 1 and wall > 0:              # 벽을 부숴야하는 경우
                if visited[movey][movex] < wall-1:
                    if cnt % 2 == 1:                               # cnt % 2 == 1 -> 낮 / cnt % 2 == 0 -> 밤
                        q.append((movey, movex, cnt+1, wall-1))
                        visited[movey][movex] = wall-1
                    else:                                          # 벽을 부숴야하는데 밤이면 cnt 증가시켜 다시 큐에 넣음
                        q.append((y, x, cnt+1, wall))
            elif board[movey][movex] == 0:                         # 빈공간일 때
                if visited[movey][movex] < wall:
                    q.append((movey, movex, cnt+1, wall))
                    visited[movey][movex] = wall
    return -1


if N == 1 and M == 1:
    print(1)
else:
    print(bfs2())