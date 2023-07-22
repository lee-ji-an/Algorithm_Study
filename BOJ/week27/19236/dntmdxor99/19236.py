import sys
from copy import deepcopy
input = sys.stdin.readline


def fishMove(sharkY, sharkX):
    for i in range(1, 17):
        if fishPos[i] == -1: continue
        if fishDir[i] == -1: continue
        y, x = fishPos[i]       # 현재 물고기의 좌표
        curFishDir = fishDir[i]     # 현재 물고기의 방향

        while True:
            ny, nx = y + dir[curFishDir][0], x + dir[curFishDir][1]
            if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != (sharkY, sharkX):
                maps[y][x], maps[ny][nx] = maps[ny][nx], maps[y][x]     # 물고기의 번호 바꿈
                fishPos[i] = (ny, nx)
                fishDir[i] = curFishDir
                if maps[y][x]:
                    fishPos[maps[y][x]] = (y, x)
                break
            else:
                curFishDir = (curFishDir + 1) % 8


def findCand(sharkY, sharkX, sharkDir):        # 상어가 먹을 수 있는 애들의 좌표를 반환
    cand = []
    ny, nx = sharkY + dir[sharkDir][0], sharkX + dir[sharkDir][1]
    while 0 <= ny < 4 and 0 <= nx < 4:
        if maps[ny][nx]:
            cand.append((ny, nx))
        ny, nx = ny + dir[sharkDir][0], nx + dir[sharkDir][1]

    return cand


def backTracking(sharkY, sharkX, sharkScore):
    global maps, fishDir, fishPos
    fishNum = maps[sharkY][sharkX]      # 물고기의 번호

    sharkScore += fishNum
    sharkDir = fishDir[fishNum]
    fishPos[fishNum] = -1
    fishDir[fishNum] = -1
    maps[sharkY][sharkX] = -1       # 상어가 있음

    fishMove(sharkY, sharkX)
    cand = findCand(sharkY, sharkX, sharkDir)

    maps[sharkY][sharkX] = 0
    mapsOri = deepcopy(maps)        # 저장해야 함
    fishPosOri = deepcopy(fishPos)
    fishDirOri = deepcopy(fishDir)

    scoreList = list()
    for (y, x) in cand:
        scoreList.append(backTracking(y, x, sharkScore))

        maps = deepcopy(mapsOri)
        fishPos = deepcopy(fishPosOri)
        fishDir = deepcopy(fishDirOri)

    if len(scoreList) == 0:
        return sharkScore

    else:
        return max(scoreList)


if __name__ == "__main__":
    maps = []
    fishPos = [0] * 17      # n번째 물고기의 좌표
    fishDir = [0] * 17      # n번째 물고기의 방향

    for col in range(4):
        row = list(map(int, input().split()))
        temp = []
        for x in range(0, 8, 2):
            temp.append(row[x])
            fishDir[row[x]] = row[x + 1] - 1
            fishPos[row[x]] = (col, x // 2)
        maps.append(temp)
    
    dir = [[-1, 0],[-1, -1],[0, -1],[1, -1],[1, 0],[1, 1],[0, 1],[-1, 1]]     # ↑, ↖, ←, ↙, ↓, ↘, →, ↗

    print(backTracking(0, 0, 0))