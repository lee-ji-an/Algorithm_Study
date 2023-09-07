from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    visit = [[[0] * 64 for i in range(m)] for i in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    q.append((sy, sx, 0))
    visit[sy][sx][0] = 1
    
    while q:
        # 큐 슬라이싱해서 cnt를 관리
        for _ in range(len(q)):
            y, x, key = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= ny < n and 0 <= nx < m) or s[ny][nx] == '#' or visit[ny][nx][key]:
                    continue
                # 해당 key를 가지고 방문하였다고 처리
                if s[ny][nx] == '.':
                    visit[ny][nx][key] = 1
                    q.append((ny, nx, key))

                elif s[ny][nx] == '1':
                    print(cnt + 1)
                    exit()
                
                # 문이면 문을 열 수 있는지 확인하고 열 수 있으면 방문한다.
                elif s[ny][nx].isupper():
                    if key & 1 << (ord(s[ny][nx]) - 65):
                        visit[ny][nx][key] = 1
                        q.append((ny, nx, key))

                # 열쇠라면 그 열쇠를 추가한 nkey를 만들고 방문여부를 다시 확인 후 방문한다
                elif s[ny][nx].islower():
                    nkey = key | (1 << ord(s[ny][nx]) - 97)
                    if not visit[ny][nx][nkey]:
                        visit[ny][nx][nkey] = 1
                        q.append((ny, nx, nkey))
        cnt += 1

n, m = map(int, input().split())
s = list(list(input().rstrip()) for _ in range(n))

for i in range(n):
    for j in range(m):
        if s[i][j] == '0':
            sy, sx = i, j
            s[i][j] = "."

bfs()
print(-1)