import sys
import itertools
from collections import deque
from copy import deepcopy


dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(board, it, n, empty):
    dq = deque(it)
    for y, x in it:
        board[y][x] = 1
    cnt = 1
    empty_cnt = 0
    while dq:
        for _ in range(len(dq)):
            y, x = dq.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == 0 or board[ny][nx] == 2):
                    board[ny][nx] = float('inf')
                    dq.append([ny, nx])
                    empty_cnt += 1
        if empty_cnt == empty:
            return cnt
        cnt += 1
    else:
        return 9999


def sol():
    n, m = map(int, sys.stdin.readline().split())
    board = [[b for b in map(int, sys.stdin.readline().split())] for _ in range(n)]
    board_ori = deepcopy(board)
    empty = 0
    pos = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                pos.append([i, j])
                empty += 1
            elif board[i][j] == 0:
                empty += 1
    empty -= m
    if empty == 0:
        print(0)
        exit(0)
    minimum = float('inf')
    for it in itertools.combinations(pos, m):
        temp = bfs(board, it, n, empty)
        minimum = temp if temp < minimum else minimum
        board = deepcopy(board_ori)
    print(minimum if minimum != 9999 else -1)


sol()
