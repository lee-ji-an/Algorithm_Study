import sys
from collections import deque
input = sys.stdin.readline

# n 세로 m 가로
n, m = map(int, input().split())
board = []
ry, rx, by, bx = 0, 0, 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
visited = []
for i in range(n):
    tmp = list(input().rstrip())
    board.append(tmp)
    for j in range(m):
        if tmp[j] == 'R':
            ry, rx = i, j
        if tmp[j] == 'B':
            by, bx = i, j

def move(y, x, i):
    cnt = 0
    while board[y + dy[i]][x + dx[i]] != '#' and board[y][x] != 'O':
        y += dy[i]
        x += dx[i]
        cnt += 1
    return y, x, cnt

def bfs():
    while q:
        cry, crx, cby, cbx, cnt = q.popleft()
        if cnt > 10:
            break

        for i in range(4):
            nby, nbx, bcnt = move(cby, cbx, i)
            nry, nrx, rcnt = move(cry, crx, i)
            if board[nby][nbx] != 'O':
                if board[nry][nrx] == 'O':
                    print(cnt)
                    return

                if nry == nby and nrx == nbx:
                    if bcnt < rcnt:
                        nry -= dy[i]
                        nrx -= dx[i]
                    else:
                        nby -= dy[i]
                        nbx -= dx[i]

                if [nry, nrx, nby, nbx] not in visited:
                    visited.append([nry, nrx, nby, nbx])
                    q.append([nry, nrx, nby, nbx, cnt + 1])

    print(-1)
    return

q.append([ry, rx, by, bx, 1])
visited.append([ry, rx, by, bx])
bfs()