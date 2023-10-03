import sys
from collections import deque
input = sys.stdin.readline


def adjAirCheck(dq):
    nextSet = set()
    while dq:
        y, x = dq.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == '1':      # 치즈라면
                    adjCheck[ny][nx] += 1
                    if adjCheck[ny][nx] >= 2:       # 인접한 공기가 2개
                        nextSet.add((ny, nx))
                else:
                    if airCheck[ny][nx] == False:       # 공기가 방문하지 않았다면
                        airCheck[ny][nx] = True
                        dq.append((ny, nx))
    
    return nextSet


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [input().strip().split() for _ in range(n)]
    airCheck = [[False] * m for _ in range(n)]      # 공기의 방문 체크
    adjCheck = [[0] * m for _ in range(n)]      # 치즈에 인접한 외부 공기의 개수

    cnt = sum([i.count('1') for i in maps])

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    dq = set()
    dq.add((0, 0))
    airCheck[0][0] = True
    time = 0

    while cnt > 0:
        time += 1
        dq = deque(dq)
        dq = adjAirCheck(dq)
        cnt -= len(dq)
        
        for y, x in dq:
            maps[y][x] = '0'
            airCheck[y][x] = True

    print(time)
