import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
area = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(n):
    tmp = list(map(int, input().split()))
    area += sum(tmp)
    board.append(tmp)


def water_count(y, x):
    cnt = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 0:
                cnt += 1
    
    return cnt

def melt():
    global board, area
    tmp = [b[:] for b in board]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                tmp[i][j] = board[i][j] - water_count(i, j)
                if tmp[i][j] < 0:
                    tmp[i][j] = 0
                area -= board[i][j] - tmp[i][j]
    
    board = tmp

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    
    
year = 0
while area:
    flag = 0
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                if flag:
                    print(year)
                    exit(0)
                bfs(i, j)
                flag = 1
                
    melt()
    year += 1

print(0)