import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
wall_count = 0
board = []
virus_spot = []
res = float('inf')

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 2:
            virus_spot.append((i, j))
        if row[j] == 1:
            wall_count += 1
max_virus_area = (N * N) - len(virus_spot) - wall_count

def bfs(virus, m):
    global a
    q = deque()
    visited = [[False] * N for _ in range(N)]
    areaCnt = 0
    for i in range(m):
        q.append((virus[i][0], virus[i][1], 0))
        visited[virus[i][0]][virus[i][1]] = True
    while q:
        y, x, cnt = q.popleft()
        for dir in range(4):
            movey = y + dy[dir]
            movex = x + dx[dir]
            if not (0 <= movey < N) or not (0 <= movex < N):
                continue
            if board[movey][movex] == 1:
                continue
            if not visited[movey][movex]:
                if board[movey][movex] == 0:
                    areaCnt += 1
                    if areaCnt == max_virus_area:
                        return cnt + 1
                q.append((movey, movex, cnt + 1))
                visited[movey][movex] = True

    return float('inf')


if max_virus_area != 0:
    for virus in combinations(virus_spot, M):
        res = min(bfs(virus, M), res)
    if res == float('inf'):
        print(-1)
    else:
        print(res)
else:
    print(0)
