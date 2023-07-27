import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

R, C = map(int, input().split())

lake = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
swan = []
water_q = deque()

for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            swan.append((r, c))
        if lake[r][c] == '.' or lake[r][c] == 'L':
            water_q.append((r, c))


def find_swan(q):
    next_q = deque()  # 다음에 탐색할 큐
    while q:
        row, col = q.popleft()
        if row == swan[1][0] and col == swan[1][1]:
            return True, None
        for d in range(4):
            mv_r, mv_c = row + dr[d], col + dc[d]

            if not(0 <= mv_r < R and 0 <= mv_c < C):
                continue
            if visited[mv_r][mv_c]:
                continue

            # 현재 얼음이면 next_q, 물이면 q 에 넣음
            if lake[mv_r][mv_c] == 'X':
                next_q.append((mv_r, mv_c))
            else:
                q.append((mv_r, mv_c))
            visited[mv_r][mv_c] = True

    return False, next_q


def melt(q):
    next_q = deque()
    while q:
        row, col = q.popleft()
        for d in range(4):
            mv_r, mv_c = row + dr[d], col + dc[d]
            if not(0 <= mv_r < R and 0 <= mv_c < C):
                continue
            if lake[mv_r][mv_c] == 'X':
                lake[mv_r][mv_c] = '.'
                next_q.append((mv_r, mv_c))  # 이번에 물이 된 곳은 가장자리이므로 다음에 탐색할 곳으로 큐에 넣음
    return next_q


swan_q = deque([(swan[0][0], swan[0][1])])
visited[swan[0][0]][swan[0][1]] = True

day = 0
while True:
    ans_flag, next_q = find_swan(swan_q)
    if ans_flag:
        break
    next_water_q = melt(water_q)

    water_q = next_water_q
    swan_q = next_q
    day += 1

print(day)
