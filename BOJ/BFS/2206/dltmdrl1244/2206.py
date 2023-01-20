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
    # 첫 번째 인덱스는 '벽을 부술 수 있는 기회', 처음에는 1
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1

    while q:
        a, b, w = q.popleft()
        # 도착점 도달
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < m:
                # 벽이 있는데 기회가 남아 있으면 지나갈 수 있는데 다음에 append 할 때는 0을 넣음
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                # 기회가 없으면 벽이 없는 곳만 지날 수 있음 (이 때 무한루프 피하기 위해 visit이 0이 아닌 (방문한) 점은 제외)
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1

print(bfs())