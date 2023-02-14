from collections import deque
import sys

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = day

    union = {(i, j)}  # 연합을 이루는 국가들의 집합
    count = A[i][j]  # 연합의 총 인구 수
    
    while (q):
        row, col = q.popleft()
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if (nr < 0 or nc < 0 or nr >= N or nc >= N):  # A 범위 밖인 경우 Skip
                continue
            if (visited[nr][nc] == day):  # 이미 방문한 지점 제외
                continue
            if (L <= abs(A[nr][nc] - A[row][col]) <= R):  # 인구 차이가 L~R명인 경우 연합에 추가
                visited[nr][nc] = day
                count += A[nr][nc]
                q.append((nr, nc))
                union.add((nr, nc))

    union_size = len(union)
    # 연합 내 국가의 인구 = (연합의 총 인구) / (연합의 크기)
    for row, col in union:
        A[row][col] = count // union_size  # 소수점 버림

    return union_size

day = 0
visited = [[-1] * N for _ in range(N)]
while (True):
    ismove = False  # 인구 이동 플래그
    # BFS 탐색하며 연합 생성
    for i in range(N):
        for j in range(N):
            if (visited[i][j] < day):  # 오늘 방문한 것이 아니면 방문
                ismove = True if (bfs(i, j) > 1) else ismove
    if not (ismove):  # 인구 이동이 없는 경우 루프 탈출
        break
    day += 1

print(day)
