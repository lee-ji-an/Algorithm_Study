import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
board = []
visited = [[set() for _ in range(M)] for _ in range(N)]
for n in range(N):
    row = input().rstrip()
    board.append(list(row))
    for m in range(M):
        if row[m] == '0':
            start_point = (n, m)
            board[n][m] = '.'


def bfs():
    q = deque([(start_point[0], start_point[1], 0, 0)])
    visited[start_point[0]][start_point[1]].add(0)
    while q:
        row, col, cnt, key = q.popleft()
        for d in range(4):
            mv_row, mv_col = row + dr[d], col + dc[d]
            if not(0 <= mv_row < N) or not(0 <= mv_col < M):
                continue
            if board[mv_row][mv_col] == '#' or key in visited[mv_row][mv_col]:
                continue
            if board[mv_row][mv_col] == '1':
                return cnt + 1

            visited[mv_row][mv_col].add(key)
            if 0 <= ord(board[mv_row][mv_col]) - ord('a') <= 5:  # a ~ f
                q.append((mv_row, mv_col, cnt + 1, key | (1 << ord(board[mv_row][mv_col]) - ord('a'))))
            elif 0 <= ord(board[mv_row][mv_col]) - ord('A') <= 5:   # A ~ F
                if 1 & (key >> ord(board[mv_row][mv_col]) - ord('A')) == 1:
                    q.append((mv_row, mv_col, cnt + 1, key))
            else:  # .
                q.append((mv_row, mv_col, cnt + 1, key))

    return -1


print(bfs())
