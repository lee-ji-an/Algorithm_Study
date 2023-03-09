import sys
from copy import deepcopy


def fish_move() -> (list, dict):
    # 물고기의 움직임을 구현한 함수
    global maps, pos

    for i in range(1, 17):
        # 1번부터 16번까지 물고기를 이동시킴
        if i in pos:
            y, x = pos[i]
            d = int(maps[y][x].imag)
            for _ in range(9):
                dy, dx = dir[d]
                ny, nx = y + dy, x + dx
                if 0 <= ny < 4 and 0 <= nx < 4:     # 범위를 벗어나지 않음
                    if maps[ny][nx] != -1:      # 상어가 없어야 함
                        maps[y][x], maps[ny][nx] = maps[ny][nx], complex(int(maps[y][x].real), d)        # 위치 교환
                        pos[i], pos[int(maps[y][x].real)] = [ny, nx], [y, x]     # 값 변경
                        break
                d = (d + 1) % 8


def can_shark_move(y : int, x : int, shark_dir : int) -> list:
    # 상어가 움직일 수 있는 공간을 반환함
    global maps

    cand = []
    dy, dx = dir[shark_dir]
    ny, nx = y + dy, x + dx
    while 0 <= ny < 4 and 0 <= nx < 4:
        if maps[ny][nx] != 0:        # 물고기가 있다면
            cand.append([ny, nx])
        ny, nx = ny + dy, nx + dx

    return cand


def sol(y : int, x : int, score : int, shark_dir : int) -> int:
    global maps, pos

    score += int(maps[y][x].real)       # 점수를 더함
    shark_dir = int(maps[y][x].imag)        # 상어의 방향을 구함
    pos.pop(int(maps[y][x].real))       # 해당 위치는 상어에게 먹힘

    maps[y][x] = -1     # 해당 자리에 상어가 있음

    fish_move()      # 물고기의 움직임
    cand = can_shark_move(y, x, shark_dir)       # 상어가 움직일 수 있는 곳

    maps[y][x] = 0      # 이제 상어는 이동해야 하므로, 해당 공간은 빈 공간이 됨

    maps_ori = deepcopy(maps)
    pos_ori = deepcopy(pos)
    score_list = []

    for (y, x) in cand:
        score_list.append(sol(y, x, score, shark_dir))
        maps = deepcopy(maps_ori)       # 맵 복구
        pos = deepcopy(pos_ori)     # 물고기 위치 복구

    if len(score_list) == 0:
        return score
    else:
        return max(score_list)


if __name__ == "__main__":
    input = sys.stdin.readline
    maps = [[0] * 4 for _ in range(4)]
    pos = dict()
    dir = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    for i in range(4):
        temp = list(map(int, input().split()))
        for j in range(4):
            maps[i][j] = complex(temp[j * 2], temp[j * 2 + 1] - 1)
            pos[temp[j * 2]] = [i, j]

    print(sol(0, 0, 0, 0))
