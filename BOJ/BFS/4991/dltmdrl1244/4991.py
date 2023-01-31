import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def bfs(start):
    q = deque()
    v = [[False] * w for _ in range(h)]
    res = [0] * len(dirts)
    found = 1

    q.append((start[0], start[1], 0))
    v[start[0]][start[1]] = True
    res[didx[start]] = 0

    while q:
        cy, cx, cnt = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < h and 0 <= nx < w:
                if board[ny][nx] != 'x' and not v[ny][nx]:

                    if (ny, nx) in didx:
                        res[didx[(ny, nx)]] = cnt + 1
                        found += 1

                    v[ny][nx] = True
                    q.append((ny, nx, cnt + 1))

    if found != len(dirts):
        return False
    return res


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        exit()

    board = []
    dirts = []
    didx = {}
    dist = []

    for i in range(h):
        tmp = list(input().rstrip())
        for j in range(w):
            if tmp[j] == 'o':
                tmp[j] = '.'
                dirts.insert(0, (i, j))

            elif tmp[j] == '*':
                dirts.append((i, j))
        board.append(tmp)

    idx = 0
    for dirt in dirts:
        didx[dirt] = idx
        idx += 1

    flag = 0
    for i in range(len(dirts)):
        t = bfs(dirts[i])
        if t:
            dist.append(t)
        else:
            flag = 1
            break
    # print(dist)

    if flag:
        print(-1)
        continue

    dirts.remove(dirts[0])
    mindist = float('inf')
    for case in permutations([i+1 for i in range(len(dirts))], len(dirts)):
        tmp = dist[0][case[0]]
        for i in range(len(case) - 1):
            tmp += dist[case[i]][case[i+1]]

        mindist = min(mindist, tmp)

    print(mindist)