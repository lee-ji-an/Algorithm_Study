from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[sys.maxsize]*M for _ in range(N)]
# visited[i][j] = 지금까지 (i, j)를 방문했을 때 벽을 깬 개수의 최솟값
# INF: 방문안함, 0: 안 깬 상태로 방문됨, 1: 하나 깬 상태로 방문됨, N: ...

# 벽은 낮에만 부술 수 있음. 밤인데 벽을 부수고 싶다면 하루 기다려야 함
# 낮/밤은 cnt로 구분. cnt가 1부터 시작하니까 홀수라면 낮, 짝수라면 밤

q = deque([(0, 0, 0)])  # row, col, broken_walls
visited[0][0] = 0
cnt = 1
while (q):
    slicer = len(q)  # pop 한 번 할 때 마다 큐의 길이를 업데이트. 길이 만큼만 pop하고 난 뒤 전역 cnt 증가
    for _ in range(slicer):
        row, col, broken_walls = q.popleft()

        if ((row, col) == (N-1, M-1)):
            print(cnt)
            sys.exit()

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
                        q.append((n_row, n_col, broken_walls))
                # 벽이라면, broken_walls를 1 증가시켜 큐에 추가
                else:
                    # 부술 수 있는 벽이 1개 이상 남아 있고 새로 방문 시 최솟값을 더 작게 만들 수 있다면
                    # 참고) 벽을 부수고 들어가도 최솟값을 더 작게 할 수 있어야 하므로 (broken_walls+1) 과 대소관계 비교
                    if (K-broken_walls > 0 and prev_min > broken_walls+1):
                        if (cnt & 1):  # 낮이라면 그냥 부수고 들어감
                            visited[n_row][n_col] = broken_walls+1  # 주의!) 실제로 부수고 들어가는 경우(낮)에만 방문 처리
                            q.append((n_row, n_col, broken_walls+1))
                        else:  # 밤이면 제자리에서 하루 기다림
                            q.append((row, col, broken_walls))
    
    cnt += 1

print(-1)
