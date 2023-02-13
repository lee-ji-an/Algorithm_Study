import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x):
    # result = (y, x) 지역과의 연합
    # population = 그 연합의 인구수
    result = [(y, x)]
    population = board[y][x]
    q = deque()
    visited[y][x] = True
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                # 차이가 l 이상 r 이하이고 방문하지 않은 지역을 탐색
                if l <= abs(board[cy][cx] - board[ny][nx]) <= r and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

                    result.append((ny, nx))
                    population += board[ny][nx]

    return result, population

# 각 연합별로 인구수를 균등하게 배분 (소수점은 버린다)
def move(res):
    for rarr, rcnt in res:
        for ay, ax in rarr:
            board[ay][ax] = rcnt // len(rarr)

ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = 0
    res = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                arr, cnt = bfs(i, j)
                # 연합 크기가 1이 아니라면, 즉 인구 이동이 필요하다면
                if len(arr) != 1:
                    flag = 1
                    res.append((arr, cnt))

    # flag가 0이라면 인구 이동이 X
    if not flag:
        break

    move(res)
    ans += 1

print(ans)