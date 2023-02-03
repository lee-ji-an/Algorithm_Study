from collections import deque
import sys

dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)

N, M = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
area = [[0]*N for _ in range(M)]  # visited 역할을 하는 배열이자 각 좌표별 영역 번호. 0이면 미방문
adjArea = {}
areaSize = [0]

# 시작 좌표 받아서 같은 영역의 좌표에 모두 영역 번호 마킹하고 영역의 넓이 반환
def bfs(row, col, areaNo):
    size = 0
    q = deque([(row, col)])
    area[row][col] = areaNo

    while (q):
        size += len(q)
        for _ in range(len(q)):
            r, c = q.popleft()
            wall = room[r][c]

            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                # 범위 벗어나면 Skip
                if not (0 <= nr < M and 0 <= nc < N):
                    continue
                # 이미 방문한 곳이면 인접 영역 정보 추가 후 Skip
                if (area[nr][nc]):
                    adjArea[areaNo].add(area[nr][nc])
                    adjArea[area[nr][nc]].add(areaNo)
                    continue
                # 벽이 아닌 방향에 대해서만 큐에 노드 삽입
                if not (wall & (1 << i)):
                    area[nr][nc] = areaNo
                    q.append((nr, nc))
    
    return size


areaNo = 1
maxArea = 0
for i in range(M):
    for j in range(N):
        if (area[i][j]):
            continue  # 방문한 지점이라면 Skip
        adjArea[areaNo] = set()
        size = bfs(i, j, areaNo)  # BFS 탐색 진행
        areaSize.append(size)
        maxArea = max(maxArea, size)
        areaNo += 1

print(areaNo-1)  # 성에 있는 방 개수
print(maxArea)  # 가장 넓은 방의 넓이

maxMerged = 0
for i in range(1, areaNo):
    for j in adjArea[i]:
        if (i == j):
            continue
        maxMerged = max(maxMerged, areaSize[i] + areaSize[j])

print(maxMerged)  # 벽 하나 제거 후 얻을 수 있는 최대 공간
