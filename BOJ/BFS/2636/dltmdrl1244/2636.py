import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cheese = 0
# 치즈 개수 저장
for _ in range(n):
    tmp = list(map(int, input().split()))
    cheese += tmp.count(1)
    board.append(tmp)
    
    
def bfs():
    q = deque()
    # 치즈 외부 아무 곳(0, 0)에서 시작
    q.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    melting = []
    while q:
        cy, cx = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    melting.append((ny, nx))
                    visited[ny][nx] = True
                
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
    
    for y, x in melting:
        board[y][x] = 0
        
    # 녹은 치즈 개수 리턴
    return len(melting)

    
time = 0
last = 0
while cheese > 0:
    last = cheese
    melted = bfs()
    cheese -= melted
    time += 1
    
print(time)
print(last)