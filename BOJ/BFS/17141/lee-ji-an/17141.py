import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
board = []
minDist = float('inf')
remainCnt = M
for i in range(N):
    board.append(list(map(int, input().split())))

# 구역의 갯수, 각 구역 안의 2 자리(바이러스를 놓을 수 있는 자리)의 위치를 key(구역의 숫자) : value(위치 튜플) 로 만들어서 딕셔너리 return
def areaCnt():
    q = deque()
    visited = [[False] * N for _ in range(N)]
    virusSpaceDict = {}
    areaNum = 2  # areaNum : 3, 4, 5 ~
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] == 1:
                continue
            flag = False
            areaNum += 1
            q.append((i, j))
            visited[i][j] = True
            if board[i][j] == 2:
                flag = True
                virusSpaceDict[areaNum] = [(i, j)]
            while q:
                y, x = q.popleft()
                for k in range(4):
                    movey = y + dy[k]
                    movex = x + dx[k]
                    if movey < 0 or movey >= N or movex < 0 or movex >= N:
                        continue
                    if not visited[movey][movex] and board[movey][movex] != 1:
                        if board[movey][movex] == 2:
                            flag = True
                            if areaNum in virusSpaceDict:
                                virusSpaceDict[areaNum].append((movey, movex))
                            else:
                                virusSpaceDict[areaNum] = [(movey, movex)]
                        q.append((movey, movex))
                        visited[movey][movex] = True
            if not flag:
                return -1, {}   # 한 구역에 2(바이러스를 놓을 수 있는 자리)가 없으면 -1 return
    return areaNum, virusSpaceDict

# virus를 놓을 공간의 리스트를 받아 다 퍼질 때까지 걸리는 시간을 return
def bfs(virusSpace):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    maxDist = -1
    for i in range(len(virusSpace)):
        q.append((virusSpace[i][0], virusSpace[i][1]))
        visited[virusSpace[i][0]][virusSpace[i][1]] = True
    while q:
        maxDist += 1
        for i in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                movey = y + dy[i]
                movex = x + dx[i]
                if movey < 0 or movey >= N or movex < 0 or movex >= N:
                    continue
                if not visited[movey][movex] and board[movey][movex] != 1:
                    q.append((movey, movex))
                    visited[movey][movex] = True
    return maxDist


areaNum, virusSpaceDict = areaCnt()
if len(virusSpaceDict.keys()) > M or areaNum == -1:  # 바이러스를 놓을 수 있는 자리가 없으면 -1 print
    print(-1)
else:
    oneCnt, moreThanOne = 0, set()
    totalSpot = []
    oneSpotList = []
    for i in range(3, areaNum + 1):     # 공간 번호 : 3, 4, 5 ...
        if len(virusSpaceDict[i]) == 1:
            oneCnt += 1
            oneSpotList.extend(virusSpaceDict[i])  # 바이러스를 놓을 수 있는 자리가 1개뿐인 구역 저장
        else:
            moreThanOne.add(i)
            totalSpot.extend(virusSpaceDict[i])    # 바이러스를 놓을 수 있는 자리가 2개 이상인 구역 저장
    oneSpotDist = bfs(oneSpotList)                 # 바이러스를 놓을 수 있는 자리가 1개뿐이라면 무조건 그 자리에 무조건 바이러스를 놓음
    for selectedSpot in combinations(totalSpot, M-oneCnt):          # 바이러스 자리가 2개 이상인 곳을 모아 놓을 자리를 뽑음
        flag = False
        for num in moreThanOne:
            if not set(selectedSpot) & set(virusSpaceDict[num]):    # 각 구역에서 바이러스 자리가 1개 이상은 뽑았는지 검사
                flag = True
                break
        if flag:
            continue
        minDist = min(minDist, max(bfs(selectedSpot), oneSpotDist))
    print(minDist)
