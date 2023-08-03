from collections import deque
import sys

W, H = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(H)]
# 경로를 만들기 위한 최소 선분 개수. (거울개수 == 선분개수-1)
visited = [[sys.maxsize]*W for _ in range(H)]

have_been_pushed = set()  # 중복 방문을 제거하기 위한 set
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

# 첫 C 좌표 찾음
for i in range(H):
    for j in range(W):
        if (board[i][j] == 'C'):
            startPos = (i, j)
            break

q = deque([startPos])
visited[startPos[0]][startPos[1]] = 0

while (q):
    row, col = q.popleft()

    for i in range(4):
        k = 1  # 같은 방향으로 쭉 나아가기 위한 계수
        while (True):
            nr, nc = row+(dr[i])*k, col+(dc[i])*k

            # 범위 밖 Skip
            if not (0 <= nr < H and 0 <= nc < W):
                break
            # 진행 중 벽을 만나면 루프 탈출
            if (board[nr][nc] == '*'):
                break
            # 방문한 적이 있는데, 이번 경로가 이미 거울을 많이 사용한 경우 더 진행할 필요 없음
            if (visited[nr][nc] < visited[row][col] + 1):
                break

            visited[nr][nc] = visited[row][col]+1  # 거울 하나 사용

            if (board[nr][nc] == 'C'):  # 목적지에 도착했으면 정답 출력 후 종료
                sys.exit(print(visited[nr][nc]-1))
            if ((nr, nc) not in have_been_pushed):
                have_been_pushed.add((nr, nc))
                q.append((nr, nc))

            k += 1
