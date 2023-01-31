import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
ROBOT, BLANK, WALL = 0, -1, -2
XYtoIdx = {}

# 시작점을 받아 모든 먼지로 가는 거리를 리스트로 반환
def bfs(startIdx):
    visited = [[False] * M for _ in range(N)]
    distList = [-1] * (dustCnt + 1)
    q = deque()
    q.append((spotList[startIdx][0], spotList[startIdx][1], 0))
    visited[spotList[startIdx][0]][spotList[startIdx][1]] = True
    distList[startIdx] = 0
    spotCnt = 1
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= M:
                continue
            if not visited[movey][movex]:
                if board[movey][movex] != 'x':
                    if board[movey][movex] == 'o' or board[movey][movex] == '*':
                        spotCnt += 1
                        distList[XYtoIdx[(movey, movex)]] = cnt + 1
                        if spotCnt == dustCnt+1:
                            return distList
                    q.append((movey, movex, cnt + 1))
                    visited[movey][movex] = True
    return distList

# 먼지의 idx 리스트를 받아 그 경로대로 거리 계산하는 함수
def distCalcul(route):
    dist = 0
    for i in range(len(route) - 1):
        if distTable[route[i]][route[i + 1]] == -1:
            return -1
        dist += distTable[route[i]][route[i + 1]]
    return dist


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    spotList = [0]
    board = []
    dist = 0
    minDist = float('inf')
    dustCnt = 0
    flag = False
    for i in range(N):
        row = input().rstrip()
        board.append(row)
        for j in range(M):
            if row[j] == 'o':
                spotList[0] = (i, j)
                XYtoIdx[(i, j)] = 0
            if row[j] == '*':
                dustCnt += 1
                spotList.append((i, j))
                XYtoIdx[(i, j)] = dustCnt
    distTable = [[0] * (dustCnt + 1) for _ in range(dustCnt + 1)]
    for i in range(dustCnt + 1):
        partDist = bfs(i)               # 거리 계산 bfs 호출
        for j in range(dustCnt + 1):
            if partDist[j] == -1:       # 하나라도 갈 수 없는 경로가 나왔을 때 flag 표시
                flag = True
                break
            distTable[i][j] = partDist[j]
    if flag:
        print(-1)
        continue
    for route in permutations(range(1, dustCnt + 1), dustCnt):  # 순열로 모든 가능한 경로 생성
        dist = distTable[0][route[0]]
        for i in range(len(route) - 1):
            dist += distTable[route[i]][route[i + 1]]
        minDist = min(minDist, dist)
    print(minDist)
