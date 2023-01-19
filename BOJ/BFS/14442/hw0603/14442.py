from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[sys.maxsize]*M for _ in range(N)]
# visited[i][j] = 지금까지 (i, j)를 방문했을 때 벽을 깬 개수의 최솟값
# INF: 방문안함, 0: 안 깬 상태로 방문됨, 1: 하나 깬 상태로 방문됨, N: ...


q = deque([(0, 0, 1, 0)])  # row, col, cnt, broken_walls
visited[0][0] = 1
result = -1
while (q):
    row, col, cnt, broken_walls = q.popleft()
    if ((row, col) == (N-1, M-1)):
        result = cnt
        break

    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]

        # matrix 범위 안에 있으면서
        if (0 <= n_row < N and 0 <= n_col < M):
            """
            visited 배열을 참조하여 지금까지 해당 좌표에 방문했을 때 부순 벽의 개수 최솟값을 보고
            내가 이번에 새로 방문했을 때 최솟값을 더 작게 만들 수 있을 때만 큐에 넣어야 함
            """
            prev_min = visited[n_row][n_col]  # (n_row, n_col)에서의 과거 최솟값

            # 빈 공간이면 그냥 큐에 추가
            if (matrix[n_row][n_col] == 0):
                if (prev_min > broken_walls):
                    visited[n_row][n_col] = broken_walls
                    q.append((n_row, n_col, cnt+1, broken_walls))
            # 벽이라면, broken_walls를 1 증가시켜 큐에 추가
            else:
                # 부술 수 있는 벽이 1개 이상 남아 있고 새로 방문 시 최솟값을 더 작게 만들 수 있다면
                # 참고) 벽을 부수고 들어가도 최솟값을 더 작게 할 수 있어야 하므로 (broken_walls+1) 과 대소관계 비교
                if (K-broken_walls > 0 and prev_min > broken_walls+1):
                    visited[n_row][n_col] = broken_walls+1
                    q.append((n_row, n_col, cnt+1, broken_walls+1))

print(result)
