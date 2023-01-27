from collections import deque

w, h = map(int, input().split())
board = [[b for b in input()] for _ in range(h)]
root = [[99999 for _ in range(w)] for _ in range(h)]

check = []
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            check.append([i, j])
board[check[0][0]][check[0][1]] = 'C1'

root[check[0][0]][check[0][1]] = -1     # -1로 해야 특정 루트로 갔을 때 사용한 거울의 개수를 파악할 수 있음

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]       # 위에서 시계 방향
dq = deque()
dq.append([*check[0]])

while dq:
    y, x = dq.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        while True:     # 기존 방향으로 쭉 나아가기 위해
            if not (0 <= ny < h and 0 <= nx < w): break     # 만약 범위를 벗어난다면
            if board[ny][nx] == '*': break      # 벽을 만난다면
            if root[ny][nx] < root[y][x] + 1: break     # 이미 방문한 곳보다 더 많은 거울을 사용해야 하는 경우, 혹은 재방문을 하는 경우
            dq.append([ny, nx])
            root[ny][nx] = root[y][x] + 1       # 맨 처음 출발했던 위치에서 +1을 해야함
            ny += dy[i]     # 기존 방향으로 계속 나아감
            nx += dx[i]
print(root[check[1][0]][check[1][1]])
