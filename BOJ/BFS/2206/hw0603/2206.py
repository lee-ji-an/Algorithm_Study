from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]  # 0: 방문안함, 1: 안 깬 상태로 방문됨, 2: 하나 깬 상태로 방문됨


q = deque([(0, 0, 1, True)])  # row, col, cnt, breakable
visited[0][0] = 1
result = -1

while (q):
    row, col, cnt, breakable = q.popleft()
    if ((row, col) == (N-1, M-1)):
        result = cnt
        break

    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]

        # matrix 범위 안에 있으면서
        if (0 <= n_row < N and 0 <= n_col < M):
            # 아직 방문하지 않았거나 아직 벽을 깰 수 있는데 과거에 벽을 깬 상태로만 방문했을 경우
            if (not visited[n_row][n_col] or (breakable and visited[n_row][n_col] == 2)):
                # 빈 공간이면 그냥 큐에 추가
                if (matrix[n_row][n_col] == 0):
                    visited[n_row][n_col] = 1 if breakable else 2
                    q.append((n_row, n_col, cnt+1, breakable))
                # 벽이라면, breakable 여부를 확인하고, 가능한 경우에만 큐에 추가
                elif (matrix[n_row][n_col] == 1 and breakable):
                    visited[n_row][n_col] = 2
                    q.append((n_row, n_col, cnt+1, False))

print(result)