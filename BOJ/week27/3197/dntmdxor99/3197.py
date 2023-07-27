import sys
from collections import deque
input = sys.stdin.readline


def waterMelt():        # 물이 녹는 과정
    while waterPos:
        y, x = waterPos.popleft()
        maps[y][x] = '.'

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and not waterCheck[ny][nx]:
                if maps[ny][nx] == '.':     # 물이 있음
                    waterPos.append((ny, nx))
                elif maps[ny][nx] == 'X':       # 얼음이라면 다음 날 녹아야 함
                    nextWaterPos.append((ny, nx))
                waterCheck[ny][nx] = True


def findSwan():     # 백조가 이동함
    while swanPos:
        y, x = swanPos.popleft()

        if y == endY and x == endX:
            return True

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and not swanCheck[ny][nx]:
                if maps[ny][nx] == '.':     # 물이라면 이동
                    swanPos.append((ny, nx))
                elif maps[ny][nx] == 'X':       # 아니라면 다음 날 녹으므로, 다음 날 이동
                    nextSwanPos.append((ny, nx))
                swanCheck[ny][nx] = True

    return False


if __name__ == "__main__":
    r, c = map(int, input().split())
    maps = [list(input().strip()) for _ in range(r)]
    swanCheck = [[False] * c for _ in range(r)]
    waterCheck = [[False] * c for _ in range(r)]

    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 현재 백조의 위치(물), 다음에 백조가 탐색해야 할 위치(얼음), 현재 물이 있는 자리, 다음에 얼음이 녹아야하는 자리
    swanPos = deque()
    nextSwanPos = deque()
    waterPos = deque()
    nextWaterPos = deque()

    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'L':
                if not swanPos:
                    swanPos.append((i, j))
                    swanCheck[i][j] = True
                else:
                    endY, endX = i, j

                maps[i][j] = '.'
                
                waterPos.append((i, j))    
                waterCheck[i][j] = True

            elif maps[i][j] == '.':
                waterPos.append((i, j))
                waterCheck[i][j] = True


    ans = 0
    while True:
        waterMelt()
        if findSwan():
            break

        swanPos = nextSwanPos
        waterPos = nextWaterPos
        nextSwanPos = deque()
        nextWaterPos = deque()

        ans += 1
        
    print(ans)