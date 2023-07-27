import sys

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)
space = [[] for _ in range(4)]  # 4x4 공간
result = 0

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    fish_in_line = [[line[2*j], line[2*j+1]-1] for j in range(4)]
    space[i] = fish_in_line


def dfs(shark_row, shark_col, score, board) -> int:
    score += board[shark_row][shark_col][0]  # 상어가 (row, col)로 이동 후 해당 칸의 물고기를 먹음
    board[shark_row][shark_col][0] = 0  # 잡아먹힌 물고기는 번호를 0으로 마킹

    # 남아있는 물고기들을 각각 움직임
    for fishIdx in range(1, 17):
        # 16개 칸을 완전탐색하며 현재 이동시킬 물고기의 위치와 방향을 찾음
        fish_row, fish_col, fish_dir = -1 , -1, -1
        for r in range(4):
            for c in range(4):
                if (board[r][c][0] == fishIdx):
                    fish_row, fish_col, fish_dir = r, c, board[r][c][1]
                    break
        # 이미 먹힌 물고기인 경우 다음 물고기로 continue
        if (fish_dir == -1):
            continue
        
        for i in range(8):
            nd = (fish_dir+i) % 8
            nr, nc = (fish_row+dr[nd], fish_col+dc[nd])

            # board 범위 밖 Skip
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            # 상어 자리인 경우 Skip
            if ((nr, nc) == (shark_row, shark_col)):
                continue

            board[fish_row][fish_col][1] = nd  # 물고기 방향 바꿈
            board[fish_row][fish_col], board[nr][nc] = board[nr][nc], board[fish_row][fish_col]  # 두 물고기 위치 스왑
            break
    
    # 상어가 물고기를 먹음
    # 상어는 자신의 방향에 있는 모든 칸을 선택적으로 움직일 수 있으므로 각 경우를 모두 탐색
    shark_dir = board[shark_row][shark_col][1]
    score_max = score  # 이번 노드의 3개 자식노드에 대한 최댓값
    for i in range(1, 4):  # 4x4 공간이므로 상어는 1~3칸까지 이동 가능
        nr, nc = (shark_row+dr[shark_dir]*i, shark_col+dc[shark_dir]*i)
        # 범위 밖 Skip
        if not (0 <= nr < 4 and 0 <= nc < 4):
            continue
        # 물고기가 없는 칸(이미 잡아먹은 물고기의 칸)이라면 Skip
        if (board[nr][nc][0] == 0):
            continue

        copied_board = [[r[:] for r in row] for row in board]
        score_max = max(score_max, dfs(nr, nc, score, copied_board))
    
    return score_max


print(dfs(0, 0, 0, space))
