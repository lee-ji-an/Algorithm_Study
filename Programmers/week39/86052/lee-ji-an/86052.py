def solution(grid):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    N, M = len(grid), len(grid[0])
    light_direction = {'S': [0, 1, 2, 3], 'L': [2, 3, 1, 0], 'R': [3, 2, 0, 1]}

    # N * M * 4 배열 / N * M 크기의 배열에 상, 하, 좌, 우에 대해서 탐색 여부를 저장
    cycle_info = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    answer = []

    def cycle_check(row, col, direction):
        cur_row, cur_col, cur_dir = row, col, direction
        cycle_info[cur_row][cur_col][cur_dir] = True

        for i in range(1, N * M * 4 + 1):
            # 다음 위치, 방향 결정
            cur_row, cur_col = (cur_row + dr[cur_dir]) % N, (cur_col + dc[cur_dir]) % M
            cur_dir = light_direction[grid[cur_row][cur_col]][cur_dir]

            # 사이클이 있는 경우
            if cur_row == row and cur_col == col and cur_dir == direction:
                return True, i
            # 이미 전에 탐색한 적이 있는 위치에 오면 무조건 사이클이 아님
            if cycle_info[cur_row][cur_col][cur_dir]:
                return False, 0

            cycle_info[cur_row][cur_col][cur_dir] = True

        return False, 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for d in range(4):
                if not cycle_info[i][j][d]:
                    flag, dist = cycle_check(i, j, d)
                    if flag:
                        answer.append(dist)

    return sorted(answer)
