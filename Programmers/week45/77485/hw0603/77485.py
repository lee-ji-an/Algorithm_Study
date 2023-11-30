from collections import deque


def solution(rows, columns, queries):
    answer = []
    matrix = [
        [
            (i-1)*columns+j
                for j in range(1, columns+1)
        ]
            for i in range(1, rows+1)
    ]

    for x1, y1, x2, y2 in queries:
        q = deque([])

        for i in range(y1 - 1, y2):
            q.append(matrix[x1 - 1][i])

        for i in range(x1, x2):
            q.append(matrix[i][y2 - 1])

        for i in range(y2 - 2, y1 - 2, -1):
            q.append(matrix[x2 - 1][i])

        for i in range(x2 - 2, x1 - 1, -1):
            q.append(matrix[i][y1 - 1])

        q.rotate(1)
        answer.append(min(q))

        for i in range(y1 - 1, y2):
            matrix[x1 - 1][i] = q.popleft()

        for i in range(x1, x2):
            matrix[i][y2 - 1] = q.popleft()

        for i in range(y2 - 2, y1 - 2, -1):
            matrix[x2 - 1][i] = q.popleft()

        for i in range(x2 - 2, x1 - 1, -1):
            matrix[i][y1 - 1] = q.popleft()

    return answer
