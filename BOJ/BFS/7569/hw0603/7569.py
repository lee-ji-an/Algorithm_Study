from collections import deque
import sys

dx = (0, 1, 0, -1, 0, 0)
dy = (-1, 0, 1, 0, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

M, N, K = map(int, sys.stdin.readline().split())
warehouse = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K)]
ripe = []
empty = []

def bfs():
    q = deque([pos for pos in ripe])  # 멀티소스 BFS
    
    result = 0
    while (q):
        for _ in range(len(q)):
            z, y, x = q.popleft()

            for i in range(6):  # 6방향 탐색
                nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
                if not (0 <= nz < K and 0 <= ny < N and 0 <= nx < M):
                    continue
                if (warehouse[nz][ny][nx] == 0):  # 익지 않은 토마토의 경우 익힘
                    warehouse[nz][ny][nx] = 1
                    q.append((nz, ny, nx))
        result += 1

    return result-1


for z in range(K):
    for y in range(N):
        warehouse[z][y] = list(map(int, sys.stdin.readline().split()))
        for x in range(M):
            if ((current := warehouse[z][y][x]) != -1):  # 빈 칸이 아니라면
                (ripe if current else empty).append((z, y, x))  # 익은 칸과 익지 않은 칸 따로 좌표 저장

days = bfs()

for z, y, x in empty:
    if not (warehouse[z][y][x]):
        days = -1
        break

print(days)
