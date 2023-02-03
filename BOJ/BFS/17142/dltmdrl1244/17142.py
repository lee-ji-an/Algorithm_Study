import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
virus = []
target = n**2
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

# target : 퍼트려야 하는 최종 바이러스 개수
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            virus.append((i, j))
            tmp[j] = 0
        if tmp[j] == 1:
            target -= 1
    board.append(tmp)


def bfs(b, combi):
    q = deque()
    visitcnt = 0

    # 비활성 바이러스도 바이러스로 카운트하되 큐에는 넣지 않는다
    for v in range(len(virus)):
        visitcnt += 1

        if v in combi:
            q.append((virus[v][0], virus[v][1]))
            b[virus[v][0]][virus[v][1]] = 2
        else:
            b[virus[v][0]][virus[v][1]] = 9

    if visitcnt == target:
        return 0

    sec = 0
    while q:
        # 큐 슬라이싱
        for _ in range(len(q)):
            cy, cx = q.popleft()

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if 0 <= ny < n and 0 <= nx < n:
                    if b[ny][nx] in (0, 9):
                        # 빈 칸이라면 cnt + 1
                        if b[ny][nx] == 0:
                            visitcnt += 1
                        b[ny][nx] = 2

                        if visitcnt == target:
                            return sec + 1

                        q.append((ny, nx))

        sec += 1
        # 만약 이전에 구해놓은 답보다 커지면 더 볼 필요 X, 즉시 리턴
        if sec > ans:
            return float('inf')
    # 큐가 빌 때까지 visitcnt가 target을 만족시키지 못하면 최댓값 리턴
    return float('inf')

ans = float('inf')
# 바이러스 후보 위치 중에서 활성 바이러스의 위치를 조합으로 추출
for combi in combinations([i for i in range(len(virus))], m):
    bcopy = [b[:] for b in board]
    ans = min(ans, bfs(bcopy, set(combi)))

if ans == float('inf'):
    print(-1)
else:
    print(ans)