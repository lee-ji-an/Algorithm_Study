import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
board = []
target = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

for i in range(h):
    tmp = list(input().rstrip())
    for j in range(w):
        if tmp[j] == 'C':
            target.append((i, j))
    board.append(tmp)

q = deque()
# 이 점에 방문할 때까지의 최소 커브 횟수
visited = [[float('inf')] * w for _ in range(h)]

q.append((target[0][0], target[0][1]))
visited[target[0][0]][target[0][1]] = 0

while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]


        while 0 <= ny < h and 0 <= nx < w:
            # 그 방향으로 쭉 직진하면서 더이상 visited 정보를 업데이트 할 수 없을 때까지 탐색
            # 이후로는 방향이 꺾이는 경우만 탐색하게 된다 (왔던 방향으로 그대로 보면 visited[ny][nx]가 visited[cy][cx]와 같으므로 break문에 걸려버림)
            if board[ny][nx] == '*' or visited[ny][nx] < visited[cy][cx] + 1:
                break

            visited[ny][nx] = visited[cy][cx] + 1
            if (ny, nx) == (target[1][0], target[1][1]):
                # 처음에 쏠 때 +1을 했으므로 -1 한 값을 출력
                print(visited[ny][nx] - 1)
                exit()

            q.append((ny, nx))
            # 방향으로 계속 진행
            ny += dy[i]
            nx += dx[i]