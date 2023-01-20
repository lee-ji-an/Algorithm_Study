import sys
from collections import deque
import copy
input = sys.stdin.readline

# n 세로 m 가로
n, m = map(int, input().split())
board = []
virus = []
ans = float('-inf')

for i in range(n):
    tmp = list(map(int, input().split()))
    for t in range(len(tmp)):
        # 바이러스의 위치에 빠르게 접근하기 위해 위치를 미리 저장해 둠
        if tmp[t] == 2:
            virus.append((i, t))
    board.append(tmp)

# 벽이 3개 세워진 상태로 호출되는 bfs
# v는 바이러스의 좌표로 이루어진 deque
def bfs(v):
    global ans
    arr = copy.deepcopy(board)
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    cnt = 0

    # 바이러스를 퍼트리는 msBFS 수행
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

    return cnt

# 벽을 세우는 것이 유효한지 검증
def adj(y, x):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        # 8방향 인접 칸 중에 범위를 벗어나는 칸이 있거나 (즉 현재 칸이 모서리에 있거나), 벽 or 바이러스가 있는 경우
        if ((ny == -1 or ny == n) or (nx == -1 or nx == m)) or (board[ny][nx] == 1 or board[ny][nx] == 2):
            return True
    # 모서리도 아니고, 주위에 벽 or 바이러스가 없이 허허벌판인 경우
    return False

# 백트래킹 사용하여 벽을 3개 세운다
def back_track(w):
    global ans
    # 벽을 3개 세우면 BFS
    if w == 3:
        v = deque(copy.deepcopy(virus))
        ans = max(ans, bfs(v))

    # 0인 칸을 찾고 벽 개수를 +1 하면서 재귀 호출, 백 트래킹으로 원상복구
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 and adj(i, j):
                    board[i][j] = 1
                    back_track(w + 1)
                    board[i][j] = 0

back_track(0)
print(ans)