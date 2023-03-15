import sys
from collections import deque
input = sys.stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited_origin = [[False] * M for _ in range(N)]
cheese_cnt = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            cheese_cnt += 1
            board[i][j] = 1


def bfs(cheese_cnt):
    time = 0
    while cheese_cnt != 0:
        prev = cheese_cnt
        time += 1
        visited = [r[:] for r in visited_origin]
        q = deque([(0, 0)])
        visited[0][0] = True
        while q:
            y, x = q.popleft()
            for i in range(4):
                movey = y + dy[i]
                movex = x + dx[i]
                if not (0 <= movey < N) or not (0 <= movex < M):
                    continue
                if visited[movey][movex]:
                    continue
                visited[movey][movex] = True
                if board[movey][movex] == 1:
                    board[movey][movex] = 0
                    cheese_cnt -= 1
                else:
                    q.append((movey, movex))

    return time, prev


T, P = bfs(cheese_cnt)
print(T)
print(P)
