import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
start_q = deque()


def start_point(row, col, num):
    start = set()
    q = deque()
    board[row][col] = num
    visited[row][col] = True
    q.append((row, col))
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                mv_r, mv_c = r + dr[d], c + dc[d]
                if not (0 <= mv_r < N) or not (0 <= mv_c < N):
                    continue
                if board[mv_r][mv_c] == 0:
                    start.add((r, c))
                    continue
                if visited[mv_r][mv_c]:
                    continue

                visited[mv_r][mv_c] = True
                board[mv_r][mv_c] = num
                q.append((mv_r, mv_c))

    return list(start)


def minimum_distance(start_points, num):
    new_visited = [row[:] for row in visited]
    q = deque(start_points)
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                mv_r, mv_c = r + dr[d], c + dc[d]
                if not (0 <= mv_r < N) or not (0 <= mv_c < N):
                    continue
                if new_visited[mv_r][mv_c]:
                    continue
                if board[mv_r][mv_c] != num and board[mv_r][mv_c] > 0:  # 나의 구역을 만난 것인지 확인해야 함
                    return cnt - 1

                new_visited[mv_r][mv_c] = True
                q.append((mv_r, mv_c))

    return float('inf')


cnt = float('inf')
num = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            num += 1
            start = start_point(i, j, num)
            res = minimum_distance(start, num)
            cnt = min(cnt, res)

print(cnt)
