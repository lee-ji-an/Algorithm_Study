from collections import deque
import sys

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

N, M = map(int, sys.stdin.readline().split())
matrix = [[0]*M for _ in range(N)]

q = deque()
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        matrix[i][j] = 99999
        if (line[j]):
            matrix[i][j] = 9999  # 상어 위치
            q.append((i, j))

cnt = 1
result = 0
while (q):
    for _ in range(len(q)):
        row, col = q.popleft()

        for i in range(8):
            n_row, n_col = row+dr[i], col+dc[i]

            if (0 <= n_row < N and 0 <= n_col < M):
                # 상어 칸이 아니면서 현재 cnt 값보다 안전 거리가 더 큰 값이 저장돼 있을 때
                if (matrix[n_row][n_col] > cnt and matrix[n_row][n_col] != 9999):
                    matrix[n_row][n_col] = cnt
                    q.append((n_row, n_col))
                    result = max(result, cnt)  # 최대 안전거리 업데이트
    
    cnt += 1

print(result)
