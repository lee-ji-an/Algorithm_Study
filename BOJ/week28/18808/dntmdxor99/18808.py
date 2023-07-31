import sys
input = sys.stdin.readline


def canCoordinate(sticker):
    # 가능한 좌표를 찾는 함수
    coordinate = []
    yOffset = len(sticker)
    xOffset = len(sticker[0])
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0 or (maps[y][x] and sticker[0][0] == 0):      # 놓으려는 보드의 시작에 아무것도 없거나, 놓여져 있더라도 스티커에 없는 공간이라면?
                if y + yOffset <= n:        # 스티커가 공간을 벗어나지 않는다면
                    if x + xOffset <= m:
                        coordinate.append((y, x))
    return coordinate


def canPut(sticker, y, x):
    # 놓을 수 있는지 판단하는 함수
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if maps[i + y][j + x] and sticker[i][j]:        # 스티커에 있는 공간이고, 보드에도 스티커가 붙여져 있다면
                return False    
    return True


def put(sticker, y, x):
    # 스티커 붙임
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                maps[i + y][j + x] = 1


def rotation(sticker):
    # 회전
    sticker = zip(*sticker[::-1])
    return [list(e) for e in sticker]


def logic(sticker):
    for _ in range(4):
        coordinate = canCoordinate(sticker)
        if coordinate:
            for y, x in coordinate:
                if canPut(sticker, y, x):
                    put(sticker, y, x)
                    return
        sticker = rotation(sticker)
        

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    stickers = []
    for _ in range(k):
        y, x = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(y)]
        stickers.append(sticker)

    for sticker in stickers:
        logic(sticker)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j]:
                cnt += 1
    print(cnt)