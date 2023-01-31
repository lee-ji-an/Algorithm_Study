from collections import deque
import sys

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
visited = [[sys.maxsize]*W for _ in range(H)]  # 해당 좌표 도달하기 위해 쓴 점프의 개수

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
move_night = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))

if ((W, H) == (1, 1)):
    sys.exit(print(0))

q = deque([(0, 0, 0)])  # row, col, jump
visited[0][0] = 0
cnt = 0
while (q):
    for _ in range(len(q)):
        row, col, jump = q.popleft()

        if ((row, col) == (H-1, W-1)):
            sys.exit(print(cnt))
        
        # 나이트의 이동을 흉내내는 경우
        if (jump < K):
            for d_r, d_c in move_night:
                n_row, n_col = row+d_r, col+d_c

                if (0 <= n_row < H and 0 <= n_col < W):
                    if (visited[n_row][n_col] > jump+1 and matrix[n_row][n_col] == 0):
                        if ((n_row, n_col) == (H-1, W-1)):
                            sys.exit(print(cnt+1))
                        visited[n_row][n_col] = jump+1
                        q.append((n_row, n_col, jump+1))
            
        # 인접 4방향으로 이동하는 경우
        for i in range(4):
            n_row, n_col = (row+dr[i], col+dc[i])

            if (0 <= n_row < H and 0 <= n_col < W):
                # 빈 곳이고, 방문했을 때 최솟값 업데이트 가능한 경우
                if (visited[n_row][n_col] > jump and matrix[n_row][n_col] == 0):
                    if ((n_row, n_col) == (H-1, W-1)):
                        sys.exit(print(cnt+1))
                    visited[n_row][n_col] = jump
                    q.append((n_row, n_col, jump))
        

    cnt += 1

print(-1)
