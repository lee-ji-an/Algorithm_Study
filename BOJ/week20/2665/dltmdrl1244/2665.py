from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board = []
for i in range(n):
    board.append(list(map(int, input().strip())))


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if board[nx][ny] == 1: # 흰색이면 같은 방 안이므로 먼저 탐색할 수 있게 appendleft, 방문처리 비용도 그대로
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else: # 검은색이면 방을 뚫고 가므로 비용(visited) +1 추가해서 방문처리
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())