import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
garbages = []

for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        if tmp[j] == 'g':
            garbages.append((i, j))

        elif tmp[j] == 'F':
            ey, ex = i, j
        
        elif tmp[j] == 'S':
            sy, sx = i, j

    board.append(tmp)

for gy, gx in garbages:
    for i in range(4):
        ny = gy + dy[i]
        nx = gx + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 'g':
            board[ny][nx] = 1

board[sy][sx] = '.'
board[ey][ex] = '.'

def betterthan(a, b):
    if a[0] < b[0]:
        return True
    
    if a[0] == b[0] and a[1] < b[1]:
        return True

    return False


def bfs():
    q = deque()
    search = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]

    search[sy][sx] = [0, 0]
    q.append((sy, sx))

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                t = search[cy][cx][:]
                if board[ny][nx] == 'g':
                    t[0] += 1
                elif board[ny][nx] == 1:
                    t[1] += 1

                if betterthan(t, search[ny][nx]):
                    search[ny][nx] = t
                    q.append((ny, nx))
    
    return search[ey][ex]

print(*bfs())