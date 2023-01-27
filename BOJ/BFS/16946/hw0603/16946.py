from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
N, M = map(int, sys.stdin.readline().split())
matrix = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
one_q = deque()
zero_q = deque()

for i in range(N):
    line = list(map(int, list(sys.stdin.readline().rstrip())))
    for j in range(M):
        matrix[i][j] = line[j]
        (one_q if line[j] else zero_q).append((i, j))

area_no = 0
while (zero_q):
    zero_row, zero_col = zero_q.popleft()
    if (visited[zero_row][zero_col]):
        continue
    visited[zero_row][zero_col] = True
    q = deque([(zero_row, zero_col)])
    
    cnt = 0
    same_area = deque([(zero_row, zero_col)])
    while (q):
        q_length = len(q)
        cnt += q_length  # 매 반복마다 큐 길이를 다시 계산하여 1회 시행에 추가된 노드 개수 누적
        for _ in range(q_length):
            row, col = q.popleft()

            for i in range(4):
                n_row = row + dr[i]
                n_col = col + dc[i]

                if (0 <= n_row < N and 0 <= n_col < M):
                    if not (visited[n_row][n_col] or matrix[n_row][n_col] > 0):
                        visited[n_row][n_col] = True
                        q.append((n_row, n_col))
                        same_area.append((n_row, n_col))

    # 같은 영역으로 마킹된 좌표들의 값을 모두 그 영역의 넓이로 변경 (원래 벽과 구분하기 위해 음수로 저장)
    while (same_area):
        row, col = same_area.popleft()
        matrix[row][col] = (cnt, area_no)  # 구역에 번호를 붙여서 나중에 구별할 수 있도록
    area_no += 1


# 벽이 있는 좌표를 순회하며 인접 영역의 넓이 구함
while (one_q):
    row, col = one_q.popleft()
    checked_area = set()
    size = 0
    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]
        if (0 <= n_row < N and 0 <= n_col < M):
            if (type(matrix[n_row][n_col]) is tuple and matrix[n_row][n_col][1] not in checked_area):
                checked_area.add(matrix[n_row][n_col][1])
                size += matrix[n_row][n_col][0]
    
    matrix[row][col] = size + 1


for i in range(N):
    for j in range(M):
        if not(type(matrix[i][j]) is tuple):
            print(matrix[i][j] % 10, end='')
        else:
            print(0, end='')
    print()
