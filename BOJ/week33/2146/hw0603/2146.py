from collections import deque
import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
border_coord = set()
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)


def mark(row, col, idx):
    matrix[row][col] = idx  # 시작좌표 마킹
    visited[row][col] = True
    q = deque([(row, col)])

    while (q):
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if (visited[nr][nc]):
                continue
            if (matrix[nr][nc] == 0):
                border_coord.add((r, c))
                continue
            matrix[nr][nc] = idx  # 대륙 마킹
            visited[nr][nc] = True  # 안해도 될지도?
            q.append((nr, nc))


def finddist(row, col) -> int:
    visited = [[False]*N for _ in range(N)]

    q = deque([(row, col)])
    visited[row][col] = True
    origin = matrix[row][col]

    dist = 0
    while (q):
        for _ in range(len(q)):
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]

                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if (visited[nr][nc]):
                    continue
                if (matrix[nr][nc] != 0 and matrix[nr][nc] != origin):
                    return dist
                visited[nr][nc] = True
                q.append((nr, nc))

        dist += 1

# 일단 대륙간 번호 붙이기
idx = 1
for i in range(N):
    for j in range(N):
        if (not visited[i][j] and matrix[i][j] == 1):
            mark(i, j, idx)
            idx += 1


# 각 테두리 좌표 별로 bfs
result = sys.maxsize
for row, col in border_coord:
    result = min(result, finddist(row, col))

print(result)
