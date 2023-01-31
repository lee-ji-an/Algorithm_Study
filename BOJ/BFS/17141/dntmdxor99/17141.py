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
        if empty_cnt == empty:      # 만약 모든 공간이 채워진다면 그대로 cnt를 반환함
            return cnt
        cnt += 1        # cnt는 모든 바이러스가 한 칸씩 번졌을 때, 1씩 증가함
    else:
        return 9999     # 만약 바이러스가 모두 퍼지지 않았을 때는 9999를 반환함


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
                empty += 1      # 바이러스를 넣을 수 있는 공간도 채워야 하는 공간으로 처리함
            elif board[i][j] == 0:
                empty += 1
    empty -= m      # 바이러스를 놓고, 나머지 내가 채워야 하는 공간의 개수
    if empty == 0:      # 채워야 하는 공간의 개수가 0이라면 0초가 걸림
        print(0)
        exit(0)
    minimum = float('inf')
    for it in itertools.combinations(pos, m):       # 모든 조합을 짜서 바이러스를 넣어봄
        temp = bfs(board, it, n, empty)
        minimum = temp if temp < minimum else minimum       # 바이러스를 모두 퍼뜨릴 수 있는 최소 시간
        board = deepcopy(board_ori)
    print(minimum if minimum != 9999 else -1)       # 9999는 바이러스를 모두 퍼뜨릴 수 없는 경우이므로 -1을 출력함


sol()
