r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
vac = []
for i in range(r):
    if maps[i][0] == -1:
        vac.append(i)       # 청정기의 위치를 찾음


def spread(maps, sp_maps):      # 먼지 분산
    for i in range(r):
        for j in range(c):
            if maps[i][j] != -1 and maps[i][j] > 0:
                sp_dust = maps[i][j] // 5
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] != -1:
                        sp_maps[ny][nx] += sp_dust
                        maps[i][j] -= sp_dust
                sp_maps[i][j] += maps[i][j]

    return sp_maps      # 새로운 맵에 넣음


def up():       # 위쪽 바람
    dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
    dir = 0
    before = 0      # 이전 값을 저장
    y, x = vac[0], 1        # 바로 오른쪽부터 시작
    while True:
        ny, nx = y + dy[dir], x + dx[dir]       # 움직임
        if y == vac[0] and x == 0:
            maps[y][x] = 0      # 만약 청정기에 도달하면 0으로 만들고 끝냄
            break
        if not (0 <= ny < r and 0 <= nx < c):       # 모서리에 도달하면 방향을 전환함
            dir += 1
            continue
        maps[y][x], before = before, maps[y][x]     # 현재 값을 저장하고, 이전 값을 현재 위치에 넣음
        y, x = ny, nx


def down():     # 아래쪽 바람
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    dir = 0
    before = 0
    y, x = vac[1], 1
    while True:
        ny, nx = y + dy[dir], x + dx[dir]
        if y == vac[1] and x == 0:
            maps[y][x] = 0
            break
        if not(0 <= ny < r and 0 <= nx < c):
            dir += 1
            continue
        maps[y][x], before = before, maps[y][x]
        y, x = ny, nx

def count(maps):
    sum = 0
    for i in range(r):
        for j in range(c):
            sum += maps[i][j]
    return sum


for _ in range(t):
    maps = spread(maps, [[0] * c for _ in range(r)])
    up()
    down()
print(count(maps))