from collections import deque
import sys

d = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
graph = [[-1] * N for _ in range(N)]
graph[r1][c1] = 0

q = deque([(r1, c1)])
while (q):
    row, col = q.popleft()
    for dr, dc in d:
        n_row, n_col = row+dr, col+dc
        if (0 <= n_row < N and 0 <= n_col < N and graph[n_row][n_col] == -1):
            if ((n_row, n_col) == (r2, c2)):  # 목적지를 만난 경우 진행을 멈추고 출력 후 종료
                print(graph[row][col] + 1)
                sys.exit()
            q.append((n_row, n_col))
            graph[n_row][n_col] = graph[row][col] + 1

print(graph[r2][c2])
