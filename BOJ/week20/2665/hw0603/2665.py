import heapq
import sys

N = int(sys.stdin.readline())
room = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[sys.maxsize] * N for _ in range(N)]  # 방문했을 때 벽 깬 횟수

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

        if (visited[nr][nc] > cnt):  # 현재 노드보다 이전에 벽을 더 많이 깬 채로 방문됐을 경우: 다시 방문 필요
            if (room[nr][nc] == 0):  # 벽이라면 깨고 지나감
                visited[nr][nc] = cnt+1
                heapq.heappush(q, (cnt+1, nr, nc))
            else:
                visited[nr][nc] = cnt  # 벽이 아니면 그냥 지나감
                heapq.heappush(q, (cnt, nr, nc))
