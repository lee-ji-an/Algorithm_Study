import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

case = []
green = deque([False] * 4 for _ in range(7))
blue = deque([False] * 4 for _ in range(7))
score = 0
for i in range(4):
    green[6][i] = True
for i in range(4):
    blue[6][i] = True

for i in range(N):
    case.append(list(map(int, input().split())))


def move(t, y, x):
    green_idx, blue_idx = set(), set()
    if t == 1:
        for i in range(7):
            if green[i][x]:
                green[i - 1][x] = True
                green_idx.add(i - 1)
                break

        for i in range(7):
            if blue[i][y]:
                blue[i - 1][y] = True
                blue_idx.add(i - 1)
                break
    elif t == 2:
        for i in range(7):
            if green[i][x] or green[i][x + 1]:
                green[i - 1][x] = green[i - 1][x + 1] = True
                green_idx.add(i - 1)
                break
        for i in range(7):
            if blue[i][y]:
                blue[i - 1][y] = blue[i - 2][y] = True
                blue_idx.add(i - 1)
                blue_idx.add(i - 2)
                break
    else:
        for i in range(7):
            if green[i][x]:
                green[i - 1][x] = green[i - 2][x] = True
                green_idx.add(i - 1)
                green_idx.add(i - 2)
                break
        for i in range(7):
            if blue[i][y] or blue[i][y + 1]:
                blue[i - 1][y] = blue[i - 1][y + 1] = True
                blue_idx.add(i - 1)
                break

    return green_idx, blue_idx


green_top = 6
blue_top = 6

for i in range(N):
    t, y, x = case[i]
    green_idx, blue_idx = move(t, y, x)

    blue_sub_score = 0
    green_sub_score = 0
    for idx in green_idx:
        flag = True
        for j in range(4):
            if not green[idx][j]:
                flag = False
                break
        if flag:
            del green[idx]
            green.appendleft([False] * 4)
            green_sub_score += 1
            green_top += 1
    for idx in blue_idx:
        flag = True
        for j in range(4):
            if not blue[idx][j]:
                flag = False
                break
        if flag:
            del blue[idx]
            blue.appendleft([False] * 4)
            blue_sub_score += 1
            blue_top += 1

    green_top = min(green_top, min(green_idx) + green_sub_score)
    blue_top = min(blue_top, min(blue_idx) + blue_sub_score)
    if green_top <= 1:
        for _ in range(2 - green_top):
            del green[5]
            green.appendleft([False] * 4)
            green_top += 1
    if blue_top <= 1:
        for _ in range(2 - blue_top):
            del blue[5]
            blue.appendleft([False] * 4)
            blue_top += 1
    score += (green_sub_score + blue_sub_score)

print(score)
tile = 0
for i in range(2, 6):
    for j in range(4):
        if green[i][j]:
            tile += 1
        if blue[i][j]:
            tile += 1
print(tile)
