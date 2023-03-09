import sys
from collections import deque

input = sys.stdin.readline

board = [[0] * 9 for _ in range(9)]
square_list = [[[False] * 10 for _ in range(3)] for _ in range(3)]
row_list = [[False] * 10 for _ in range(9)]
col_list = [[False] * 10 for _ in range(9)]

square_set = [[set() for _ in range(3)] for _ in range(3)]
row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
q = []
cnt = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] != 0:
            board[i][j] = row[j]
            row_list[i][row[j]] = True
            col_list[j][row[j]] = True
            square_list[i//3][j//3][row[j]] = True
        else:
            cnt += 1
            q.append((i, j))

for i in range(0, 9):
    for j in range(1, 10):
        if not row_list[i][j]:
            row_set[i].add(j)
        if not col_list[i][j]:
            col_set[i].add(j)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(1, 10):
            if not square_list[i][j][k]:
                square_set[i][j].add(k)


def recur(idx):
    if idx == len(q):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()

        return 1  # 모든 칸을 채웠을 때 return 1
    y, x = q[idx]
    candidate = row_set[y] & col_set[x] & square_set[y//3][x//3]
    for item in candidate:
        board[y][x] = item
        row_set[y].remove(item)
        col_set[x].remove(item)
        square_set[y//3][x//3].remove(item)
        ret = recur(idx + 1)
        if ret:
            return 1
        board[y][x] = 0
        row_set[y].add(item)
        col_set[x].add(item)
        square_set[y // 3][x // 3].add(item)

    return 0


recur(0)
