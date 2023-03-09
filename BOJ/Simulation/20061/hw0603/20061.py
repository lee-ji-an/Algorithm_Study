import sys

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
score = 0


# 블록 놓기
def place_block(t, x, y):
    place = []
    minIdx_green, minIdx_blue = 5, 5

    place.append((x, y))
    match (t):
        case 2:
            place.append((x, y+1))
            minIdx_blue = 4
        case 3:
            place.append((x+1, y))
            minIdx_green = 4
    
    # Green
    for i in range(6):
        for r, c in place:
            if ((nr := r-x+i) < 6 and green[nr][c] == 1):
                minIdx_green = min(minIdx_green, i-1)

    # Blue
    for i in range(6):
        for r, c in place:
            if ((nc := c-y+i) < 6 and blue[r][nc] == 1):
                minIdx_blue = min(minIdx_blue, i-1)
    
    for r, c in place:
        green[r-x+minIdx_green][c] = 1
        blue[r][c-y+minIdx_blue] = 1


# 블록 이동
def move_block(blue, green, move):
    for tile, idx in move:
        if (tile == 0):
            green = [
                [
                    green[i-1][j] if 0 < i <= idx else green[i][j] for j in range(4)
                ] for i in range(6)
            ]
            for i in range(4):
                green[0][i] = 0
        else:
            blue = [
                [
                    blue[i][j-1] if 0 < j <= idx else blue[i][j] for j in range(6)
                ] for i in range(4)
            ]
            for i in range(4):
                blue[i][0] = 0

    return green, blue


# 점수 계산
def get_score(blue, green):
    global score
    move = []

    # Green
    for i in range(6):
        if (green[i][0] == green[i][1] == green[i][2] == green[i][3] == 1):
            for j in range(4):
                green[i][j] = 0
            score += 1
            move.append([0, i])
    
    # Blue
    for i in range(6):
        if (blue[0][i] == blue[1][i] == blue[2][i] == blue[3][i] == 1):
            for j in range(4):
                blue[j][i] = 0
            score += 1
            move.append([1, i])
    
    green, blue = move_block(blue, green, move)
    return green, blue


def special_color(blue, green):
    move = []
    for i in range(2):
        for j in range(4):
            if (green[i][j]):
                move.append([0, 5])
                break

    for i in range(2):
        for j in range(4):
            if (blue[j][i]):
                move.append([1, 5])
                break
    
    return move_block(blue, green, move)


N = int(sys.stdin.readline())
for _ in range(N):
    t, x, y = map(int, sys.stdin.readline().split())
    place_block(t, x, y)  # 블록 놓기
    green, blue = get_score(blue, green)
    green, blue = special_color(blue, green)  # 연한 색의 특수 칸 처리


block_cnt = 0
for i in range(6):
    for j in range(4):
        block_cnt += green[i][j]
        block_cnt += blue[j][i]

print(score, block_cnt, sep='\n')
