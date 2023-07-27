import sys
input = sys.stdin.readline

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

fish_info = [[0] * 3 for _ in range(17)]
board = [[0] * 4 for _ in range(4)]


def move(board, fish_info):
    for i in range(1, 17):
        row, col, dir = fish_info[i][0], fish_info[i][1], fish_info[i][2]
        if row == -1 and col == -1:  # 먹힌 물고기이면
            continue
        for d in range(0, 8):
            mv_r, mv_c = row + dr[(dir + d) % 8], col + dc[(dir + d) % 8]
            if not(0 <= mv_r < 4 and 0 <= mv_c < 4):
                continue
            if board[mv_r][mv_c] == -1:  # 상어가 있는 곳일 때 갈 수 없음
                continue
            another_fish = board[mv_r][mv_c]

            # 물고기 정보 설정
            fish_info[i][0], fish_info[i][1] = mv_r, mv_c
            if another_fish != 0:
                fish_info[another_fish][0], fish_info[another_fish][1] = row, col
            fish_info[i][2] = (dir + d) % 8

            # 공간 정보 설정
            board[row][col], board[mv_r][mv_c] = board[mv_r][mv_c], board[row][col]
            break


def dfs(s_row, s_col, s_dir, fish_cnt, board, fish_info):
    ans = fish_cnt
    new_board = [r[:] for r in board]
    new_fish_info = [r[:] for r in fish_info]

    move(new_board, new_fish_info)
    for d in range(1, 5):
        mv_r, mv_c = s_row + dr[s_dir] * d, s_col + dc[s_dir] * d
        if not (0 <= mv_r < 4 and 0 <= mv_c < 4):
            break
        if new_board[mv_r][mv_c] == 0:  # 물고기가 없으면 넘어감 (상어는 물고기가 있는 곳으로 갈 수 없음)
            continue

        food = new_board[mv_r][mv_c]
        food_dir = new_fish_info[food][2]

        new_board[s_row][s_col] = 0
        new_board[mv_r][mv_c] = -1
        new_fish_info[food] = [-1, -1, -1]

        ans = max(ans, dfs(mv_r, mv_c, food_dir, fish_cnt + food, new_board, new_fish_info))

        new_board[s_row][s_col] = -1
        new_board[mv_r][mv_c] = food
        new_fish_info[food] = [mv_r, mv_c, food_dir]

    return ans


for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num, dir = row[j], row[j + 1] - 1
        fish_info[num] = [i, j//2, dir]
        board[i][j // 2] = num

shark_dir = fish_info[board[0][0]][2]
fish_info[board[0][0]] = [-1, -1, -1]
food = board[0][0]
board[0][0] = -1

print(dfs(0, 0, shark_dir, food, board, fish_info))

