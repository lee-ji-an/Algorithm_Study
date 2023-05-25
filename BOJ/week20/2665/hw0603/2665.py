import heapq
import sys

N = int(sys.stdin.readline())
room = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # 방문했을 때 벽 깬 횟수

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

q = [(0, 0, 0)]  # 깬 횟수, row, col

while (q):
    cnt, row, col = heapq.heappop(q)
    if ((row, col) == (N-1, N-1)):  # 목적지 도달
        print(cnt)
        break

    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]

        if not (0 <= nr < N and 0 <= nc < N):
            continue  # 범위 밖 Skip
        if (visited[nr][nc]):
            continue  # 중복방문 제거

        visited[nr][nc] = True
        heapq.heappush(q, (cnt if room[nr][nc] else cnt + 1, nr, nc))
