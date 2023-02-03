import sys
from collections import deque

input = sys.stdin.readline
dy = (0, 0, 1, -1)  # 동서남북
dx = (1, -1, 0, 0)
dirMask = (4, 1, 8, 2)  # 0100, 0001, 1000, 0010 동서남북
N, M = map(int, input().split())
board = []
for i in range(M):
    board.append(list(map(int, input().split())))

def areaCnt():
    areaDict = {}
    areaNum = 0
    maxArea = 0
    visited = [[-1] * N for _ in range(M)]
    aroundArea = {}
    for i in range(M):
        for j in range(N):
            if visited[i][j] == -1:
                aroundArea[areaNum] = set()
                q = deque()
                q.append((i, j))
                visited[i][j] = areaNum
                area = 1
                while q:
                    y, x = q.popleft()
                    for dir in range(4):
                        movey = y + dy[dir]
                        movex = x + dx[dir]
                        if movey < 0 or movey >= M or movex < 0 or movex >= N:
                            continue
                        if visited[movey][movex] >= 0:              # 이미 방문한 적이 있으면 인접 행렬에 넣기
                            aroundArea[areaNum].add(visited[movey][movex])
                            continue
                        if dirMask[dir] & board[y][x] != 0:         # 벽이 있다면
                            continue
                        visited[movey][movex] = areaNum
                        area += 1
                        q.append((movey, movex))
                areaDict[areaNum] = area
                maxArea = max(maxArea, area)
                areaNum += 1
    return areaDict, areaNum, maxArea, aroundArea   # 구역 번호 : 면적 dictionary / 구역 번호 / 최대 구역 / 인접구역 dictionary


areaDict, areaNum, oneMaxArea, aroundArea = areaCnt()

twoMax = 0
print(areaNum)
print(oneMaxArea)
for key in aroundArea.keys():
    for item in aroundArea[key]:
        if key != item:
            twoMax = max(twoMax, areaDict[key]+areaDict[item])
print(twoMax)
