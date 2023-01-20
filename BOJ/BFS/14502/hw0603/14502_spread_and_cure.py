from itertools import combinations
from collections import deque
import sys

EMPTY, WALL, VIRUS = 0, 1, 2
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
empty_list = []
virus_list = []
N, M = map(int, sys.stdin.readline().split())
max_cnt = 0


# 연구실 형태 입력받으면서 바이러스와 빈 공간의 위치 저장
lab = [[EMPTY]*M for _ in range(N)]
for row in range(N):
    line = [int(col) for col in sys.stdin.readline().split()]
    for col in range(M):
        lab[row][col] = line[col]
        if (lab[row][col] == EMPTY):
            empty_list.append((row, col))
        if (lab[row][col] == VIRUS):
            virus_list.append((row, col))


# 벽 세운 후의 연구실 정보 받아서 BFS 탐색 형태로 바이러스 퍼트린 후 안전 영역의 개수 반환
def spread(lab):
    global virus_added
    q = deque(virus_list)  # 바이러스가 있는 좌표부터 감염을 시작해야 하므로 미리 큐에 삽입
    visited = [[False]*M for _ in range(N)]

    while (q):
        row, col = q.popleft()
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            if (0 <= nrow < N and 0 <= ncol < M):  # 새로운 좌표가 배열의 범위를 벗어나지 않고
                if (not visited[nrow][ncol] and lab[nrow][ncol] == EMPTY):  # 방문하지 않은 곳이면서 빈 공간이라면
                    visited[nrow][ncol] = True  # 방문 표시
                    lab[nrow][ncol] = VIRUS  # 바이러스 배치
                    virus_added.append((nrow, ncol))  # 추가된 바이러스들의 좌표를 따로 저장해둠
                    q.append((nrow, ncol))  # 큐에 해당 좌표 삽입

    return sum(row.count(EMPTY) for row in lab)  # 바이러스 전파 이후 안전 영역의 개수 반환


# 벽을 3개 세우는 모든 경우의 수: 조합
for (r1, c1), (r2, c2), (r3, c3) in combinations(empty_list, 3):
    lab[r1][c1] = lab[r2][c2] = lab[r3][c3] = WALL  # 선택된 좌표에 벽 세우기

    # 세워진 벽에 대해 바이러스 퍼트린 후 안전 영역의 개수 구함
    virus_added = []
    cnt = spread(lab)
    max_cnt = max(max_cnt, cnt)

    # 한 번 시뮬레이션 이후에는 연구소 상태 원상복구
    for r, c in virus_added:
        lab[r][c] = EMPTY  # 바이러스 감염 해제
    lab[r1][c1] = lab[r2][c2] = lab[r3][c3] = EMPTY  # 세운 벽 다시 허물기

print(max_cnt)
