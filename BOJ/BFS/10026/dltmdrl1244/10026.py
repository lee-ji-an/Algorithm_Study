import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
normal = []
jaehan = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for i in range(n):
    tmp = list(input().rstrip())
    # 정상인
    normal.append(tmp[:])

    # 재한이
    for j in range(n):
        if tmp[j] == 'G':
            tmp[j] = 'R'
    jaehan.append(tmp)

def normalbfs(i, j):
    q = deque()
    q.append((i, j))
    nvisited[i][j] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if normal[ny][nx] == normal[cy][cx] and not nvisited[ny][nx]:
                    nvisited[ny][nx] = True
                    q.append((ny, nx))


def jaehanbfs(i, j):
    q = deque()
    q.append((i, j))
    jvisited[i][j] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if jaehan[ny][nx] == jaehan[cy][cx] and not jvisited[ny][nx]:
                    jvisited[ny][nx] = True
                    q.append((ny, nx))

nvisited = [[False] * n for _ in range(n)]
jvisited = [[False] * n for _ in range(n)]
normalans = 0
jaehanans = 0
for i in range(n):
    for j in range(n):
        if not nvisited[i][j]:
            normalbfs(i, j)
            normalans += 1

        if not jvisited[i][j]:
            jaehanbfs(i, j)
            jaehanans += 1

print(normalans, jaehanans)