import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
board = []
num_list = []
max_value = float('inf') * -1
max_element = float('inf') * -1
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    max_element = max(max_element, max(row))


def dfs(y, x, value, cnt):
    global max_value
    if value + max_element * (4 - cnt) <= max_value:
        return
    if cnt == 4:
        max_value = max(max_value, value)
        return
    for i in range(4):
        if cnt == 1 and i == 0:
            continue
        movey = y + dy[i]
        movex = x + dx[i]
        if not (0 <= movey < N) or not(0 <= movex < M) or visited[movey][movex]:
            continue
        visited[movey][movex] = True
        if cnt == 2:
            dfs(y, x, value + board[movey][movex], cnt + 1)
        dfs(movey, movex, value + board[movey][movex], cnt + 1)
        visited[movey][movex] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

print(max_value)
