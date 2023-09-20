import sys
from collections import deque
input = sys.stdin.readline

# 중심을 기준으로 3x3 범위 체크해서 돌릴 수 있는지 여부를 반환
def canSpin(y, x):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (0 <= y+i < n and 0 <= x+j < n):
                return False
            
            if board[y+i][x+j] == '1':
                return False
    
    return True

def bfs():
    q = deque()
    cnt = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    # 통나무 좌표 두개의 y좌표가 같다 -> 가로로 놓여있다
    if log_start[0][0] == log_start[1][0]:
        q.append((log_start[1], 1))
        visited.add((log_start[1], 1))
    else:
        q.append((log_start[1], 0))
        visited.add((log_start[1], 0))

    while q:
        for _ in range(len(q)):
            (cy, cx), dir = q.popleft()

            for i in range(4):
                ny = cy + d[i][0]
                nx = cx + d[i][1]

                if dir == 1: # 가로
                    if not (0 <= ny < n and 0 <= nx < n and 0 <= nx + 1 < n and 0 <= nx - 1 < n and board[ny][nx] != '1' and board[ny][nx-1] != '1' and board[ny][nx+1] != '1'):
                        continue
                
                else: # 세로
                    if not (0 <= ny < n and 0 <= nx < n and 0 <= ny + 1 < n and 0 <= ny - 1 < n and board[ny][nx] != '1' and board[ny+1][nx] != '1' and board[ny-1][nx] != '1'):
                        continue

                if (ny, nx) == log_end[0] and dir == log_end[1]:
                    return cnt + 1
                
                if ((ny, nx), dir) not in visited:
                    q.append(((ny, nx), dir))
                    visited.add(((ny, nx), dir))

            # 돌릴 수 있는지 체크 -> 돌릴 수 있으면 좌표는 그대로, 방향만 바꿔서 append
            if canSpin(cy, cx) and ((cy, cx), (dir + 1) % 2) not in visited:
                q.append(((cy, cx), (dir + 1) % 2))
                visited.add(((cy, cx), (dir+1) % 2))
        
        cnt += 1
    
    return 0


n = int(input())
board = []
log_start = []
log_end = []
# 방향 1 : 가로 0 : 세로

for i in range(n):
    t = list(input().rstrip())
    for j in range(n):
        if t[j] == 'B':
            log_start.append((i, j))
            t[j] = '0'
        if t[j] == 'E':
            log_end.append((i, j))
            t[j] = '0'
    
    board.append(t)

# 통나무 좌표 두개의 y좌표가 같다 -> 가로로 놓여있다
if log_end[0][0] == log_end[1][0]:
    log_end = (log_end[1], 1)
else:
    log_end = (log_end[1], 0)

print(bfs())