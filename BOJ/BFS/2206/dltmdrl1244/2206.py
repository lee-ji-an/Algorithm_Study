import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1

    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])

                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1

print(bfs())