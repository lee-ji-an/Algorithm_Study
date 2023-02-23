from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(n)]

def solve(x, dir, count):
    global board
    for idx in range(x, n+1, x):
        idx -= 1
        if dir == 0:  # 시계 방향
            for _ in range(count):
                board[idx].appendleft(board[idx].pop())
        else:  # 반시계 방향
            for _ in range(count):
                board[idx].append(board[idx].popleft())

    tmp = [deque(list(b)[:]) for b in board]
    flag = 0

    for i in range(n):
        for j in range(m):
            if i != 0 and board[i][j] != 0 and board[i][j] == board[i-1][j]:
                tmp[i-1][j] = tmp[i][j] = 0
                flag = 1
            if i != n-1 and board[i][j] != 0 and board[i][j] == board[i+1][j]:
                tmp[i+1][j] = tmp[i][j] = 0
                flag = 1
            if board[i][j] != 0 and board[i][j] == board[i][j-1]:
                tmp[i][j] = tmp[i][j-1] = 0
                flag = 1
            if board[i][j] != 0 and board[i][j] == board[i][(j+1) % m]:
                tmp[i][j] = tmp[i][(j+1) % m] = 0
                flag = 1

    if not flag:
        cnt = 0
        ss = 0
        for i in range(n):
            for j in range(m):
                if tmp[i][j] != 0:
                    ss += tmp[i][j]
                    cnt += 1
        if cnt != 0:
            avg = ss / cnt

            for i in range(n):
                for j in range(m):
                    if tmp[i][j] > avg and tmp[i][j] != 0:
                        tmp[i][j] -= 1
                    elif tmp[i][j] < avg and tmp[i][j] != 0:
                        tmp[i][j] += 1
    board = tmp


for _ in range(t):
    x, d, k = map(int, input().split())
    solve(x, d, k)

ans = 0
for b in board:
    ans += sum(b)

print(ans)