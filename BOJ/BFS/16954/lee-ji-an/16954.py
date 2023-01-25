import sys
from collections import deque

input = sys.stdin.readline
dx = (0, 0, -1, 1, -1, -1, 1, 1, 0)
dy = (-1, 1, 0, 0, -1, 1, -1, 1, 0)
board = ["" for _ in range(8)]
visited = [[0] * 8 for _ in range(8)]
walls = {}
flag = True
height = 8
for i in range(8):
    row = input().rstrip()
    board[i] = row
    for j in range(len(row)):
        if row[j] == '#':
            if j in walls:
                walls[j].add(i)
            else:
                walls[j] = {i}
            if flag:
                height = i
                flag = False


def bfs():
    q = deque()
    q.append((7, 0, 0))
    visited[7][0] = 0
    while q:
        y, x, cnt = q.popleft()
        for i in range(9):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= 8 or movex < 0 or movex >= 8:
                continue
            if 8 - height <= cnt:  # 벽이 모두 내려갔다면 return 1
                return 1
            if visited[movey][movex] < cnt + 1:
                if movex in walls:
                    if movey - cnt in walls[movex]:  # 빈공간이 아니면 continue
                        continue
                    if movey - cnt - 1 in walls[movex]:  # 벽을 옮겼을 때 벽과 만나면 continue
                        continue
                if movey == 0 and movex == 7:
                    return 1
                q.append((movey, movex, cnt + 1))
                visited[movey][movex] = cnt + 1
    return 0


print(bfs())
