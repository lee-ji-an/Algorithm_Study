import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
q = deque()
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
visited = [[False] * m for _ in range(n)]

# 전체적인 실행 매커니즘은 기본적인 BFS와 동일
def bfs(y, x):
    q.append((y, x, [None, None]))
    visited[y][x] = True

    while q:
        # 이전 좌표를 prev에 가져오는 것이 핵심
        cy, cx, prev = q.popleft()
        visited[cy][cx] = True

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                # ny, nx를 prev과 비교하면서 바로 직전의 점을 다시 q에 넣는 일을 방지
                if (ny != prev[0] or nx != prev[1]):
                    # ny, nx가 prev가 아닌데 방문했었다면, 이는 사이클을 발견했다는 것을 의미
                    if visited[ny][nx] and (board[cy][cx] == board[ny][nx]):
                        print("Yes")
                        exit()

                    # 같은 문자라면 q에 삽입. 이 때 prev 값에는 현재 위치 (cy, cx)를 넣어 줌.
                    if not visited[ny][nx] and board[cy][cx] == board[ny][nx]:
                        q.append((ny, nx, [cy, cx]))

for i in range(n):
    for j in range(m):
        if not visited[i][j] :
            bfs(i, j)
print("No")