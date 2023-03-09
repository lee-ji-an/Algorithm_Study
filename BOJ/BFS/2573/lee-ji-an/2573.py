import sys
from collections import deque

input = sys.stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
q = deque()
iceberg_cnt = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] > 0:
            board[i][j] = row[j]
            q.append((i, j))
            iceberg_cnt += 1


def end_check(iceberg_cnt):
    visited = [[False] * M for _ in range(N)]
    if len(q) == 0:
        return False
    y, x = q[0]
    q2 = deque([(y, x)])
    cnt = 1
    while q2:
        y, x = q2.popleft()
        visited[y][x] = True
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if visited[movey][movex]:
                continue
            visited[movey][movex] = True
            if board[movey][movex] > 0:
                cnt += 1
                q2.append((movey, movex))
    if cnt == iceberg_cnt:
        return False

    return True


def melting(iceberg_cnt):
    ans = 0
    while q:
        ans += 1
        new_board = [r[:] for r in board]
        for i in range(len(q)):
            y, x = q.popleft()
            sea_cnt = 0
            for d in range(4):
                movey = y + dy[d]
                movex = x + dx[d]
                if not(0 <= movey < N) or not(0 <= movex < M):
                    continue
                if new_board[movey][movex] == 0:
                    sea_cnt += 1
            if board[y][x] <= sea_cnt:
                board[y][x] = 0
                iceberg_cnt -= 1
            else:
                board[y][x] -= sea_cnt
                q.append((y, x))
        if end_check(iceberg_cnt):
            return ans

    return 0


print(melting(iceberg_cnt))
