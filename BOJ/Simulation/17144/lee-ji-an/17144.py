import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int, input().split())

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
room = []
cleaner = []
q = deque()
zero_list = [[0] * C for _ in range(R)]
visited_origin = [[False] * C for _ in range(R)]
total_dust = 0
for i in range(R):
    row = list(map(int, input().split()))
    room.append(row)
    for j in range(C):
        if row[j] == -1:
            cleaner.append(i)
        elif row[j] > 0:
            total_dust += row[j]


def dust_spread():
    dust_change = [r[:] for r in zero_list]
    dust_change[cleaner[0]][0] = -1
    dust_change[cleaner[1]][0] = -1
    for y in range(R):
        for x in range(C):
            if room[y][x] == 0 or room[y][x] == -1:
                continue
            area = 0
            spread_amount = room[y][x] // 5
            for j in range(4):
                movey = y + dy[j]
                movex = x + dx[j]
                if not (0 <= movey < R) or not (0 <= movex < C) or room[movey][movex] == -1:
                    continue
                area += 1
                dust_change[movey][movex] += spread_amount
            dust_change[y][x] += room[y][x] - spread_amount * area

    return dust_change


def rotation():
    for r in range(cleaner[0] - 1, 0, -1):  # 하
        room[r][0] = room[r - 1][0]
    for c in range(0, C - 1):  # 좌
        room[0][c] = room[0][c + 1]
    for r in range(0, cleaner[0]):  # 위
        room[r][C - 1] = room[r + 1][C - 1]
    for c in range(C - 1, 1, -1):  # 우
        room[cleaner[0]][c] = room[cleaner[0]][c - 1]
    room[cleaner[0]][1] = 0

    for r in range(cleaner[1] + 1, R - 1):
        room[r][0] = room[r + 1][0]
    for c in range(0, C - 1):
        room[R - 1][c] = room[R - 1][c + 1]
    for r in range(R - 1, cleaner[1], -1):
        room[r][C - 1] = room[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        room[cleaner[1]][c] = room[cleaner[1]][c - 1]
    room[cleaner[1]][1] = 0


for i in range(T):
    dust_change = dust_spread()
    room = [r[:] for r in dust_change]
    clean_dust = room[cleaner[0] - 1][0] + room[cleaner[1] + 1][0]
    rotation()
    total_dust -= clean_dust
print(total_dust)
