import sys
from collections import deque
input = sys.stdin.readline

VERTICAL, HORIZONTAL = True, False
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(input())

board = []
start_point = []
end_point = []
visited = set()
for i in range(N):
    board.append(list(input().rstrip()))
    for j in range(N):
        if board[i][j] == 'B':
            start_point.append((i, j))
            board[i][j] = '0'
        elif board[i][j] == 'E':
            end_point.append((i, j))
            board[i][j] = '0'


# U, D, L, R 방법으로 움직이는 게 가능한지 검사
def check(row, col, direction):
    if direction == VERTICAL:
        if not (1 <= row < N - 1):
            return False
        if board[row - 1][col] == '0' and board[row][col] == '0' and board[row + 1][col] == '0':
            return True
        else:
            return False
    else:
        if not (1 <= col < N - 1):
            return False
        if board[row][col - 1] == '0' and board[row][col] == '0' and board[row][col + 1] == '0':
            return True
        else:
            return False


# T 방법으로 움직이는 게 가능한지 검사
def turn_check(row, col):
    if not (1 <= row < N - 1) or not (1 <= col < N - 1):
        return False
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if board[i][j] != '0':
                return False
    return True


def bfs():
    q = deque()
    # q에 (row, col, direction, cnt) 형태로 넣음
    q.append((start[0], start[1], start[2], 0))
    # (row, col, direction) 형태를 set에 넣어서 visited 관리
    visited.add((start[0], start[1], start[2]))
    while q:
        row, col, direction, cnt = q.popleft()
        # 최종 위치에 도달하면 return
        if row == end[0] and col == end[1] and direction == end[2]:
            return cnt

        # U, D, L, R 방법으로 움직이는 경우
        for d in range(4):
            mv_r, mv_c = row + dr[d], col + dc[d]
            if not (0 <= mv_r < N) or not (0 <= mv_c < N):
                continue
            if (mv_r, mv_c, direction) in visited:
                continue

            if check(mv_r, mv_c, direction):
                visited.add((mv_r, mv_c, direction))
                q.append((mv_r, mv_c, direction, cnt + 1))

        # T 방법으로 움직이는 경우
        if (row, col, not direction) in visited:
            continue

        if turn_check(row, col):
            visited.add((row, col, not direction))
            q.append((row, col, not direction, cnt + 1))

    return 0


# 최종 위치의 방향을 구함 ( VERTICAL, HORIZONTAL )
if all(end_point[0][0] == num[0] for num in end_point):
    end = (end_point[1][0], end_point[1][1], HORIZONTAL)
else:
    end = (end_point[1][0], end_point[1][1], VERTICAL)

# 시작 위치의 방향을 구함 ( VERTICAL, HORIZONTAL )
if all(start_point[0][0] == num[0] for num in start_point):
    start = (start_point[1][0], start_point[1][1], HORIZONTAL)
else:
    start = (start_point[1][0], start_point[1][1], VERTICAL)

print(bfs())
