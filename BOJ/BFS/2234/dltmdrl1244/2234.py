import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [[-1] * w for _ in range(h)]
root = [[-1] * w for _ in range(h)]
areacnt = 0
maxarea = -1
size = {}
ids = 0

# 서북동남
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    cnt = 1
    visited[y][x] = ids
    root[y][x] = ids

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if not board[cy][cx] & (1 << i) and visited[ny][nx] == -1:
                    cnt += 1
                    visited[ny][nx] = ids
                    root[ny][nx] = ids
                    q.append((ny, nx))

    return cnt


def find_adj(y, x):
    q = deque()
    q.append((y, x))
    v = [[False] * w for _ in range(h)]
    v[y][x] = True
    adj = set()

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if not board[cy][cx] & (1 << i) and not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny, nx))

                if board[cy][cx] & (1 << i) != 0 and root[cy][cx] != root[ny][nx]:
                    if root[ny][nx] not in adj:
                        adj.add(root[ny][nx])

    return list(adj)


start = []
for i in range(h):
    for j in range(w):
        # 방문하지 않은 새 영역의 점을 찾으면
        if visited[i][j] == -1:
            # 그 점을 저장하고 나중에 인접 영역을 찾을 때 시작점으로 사용할 수 있게 함
            start.append((i, j))
            # 영역 수 갱신
            areacnt += 1
            # bfs 수행하면서 그 점과 같은 영역을 세서 넓이 리턴
            a = bfs(i, j)
            size[ids] = a
            ids += 1
            # 최대 넓이 갱신
            maxarea = max(maxarea, a)

adj = []
# 시작점(각 영역마다 하나씩 넣어놓은 것)에서 bfs 탐색하여 자기가 속한 영역과 인접한 영역의 id값 탐색
for s in start:
    adj.append(find_adj(s[0], s[1]))

maxunion = 0
# 각 영역에 대해, 각 인접한 영역에 대해 union 한다 가정하고 합친 넓이 갱신
for i in range(ids):
    for j in adj[i]:
        maxunion = max(maxunion, size[i] + size[j])

print(areacnt)
print(maxarea)
print(maxunion)
