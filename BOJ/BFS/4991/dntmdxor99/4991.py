import sys
from collections import deque
import itertools

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(board, y, x):
    dq = deque([[y, x]])
    dist = [[-1] * w for _ in range(h)]        # 어느 한 정점에서 다른 정점까지의 거리를 나타내는 리스트
    dist[y][x] = 0
    while dq:
        for _ in range(len(dq)):
            y, x = dq.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and dist[ny][nx] == -1:
                    # 방문하지 않았다면 방문한다.
                    # 이미 방문한 정점이라면 최적이 보장되므로 방문할 필요가 없다.
                    if board[ny][nx] != 'x':
                        dq.append([ny, nx])
                        dist[ny][nx] = dist[y][x] + 1

    return dist


def sol(w, h):
    board = [[b for b in list(sys.stdin.readline().strip())] for _ in range(h)]

    pos = []        # 청소기와 쓰레기의 좌표
    for y in range(h):
        for x in range(w):
            if board[y][x] == '*':
                pos.append((y, x))
            elif board[y][x] == 'o':
                pos.insert(0, (y, x))       # 청소기는 항상 0에 들어가야 함

    flag = True
    l = len(pos)
    check = [[0] * l for _ in range(l)]     # 0번 인덱스는 청소기, 1, 2, ... , n은 쓰레기

    for i, p in enumerate(pos):     # 한 정점에서 다른 정점까지의 거리를 파악함
        if flag:
            dist = bfs(board, *p)       # bfs를 사용하여 한 정점에서 다른 정점까지의 거리를 찾음
            for j, n_p in enumerate(pos):       # 인접 행렬에 집어넣음
                if (d := dist[n_p[0]][n_p[1]]) == -1:
                    print(-1)
                    flag = False
                    break
                check[i][j] = d

    if flag:
        minimum = float('inf')
        for it in itertools.permutations(range(1, l), l - 1):
            # 시작은 항상 0(청소기)이므로, 쓰레기에서 다른 쓰레기로 이동하는 경우의 수를 모두 살펴봄
            dist = 0
            it = tuple([0]) + it
            for j in range(l - 1):      # 모든 거리를 구해봄
                dist += check[it[j]][it[j + 1]]
            minimum = dist if dist < minimum else minimum       # 거기서 최적을 찾음
        print(minimum)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        exit(0)
    sol(w, h)
