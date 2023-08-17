import sys
import heapq
from collections import deque
input = sys.stdin.readline


dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def destBFS(check, y, x, found = 0):
    startList = []
    dq = deque()
    dq.append((0, y, x))
    yOri, xOri = y, x

    if (y, x) in startToDest:
        heapq.heappush(startList, (0, y, x))        # 같은 거리라면 위쪽, 왼쪽
        if (y, x) in destToStart.get((y, x), set()):
            destStartPair[(y, x)][(y, x)] = 0
        found += 1
        if found == m:
            return startList
        
    check[y][x] = False

    while dq:
        dist, y, x = dq.popleft()
        for dirY, dirX in dir:
            nextY, nextX = y + dirY, x + dirX
            if 0 <= nextY < n and 0 <= nextX < n:
                if check[nextY][nextX] and maps[nextY][nextX] == 0:
                    check[nextY][nextX] = False
                    dq.append((dist + 1, nextY, nextX))

                    if (nextY, nextX) in startToDest:
                        heapq.heappush(startList, (dist + 1, nextY, nextX))
                        if (nextY, nextX) in destToStart.get((yOri, xOri), set()):
                            destStartPair[(yOri, xOri)][(nextY, nextX)] = dist + 1
                        found += 1
                        if found == m:
                            return startList
    
    return [[-999, -999, -999]]


if __name__ == "__main__":
    n, m, fuel = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]

    startY, startX = map(int, input().split())
    startY, startX = startY - 1, startX - 1

    startToDest = dict()
    destToStart = dict()
    destStartPair = dict()

    for i in range(m):
        y, x, destY, destX = map(int, input().split())
        y, x, destY, destX = y - 1, x - 1, destY - 1, destX - 1
        startToDest[(y, x)] = (destY, destX)
        destToStart[(destY, destX)] = destToStart.get((destY, destX), [])
        destToStart[(destY, destX)].append((y, x))
        destStartPair[(destY, destX)] = {(y, x) : 0}

    closerFromDest = dict()

    check = [[True] * n for _ in range(n)]
    destStartDist, startY, startX = destBFS(check, startY, startX, m - 1)[0]
    if destStartDist == -999:
        print(-1)
        exit(0)

    for destY, destX in destToStart:
        check = [[True] * n for _ in range(n)]
        temp = destBFS(check, destY, destX)
        if temp[0][0] == -999:
            print(-1)
            exit(0)
        closerFromDest[(destY, destX)] = temp

    found = set()
    cnt = 0
    while cnt < m:
        if fuel - destStartDist <= 0:
            print(-1)
            exit()

        fuel -= destStartDist       # 손님까지 가는 연로를 뺌
        found.add((startY, startX))
        endY, endX = startToDest[(startY, startX)]
        startEndDist = destStartPair[(endY, endX)][(startY, startX)]

        if fuel - startEndDist < 0:
            print(-1)
            exit()
        else:
            fuel += startEndDist
            cnt += 1
            if cnt < m:
                destStartDist, startY, startX = heapq.heappop(closerFromDest[(endY, endX)])
                while (startY, startX) in found:
                    destStartDist, startY, startX = heapq.heappop(closerFromDest[(endY, endX)])
        
    print(fuel)