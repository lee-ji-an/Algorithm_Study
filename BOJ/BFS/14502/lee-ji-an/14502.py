import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
virus = []  # bfs 처음 시작할 때 쓰려고
blank = []
board = []
visited = [[0 for _ in range(M)] for _ in range(N)]
wallCount = 0
safeZone = 0
dx = (0, 0, -1, 1) # 상하좌우
dy = (-1, 1, 0, 0)
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(len(row)):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            blank.append((i, j))
        elif board[i][j] == 1:
            wallCount += 1

def bfs(wallCount):
    cnt = 0
    q = deque()
    for pos in virus:
        q.append(pos)
        cnt += 1
        visited[pos[0]][pos[1]] = 1
    while q:
        y, x = q.popleft()  # x,y 헷갈림..
        for i in range(4):
            movex = x + dx[i]
            movey = y + dy[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= M:
                continue
            if not visited[movey][movex]:
                if board[movey][movex] == 0:   # 빈칸이면 q 에 넣음
                    q.append((movey, movex))
                    cnt += 1
                    visited[movey][movex] = 1
    return N*M-cnt-wallCount-3


for walls in combinations(blank, 3):
    one, two, three = walls[0], walls[1], walls[2]
    board[one[0]][one[1]] = 1
    board[two[0]][two[1]] = 1
    board[three[0]][three[1]] = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    safeZone = max(bfs(wallCount), safeZone)
    board[one[0]][one[1]] = 0
    board[two[0]][two[1]] = 0
    board[three[0]][three[1]] = 0
print(safeZone)