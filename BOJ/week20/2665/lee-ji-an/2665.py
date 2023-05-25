import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
board = []
q = deque()
visited = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    board.append(input().rstrip())


def bfs():
    q.append((0, 0, 0))
    visited[0][0] = 0
    while q:
        # y, x : 위치, cnt: 흰방으로 바꾼 횟수
        y, x, cnt = q.popleft()
        for i in range(4):
            movey, movex, new_cnt = y + dy[i], x + dx[i], cnt
            if not(0 <= movey < N and 0 <= movex < N):
                continue
            # 검은 방일 때는 흰방으로 바꿔야하므로 cnt 를 1 증가시킴
            if board[movey][movex] == '0':
                new_cnt += 1
            # visited에 기록된 cnt보다 클 때만 다시 큐에 넣음
            if visited[movey][movex] > new_cnt:
                visited[movey][movex] = new_cnt
                if not(movey == N - 1 and movex == N - 1):
                    q.append((movey, movex, new_cnt))

    return visited[N - 1][N - 1]


print(bfs())
