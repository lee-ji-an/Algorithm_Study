def solution(rows, columns, queries):
    from collections import deque
    answer = []
    matrix = [[(r) * columns + c + 1 for c in range(columns)] for r in range(rows)]
    min_value = 0
    # print(matrix)

    for q in queries:
        s_row, s_col, e_row, e_col = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1

        # 큐에 회전할 수를 append
        left, right, top, down = deque(), deque(), deque(), deque()
        for l in range(s_row, e_row + 1):
            left.append(matrix[l][s_col])
        for r in range(e_row, s_row - 1, -1):
            right.append(matrix[r][e_col])
        for t in range(e_col - 1, s_col, -1):
            top.append(matrix[s_row][t])
        for d in range(s_col + 1, e_col):
            down.append(matrix[e_row][d])

        if down:
            min_value = min(min(left), min(right), min(down), min(top))
        else:
            min_value = min(min(left), min(right))

        # 회전시키기
        top.append(left.popleft())
        right.append(top.popleft())
        down.append(right.popleft())
        left.append(down.popleft())

        # 회전 결과를 행렬에 업데이트
        for l in range(s_row, e_row + 1):
            matrix[l][s_col] = left[l - s_row]
        for r in range(e_row, s_row - 1, -1):
            matrix[r][e_col] = right[e_row - r]
        for t in range(e_col - 1, s_col, -1):
            matrix[s_row][t] = top[e_col - 1 - t]
        for d in range(s_col + 1, e_col):
            matrix[e_row][d] = down[d - (s_col + 1)]

        answer.append(min_value)

    return answer