def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n + 1)]

    dr = (1, 0, -1)
    dc = (0, 1, -1)


    cur_row, cur_col, cur_direct = 0, 0, 0
    cur_num = 1
    triangle[cur_row][cur_col] = cur_num

    # 한 줄 먼저 채우기
    for i in range(n - 1):
        cur_num += 1
        cur_row, cur_col = cur_row + dr[cur_direct], cur_col + dc[cur_direct]

        triangle[cur_row][cur_col] = cur_num

    # 나머지 채우기
    for i in range(n - 1, 0, -1):
        cur_direct = (cur_direct + 1) % 3

        for j in range(i):
            cur_num += 1
            cur_row, cur_col = cur_row + dr[cur_direct], cur_col + dc[cur_direct]

            triangle[cur_row][cur_col] = cur_num

    for t in triangle:
        answer.extend(t)

    return answer
