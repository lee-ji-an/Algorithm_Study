from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
W, H = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(H)]
visited = [[sys.maxsize] * W for _ in range(H)]  # 해당 좌표에 도달하기 위한 경로의 선분 개수 (즉, 거울 개수 + 1)
have_been_pushed = set()  # 중복 방문을 제거하기 위한 set

# 시작 지점과 도착 지점 구함
(s_row, s_col), (e_row, e_col) = [(i, j) for i in range(H) for j in range(W) if board[i][j] == 'C']

# 시작 지점에서 BFS 탐색 출발
q = deque([(s_row, s_col)])
visited[s_row][s_col] = 0
while (q):
    row, col = q.popleft()

    for i in range(4):
        n_row, n_col = row + dr[i], col + dc[i]

        # 레이저를 직선으로 쏘는 것 처럼
        # 방향을 한 번 정했으면 그 방향으로 최대한 멀리 갈 수 있는 곳 까지 계속 탐색 진행
        while (0 <= n_row < H and 0 <= n_col < W):
            # 진행 중 벽을 만나면 루프 탈출
            if (board[n_row][n_col] == '*'):
                break
            # 방문한 적이 있는데, 이번 경로에서 최솟값을 업데이트 할 수 없는 경우 더 볼 필요 X
            if (visited[n_row][n_col] < visited[row][col] + 1):
                break

            # 방문 처리 후 큐에 삽입. 방향이 한번 변했으므로 +1 해서 visited 에 저장
            visited[n_row][n_col] = visited[row][col] + 1
            if ((n_row, n_col) == (e_row, e_col)):  # 목적지에 도착했으면 정답 출력 후 종료
                sys.exit(print(visited[e_row][e_col]-1))
            
            if ((n_row, n_col) not in have_been_pushed):
                have_been_pushed.add((n_row, n_col))
                q.append((n_row, n_col))

            # 같은 방향의 다음 좌표
            n_row, n_col = n_row + dr[i], n_col + dc[i]

raise Exception("BFS 탐색 중 경로를 찾지 못함")
