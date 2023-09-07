import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx] = True
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    flag = 0
    # 같은 섬의 땅을 기록
    land = [(sy, sx)]

    while q:
        cy, cx, cnt = q.popleft()

        # 바다로 진출했으면 flag 1로 만들어서 다음 번에 만나는 육지가 다른 섬이라는 것을 표시
        if board[cy][cx] == 0:
            flag = 1

        for dy, dx in delta:
            ny, nx = cy + dy, cx + dx

            if not (0 <= ny < n and 0 <= nx < n):
                continue
            
            if board[ny][nx] == 1 and not visited[ny][nx]:
                # flag가 1이면 다른 섬을 발견한 것임
                if flag:
                    return cnt, land
                
                # 1이 아니면 appendleft 해서 같은 섬 내부를 우선 탐색
                visited[ny][nx] = True
                land.append((ny, nx))
                q.appendleft((ny, nx, cnt))
            
            elif board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cnt + 1))
    
    return sys.maxsize, []


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            minDist, land = bfs(i, j)
            ans = min(ans, minDist)
            visited = [[False for _ in range(n)] for _ in range(n)]
            # 같은 섬 내부를 제외한 나머지 부분에 대한 방문처리 정보를 초기화
            for ly, lx in land:
                visited[ly][lx] = True

print(ans)