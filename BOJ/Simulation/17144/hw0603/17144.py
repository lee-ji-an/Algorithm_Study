import sys
R, C, T = map(int, sys.stdin.readline().split())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기 청정기 위치 저장
for i in range(R):
    if (house[i][0] == -1):
        top, bottom = i, i+1
        break

# 미세먼지 확산
def spread():
    dr = (-1, 0, 0, 1)
    dc = (0, -1, 1, 0)

    tmp_list = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 공기청정기가 있거나 미세먼지가 없는 칸인 경우 Skip
            if (house[i][j] <= 0):
                continue
            spread_amount = 0
            for k in range(4):
                nr, nc = dr[k]+i, dc[k]+j
                # 범위를 벗어나거나 공기청정기가 있는 칸인 경우 Skip
                if not (0 <= nr < R and 0 <= nc < C and house[nr][nc] != -1):
                    continue
                tmp_list[nr][nc] += house[i][j] // 5  # 인접 칸으로 미세먼지 확산
                spread_amount += house[i][j] // 5  # 확산된 미세먼지 양
            house[i][j] -= spread_amount  # 확산된 미세먼지를 빼줌

    for i in range(R):
        for j in range(C):
            house[i][j] += tmp_list[i][j]


# 공기청정기 이동
def purifier():
    dr_top = [0, -1, 0, 1]
    dr_bottom = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for dr, dc, pos in [(dr_top, dc, top), (dr_bottom, dc, bottom)]:  # 위쪽, 아래쪽
        delta_idx = 0
        prev = 0
        r, c = (pos, 1)
        while (True):
            nr, nc = r + dr[delta_idx], c + dc[delta_idx]
            if ((r, c) == (pos, 0)):
                break
            if (nr < 0 or nr >= R or nc < 0 or nc >= C):
                delta_idx += 1
                continue
            house[r][c], prev = prev, house[r][c]  # swap
            r, c = nr, nc


for _ in range(T):
    spread()  # 확산
    purifier()  # 공기청정기 위쪽 바람

print(sum(map(sum, house))+2)  # 공기청정기(-1)이 두대이므로 2를 더해줌
