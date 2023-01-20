import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# n 세로 m 가로
n, m = map(int, input().split())
board = []
virus = []
zeros = []
ans = float('-inf')

for i in range(n):
    tmp = list(map(int, input().split()))
    for t in range(len(tmp)):
        if tmp[t] == 2:
            virus.append((i, t))

        # 벽 or 바이러스가 아닌 빈칸의 좌표를 다 넣어둔다
        elif tmp[t] == 0:
            zeros.append((i, t))
    board.append(tmp)

# 그 중에서 3개를 뽑는다
for zero in combinations(zeros, 3):
    v = deque(virus)
    arr = copy.deepcopy(board)
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    cnt = 0

    # 벽 세우기
    for i in zero:
        arr[i[0]][i[1]] = 1

    # 바이러스 퍼트리기
    while v:
        cy, cx = v.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = 2
                    v.append((ny, nx))

    # 안전 구역 탐색
    for a in arr:
        cnt += a.count(0)

    ans = max(ans, cnt)

print(ans)