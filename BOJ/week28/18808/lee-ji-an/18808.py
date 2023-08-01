import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

laptop = [[False] * M for _ in range(N)]


def solve(R, C, sticker):
    row, col = R, C
    for r in range(4):  # r : 시계 방향으로 90도 회전한 횟수
        for n in range(N - row + 1):
            for m in range(M - col + 1):
                flag, new_laptop, cnt = attach(n, m, laptop, sticker)
                if flag:
                    return new_laptop, cnt
        row, col, sticker = rotate(len(sticker), len(sticker[0]), sticker)

    return laptop, 0


# n, m 위치를 시작으로 스티커를 붙임
def attach(n, m, laptop, sticker):
    cnt = 0
    row, col = len(sticker), len(sticker[0])
    new_laptop = [r[:] for r in laptop]
    for r in range(row):
        for c in range(col):
            if sticker[r][c] == 0:
                continue
            if new_laptop[n + r][m + c]:
                return False, laptop, 0

            new_laptop[n + r][m + c] = True
            cnt += 1
    # sticker 를 봍일 수 있는지에 대한 여부, sticker 를 붙인 후의 laptop, sticker 칸 갯수
    return True, new_laptop, cnt


# 스티커를 회전시키는 함수
def rotate(row, col, sticker):
    new_sticker = [[0] * row for _ in range(col)]
    new_row, new_col = col, row

    for r in range(row):
        for c in range(col):
            new_sticker[c][new_col - 1 - r] = sticker[r][c]

    return len(new_sticker), len(new_sticker[0]), new_sticker


ans = 0
for k in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for r in range(R)]

    laptop, cnt = solve(R, C, sticker)
    ans += cnt


print(ans)
