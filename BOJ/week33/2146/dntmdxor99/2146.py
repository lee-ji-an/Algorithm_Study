import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    dq = deque()
    borderDQ = set()
    groupNum = 1

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                groupNum += 1
                maps[i][j] = groupNum
                dq.append((i, j))

                while dq:
                    y, x = dq.popleft()
                    for dy, dx in dir:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            if maps[ny][nx] == 1:
                                dq.append((ny, nx))
                                maps[ny][nx] = groupNum
                            if maps[ny][nx] == 0:
                                borderDQ.add((y, x))

    minimum = sys.maxsize
    seaDQ = deque()
    mapsOriginal = [arr[:] for arr in maps]

    for y, x in borderDQ:       # 가장자리에서 BFS
        maps = [arr[:] for arr in mapsOriginal]
        seaDQ.clear()
        seaDQ.append((y, x, 0))     # 바다의 BFS
        curGroup = maps[y][x]
        
        while seaDQ:        # 바다를 BFS
            y, x, cnt = seaDQ.popleft()

            if cnt >= minimum:      # 기존의 최솟값보다 크면 안 가도 됨
                break

            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n:
                    if maps[ny][nx] == 0:       # 바다면
                        seaDQ.append((ny, nx, cnt + 1))
                        maps[ny][nx] = -1       # 방문처리

                    elif maps[ny][nx] > 1:      # 대륙이고
                        if curGroup != maps[ny][nx]:        # 다른 그룹이면 최솟값 갱신해야 함
                            minimum = min(minimum, cnt)
    
    print(minimum)