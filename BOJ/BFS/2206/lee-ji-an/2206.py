import sys
from collections import deque

input = sys.stdin.readline
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
N, M = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
board = []
# score : 최소 cnt를 저장
score = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
for i in range(N):
    board.append(list(map(int, list(input().rstrip()))))
board[N-1][M-1] = 2
q = deque()


def bfs():
    q.append((0, 0, 1, 0))
    while q:
        y, x, cnt, crush = q.popleft()
        for i in range(4):
            movex = x + dx[i]
            movey = y + dy[i]
            if movex < 0 or movex >= M or movey < 0 or movey >= N:
                continue
            if board[movey][movex] == 0:
                if score[movey][movex][crush] > cnt+1:  # cnt 비교로 visited를 대신
                    score[movey][movex][crush] = cnt+1
                    q.append((movey, movex, cnt + 1, crush))
            elif board[movey][movex] == 1 and crush == 0:
                if score[movey][movex][1] > cnt + 1:
                    score[movey][movex][1] = cnt+1
                    q.append((movey, movex, cnt + 1, 1))
            elif board[movey][movex] == 2:
                return cnt+1
    return -1
if M == 1 and N == 1:
    print(1)
else:
    print(bfs())
