import sys
from collections import deque

input = sys.stdin.readline
W, H = map(int, input().split())
board = []
dy = (-1, 1, 0, 0)  # 상 하 좌 우
dx = (0, 0, -1, 1)
starty, startx, endy, endx = -1, -1, -1, -1
for i in range(H):
    board.append(input().rstrip())
    for j in range(W):
        if board[i][j] == 'C':
            if starty == -1:
                starty = i
                startx = j
            else:
                endy = i
                endx = j

def bfs():
    q = deque()
    visited = [[float('inf')] * W for _ in range(H)]
    q.append((starty, startx, -1, 0))
    visited[starty][startx] = 0
    while q:
        y, x, prev, corner= q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if prev == i:
                continue
            if prev == 0 or prev == 2:
                if prev+1 == i:
                    continue
            else:
                if prev-1 == i:
                    continue
            while True:
                if movey < 0 or movey >= H or movex < 0 or movex >= W:
                    break
                if board[movey][movex] == '*' or visited[movey][movex] < corner+1:
                    break
                if endy == movey and endx == movex:
                    return corner
                visited[movey][movex] = corner+1
                q.append((movey, movex, i, corner + 1))
                movey = movey + dy[i]
                movex = movex + dx[i]


print(bfs())