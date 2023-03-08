import sys

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)
space = [[] for _ in range(4)]  # 4x4 공간

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    fish = []
    for j in range(4):
        fish.append([line[2*j], line[2*j+1]-1])  # [물고기 번호(a_i), 방향(b_i)]
    space[i] = fish

max_score = 0

def dfs(row_shark: int, col_shark: int, score: int, board: list[list[list[int]]]):
    global max_score

    score += board[row_shark][col_shark][0]
    max_score = max(max_score, score)
    board[row_shark][col_shark][0] = 0

    # 1~16번 물고기 움직임
    for fishNum in range(1, 17):
        row_fish, col_fish = -1, -1
        for row in range(4):
            for col in range(4):
                if (board[row][col][0] == fishNum):
                    row_fish, col_fish = row, col
                    break
        if ((row_fish, col_fish) == (-1, -1)):
            continue
        dir_fish = board[row_fish][col_fish][1]

        for i in range(8):
            nd = (dir_fish+i) % 8
            nr, nc = row_fish + dr[nd], col_fish+dc[nd]

            # 범위 밖 Skip
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            # 상어 자리 Skip
            if (nr == row_shark and nc == col_shark):
                continue

            board[row_fish][col_fish][1] = nd  # 물고기 방향 바꾸고
            board[row_fish][col_fish], board[nr][nc] = board[nr][nc], board[row_fish][col_fish]  # 물고기 위치 Swap
            break

    # 상어가 물고기 먹음
    dir_shark = board[row_shark][col_shark][1]
    for i in range(1, 5):
        nr = row_shark + dr[dir_shark]*i
        nc = col_shark + dc[dir_shark]*i
        if ((0 <= nr < 4 and 0 <= nc < 4) and board[nr][nc][0] > 0):
            dfs(nr, nc, score, [[r[:] for r in row] for row in board])

dfs(0, 0, 0, space)
print(max_score)
