import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)  # 상 하 좌 우
START, GARBAGE, FLOWER, G_AROUND, EMPTY = 0, 1, 2, 3, -1
board = [[EMPTY] * M for _ in range(N)]
garbage_set = set()
visited = [[False] * M for _ in range(N)]
heap = []


def bfs(start_point):
    heapq.heappush(heap, (0, 0, start_point[0], start_point[1]))
    visited[start_point[0]][start_point[1]] = 0
    while heap:
        garbage_cnt, garbage_around_cnt, y, x = heapq.heappop(heap)
        for i in range(4):
            movey, movex = y + dy[i], x + dx[i]
            new_g_cnt, new_a_cnt = garbage_cnt, garbage_around_cnt

            if not ((0 <= movey < N) and (0 <= movex < M)) or visited[movey][movex]:
                continue
            if board[movey][movex] == FLOWER:
                return garbage_cnt, garbage_around_cnt

            visited[movey][movex] = True
            if board[movey][movex] == GARBAGE:
                new_g_cnt += 1
            elif board[movey][movex] == G_AROUND:
                new_a_cnt += 1
            heapq.heappush(heap, (new_g_cnt, new_a_cnt, movey, movex))


for i in range(N):
    row = input().rstrip()
    for j in range(M):
        if row[j] == 'S':
            start = (i, j)
            board[i][j] = START
        elif row[j] == 'g':
            garbage_set.add((i, j))
            board[i][j] = GARBAGE
        elif row[j] == 'F':
            flower = (i, j)
            board[i][j] = FLOWER

# 쓰레기 주위 부분 표시
for y, x in garbage_set:
    for i in range(4):
        movey, movex = y + dy[i], x + dx[i]
        if not ((0 <= movey < N) and (0 <= movex < M)) or board[movey][movex] != EMPTY:
            continue
        board[movey][movex] = G_AROUND

ans = bfs(start)
print(ans[0], ans[1])
