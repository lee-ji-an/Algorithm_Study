import sys
from collections import deque
input = sys.stdin.readline

# 먼지 or 청소기로부터 다른 칸들까지의 거리를 계산하여 리턴
def bfs(start):
    q = deque()
    dy = [-1, 0, 0, 1]
    dx = [0, 1, -1, 0]
    v = [[False] * w for _ in range(h)]
    res = [0] * len(dirts)
    # 찾은 먼지 or 청소기 칸의 개수
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
                    # 찾은 먼지의 인덱스에다가 값을 갱신하고 찾은 개수 + 1
                    if (ny, nx) in didx:
                        res[didx[(ny, nx)]] = cnt + 1
                        found += 1

                    v[ny][nx] = True
                    q.append((ny, nx, cnt + 1))

    # 만약 찾은 개수가 더 적다면 도달할 수 없는 칸이 있다는 뜻이므로 False 리턴
    if found != d:
        return False
    return res

# TSP 알고리즘
def dfs(start, visited):
    # 모든 칸을 방문했다면 더이상 남은 거리가 없으므로 0 리턴
    if visited == (1 << d) - 1:
        return 0

    # 방문한 적이 있는 점이면 바로 꺼내먹어요
    if tsp[start][visited] != float('inf'):
        return tsp[start][visited]

    for i in range(1, d):
        # 방문 정보를 확인하고 방문했던 점이면 pass
        if visited & (1 << i):
            continue
        
        # 방문하지 않은 점이면 그 점 i를 방문체크하고 재귀 dfs를 수행한 값에다 현재점 -> i까지의 거리를 더한 값으로 갱신
        tsp[start][visited] = min(tsp[start][visited], dfs(i, visited | (1 << i)) + dist[start][i])

    return tsp[start][visited]


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    board = []
    dirts = []
    didx = {}

    
    for i in range(h):
        tmp = list(input().rstrip())
        for j in range(w):
            if tmp[j] == 'o':
                dirts.insert(0, (i, j))
                tmp[j] = '.'
            elif tmp[j] == '*':
                dirts.append((i, j))
        board.append(tmp)
    d = len(dirts)
    idx = 0
    # 각 먼지들과 청소기에 인덱스를 매겨 거리 계산할 때 사용함
    for dirt in dirts:
        didx[dirt] = idx
        idx += 1

    # 각 점으로부터 다른 점들까지 떨어진 거리를 계산하여 인접 행렬을 만듦
    dist = []
    flag = 0
    for i in range(d):
        t = bfs(dirts[i])
        if t:
            dist.append(t)
        else:
            flag = 1
            break

    if flag:
        print(-1)
        continue
    
    tsp = [[float('inf')] * (1 << d) for _ in range(d)]
    # tsp 수행
    print(dfs(0, 1))