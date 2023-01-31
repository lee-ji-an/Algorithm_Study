import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
place = []
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
wallcount = 0

# 입력 받고 바이러스 위치 후보들을 저장
# BFS 수행 후 바이러스가 퍼진 구역을 빠르게 계산하기 위해 벽 개수도 계산 해놓음
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            tmp[j] = 0
            place.append((i, j))
        if tmp[j] == 1:
            wallcount += 1
    board.append(tmp)

ans = float('inf')
# 전체 바이러스 위치 후보들 중 m개를 선택하는 조합 사용
for combi in combinations(place, m):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    cnt = 0
    flag = 0

    # 해당 위치의 board 값을 2(바이러스)로 만들어 주고 큐에 모두 삽입
    for cy, cx in combi:
        board[cy][cx] = 2
        q.append((cy, cx))
        visited[cy][cx] = 0

    # 이번 시행에서의 최댓값, 즉 바이러스가 퍼지는 데 가장 멀리 떨어져 있는 점에 몇 초만에 도달하는지
    local = 0
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] == 0 and visited[ny][nx] == -1:
                    board[ny][nx] = 2
                    cnt += 1
                    visited[ny][nx] = visited[cy][cx] + 1
                    local = max(local, visited[ny][nx])
                    # 만약 ans보다 크면 더 볼 필요가 없으므로 바로 break
                    if local > ans:
                        flag = 1

                    q.append((ny, nx))

            if flag:
                break
        if flag:
            break

    # 만약 모든 구역이 바이러스에 감염되지 않았다면 답을 갱신하지 않는다
    if cnt == n**2 - wallcount - m:
        ans = min(ans, local)

    # 바이러스를 다시 0으로 만들어 줘서 다음 시행에 사용할 수 있도록
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0


if ans == float('inf'):
    print(-1)
else:
    print(ans)