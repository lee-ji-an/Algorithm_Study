import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
# 3차원 배열을 만들 때 '층' 에 해당하는 부분을 '벽 부술 수 있는 기회 + 1' 로 만듦
visited = [[[float('inf')] * m for _ in range(n)] for _ in range(k + 1)]
visited[0][0][0] = 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        # f는 벽을 부술 기회를 사용한 횟수를 나타냄
        f, y, x = q.popleft()

        if y == n-1 and x == m-1:
            return visited[f][y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                # '벽이 있고' and '벽 부술 기회가 남았고' and (방문하지 않았거나 기존의 값을 개선할 수 있으면)
                if board[ny][nx] == 1 and f <= k - 1 and visited[f+1][ny][nx] > visited[f][y][x] + 1:
                    visited[f+1][ny][nx] = visited[f][y][x] + 1
                    q.append([f+1, ny, nx])

                # '벽이 아니고' and (방문하지 않았으면)
                elif board[ny][nx] == 0 and (visited[f][ny][nx] == float('inf')):
                    visited[f][ny][nx] = visited[f][y][x] + 1
                    q.append([f, ny, nx])
    return -1

print(bfs())