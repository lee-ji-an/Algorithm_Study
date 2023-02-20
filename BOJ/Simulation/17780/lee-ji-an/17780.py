import sys
input = sys.stdin.readline

WHITE, RED, BLUE = 0, 1, 2

N, K = map(int, input().split())

dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)
color = [[BLUE] * (N + 2)]
horse_list = [[0] * (N + 1) for _ in range(N + 1)]
numToPos = {}


for _ in range(N):
    color.append([BLUE] + list(map(int, input().split())) + [BLUE])
color.append([BLUE] * (N + 2))

for i in range(K):
    r, c, direction = map(int, input().split())
    numToPos[i + 1] = (r, c, direction - 1)
    horse_list[r][c] = (horse_list[r][c] << 4) + (i + 1)

horse_bitmask = 0b1111


def get_reverse(direction):  # 방향을 입력받아서 반대 방향을 반환하는 함수
    if direction == 0 or direction == 2:
        return direction + 1
    else:
        return direction - 1


def get_horse_cnt(num):  # bit 숫자를 입력받아서 말이 몇 개 있는지 반환하는 함수
    if num.bit_length() % 4 > 0:
        return num.bit_length() // 4 + 1
    return num.bit_length() // 4


def do_white(y, x, movey, movex):
    # 칸에 있는 말 전체를 들어서 위에 올림
    horse_list[movey][movex] += (horse_list[y][x] << (get_horse_cnt(horse_list[movey][movex]) * 4))
    for _ in range(get_horse_cnt(horse_list[y][x])):
        horse = horse_list[y][x] & horse_bitmask
        numToPos[horse] = (movey, movex, numToPos[horse][2])
        horse_list[y][x] = horse_list[y][x] >> 4
    horse_list[y][x] = 0

    return get_horse_cnt(horse_list[movey][movex])  # 옮긴 칸에 말이 몇 개 있는지 반환


def do_red(y, x, movey, movex):
    # 맨 위에 있는 말들을 하나씩 들어서 옮김
    for i in range(1, get_horse_cnt(horse_list[y][x]) + 1):
        top_horse = horse_list[y][x] >> (get_horse_cnt(horse_list[y][x]) - i) * 4 & horse_bitmask
        horse_list[movey][movex] += top_horse << get_horse_cnt(horse_list[movey][movex]) * 4
        numToPos[top_horse] = (movey, movex, numToPos[top_horse][2])
    horse_list[y][x] = 0

    return get_horse_cnt(horse_list[movey][movex])  # 옮긴 칸에 말이 몇 개 있는지 반환


def do_blue(k, y, x, direction):
    reverse_dir = get_reverse(direction)
    movey = y + dy[reverse_dir]
    movex = x + dx[reverse_dir]
    numToPos[k] = (y, x, reverse_dir)
    if color[movey][movex] == BLUE:
        return get_horse_cnt(horse_list[y][x])  # 옮긴 칸에 말이 몇 개 있는지 반환
    elif color[movey][movex] == RED:
        return do_red(y, x, movey, movex)
    else:
        return do_white(y, x, movey, movex)


def solve():
    value = 0
    for i in range(1000):
        for j in range(1, K + 1):
            y, x, direction = numToPos[j]
            if horse_list[y][x] & horse_bitmask != j:
                continue
            movey, movex = y + dy[direction], x + dx[direction]
            if color[movey][movex] == BLUE:
                value = do_blue(j, y, x, direction)
            elif color[movey][movex] == WHITE:
                value = do_white(y, x, movey, movex)
            elif color[movey][movex] == RED:
                value = do_red(y, x, movey, movex)
            if value >= 4:
                return i + 1
    return -1


print(solve())
