import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
# visited : 벽을 몇 개 부순 상태로 방문하였는가 (적을수록 좋다)
visited = [[float('inf')] * m for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

def bfs():
    q = deque()
    # 좌표, cnt, 낮밤, 벽부순 횟수
    q.append([0, 0, 1, True, 0])
    visited[0][0] = 0

    while q:
        cy, cx, cnt, day, walls = q.popleft()

        if (cy, cx) == (n-1, m-1):
            return cnt

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                # 벽이면 낮밤 여부를 따져본다.
                if board[ny][nx] == 1:
                    # 낮이면 바로 부술 수 있다.
                    if day:
                        # 벽 부술 기회가 남았고, 벽 부순 횟수를 더 줄일 수 있으면 넣는다.
                        if walls < k and visited[ny][nx] > walls + 1:
                            visited[ny][nx] = walls + 1
                            q.append([ny, nx, cnt+1, not day, walls + 1])
                    # 밤이면 제자리에서 한 번 기다린다.
                    else:
                        q.append([cy, cx, cnt+1, not day, walls])

                # 벽이 아니면 visited만 검사 후 바로 넣는다.
                else:
                    if visited[ny][nx] > walls:
                        visited[ny][nx] = walls
                        q.append([ny, nx, cnt+1, not day, walls])
    return -1

print(bfs())