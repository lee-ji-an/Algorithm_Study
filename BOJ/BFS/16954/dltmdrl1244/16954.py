from collections import deque
import sys
input = sys.stdin.readline
board = deque([list(input().rstrip()) for _ in range(8)])

# 제자리에 있을 수도 있으므로 (0, 0) 쌍도 추가
dy = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, -1, 1, -1, 0, 1, 0]

def bfs():
    # cnt : 회차
    cnt = 0
    visited = deque([[False] * 8 for _ in range(8)])
    visited[7][0] = True
    q = deque()
    q.append((7, 0, 0))

    while q:
        cy, cx, ccnt = q.popleft()

        if (cy, cx) == (0, 8-1):
            return 1

        # 다음 stage로 넘어가면 (다음 회차의 이동에 대한 탐색이 시작되면) 맵이 한칸씩 이동
        if ccnt != cnt:
            visited.appendleft([False] * 8)
            visited.pop()
            board.appendleft(['.'] * 8)
            board.pop()
            cnt = ccnt

        # 현재 위치가 벽이면 바로 종료
        if board[cy][cx] == '#':
             continue

        for i in range(9):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < 8 and 0 <= nx < 8:
                # 방문하지 않은 새로운 점이거나 or 제자리에 있거나
                if board[ny][nx] == '.' and (not visited[ny][nx] or i == 8):
                    visited[ny][nx] = True
                    q.append((ny, nx, ccnt + 1))
    return 0

print(bfs())