import copy
import sys
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


fish_dict = {}
board = [[0] * 4 for _ in range(4)]
shark = (0, 0, -1)
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        board[i][j//2] = row[j]
        fish_dict[row[j]] = (i, j//2, row[j + 1] - 1)


# 물고기 움직이기
def fish_move(board, fish_dict):
    for i in range(1, 17):
        y, x, direction = fish_dict[i]
        if direction == -1:
            continue
        for j in range(direction, direction + 8):
            d = j % 8
            movey = y + dy[d]
            movex = x + dx[d]
            if not(0 <= movey < 4) or not(0 <= movex < 4):
                continue
            if board[movey][movex] >= 0:
                fish_dict[i] = (movey, movex, d)
                if board[movey][movex] > 0:
                    fish_dict[board[movey][movex]] = (y, x, fish_dict[board[movey][movex]][2])
                board[movey][movex], board[y][x] = board[y][x], board[movey][movex]
                break
    return board, fish_dict


def recur(ans, shark, board, fish_dict):
    global max_cnt
    max_cnt = max(max_cnt, ans)

    flag = False
    y, x, direction = shark

    new_board = [r[:] for r in board]
    new_dict = copy.deepcopy(fish_dict)
    new_board, new_dict = fish_move(new_board, new_dict)   # 물고기 움직이기

    # 상어 움직이기
    for i in range(1, 4):
        movey = y + dy[direction] * i
        movex = x + dx[direction] * i
        if not (0 <= movey < 4) or not (0 <= movex < 4):
            break
        if new_board[movey][movex] == 0:  # 빈칸일 때는 상어가 갈 수 없음
            continue

        flag = True
        target_fish = new_board[movey][movex]
        target_fish_prop = new_dict[target_fish]

        new_board[shark[0]][shark[1]] = 0
        new_board[movey][movex] = -1
        new_shark = (movey, movex, new_dict[target_fish][2])
        new_dict[target_fish] = (-1, -1, -1)

        recur(ans + target_fish, new_shark, new_board, new_dict)  # 재귀호출

        new_board[shark[0]][shark[1]] = -1
        new_board[movey][movex] = target_fish
        new_dict[target_fish] = target_fish_prop

    # flag  F : 상어가 먹을 수 있는 물고기가 없을 때 / T : 먹을 수 있는 물고기가 하나라도 있을 때
    if not flag:
        return


# 상어를 0, 0에 위치시킴
shark = [0, 0, fish_dict[board[0][0]][2]]
ans = board[0][0]
fish_dict[board[0][0]] = (-1, -1, -1)
board[0][0] = -1

max_cnt = 0
recur(ans, shark, board, fish_dict)
print(max_cnt)