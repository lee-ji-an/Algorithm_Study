from itertools import combinations
from collections import deque
import sys

dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

virus_pos = []  # 바이러스 위치
empty_cnt = 0  # 빈 칸의 개수
INF = sys.maxsize  # 무한대


def bfs(q: deque, empty_cnt: int) -> int:
    visited = [[False] * N for _ in range(N)]
    for i, j in q:
        visited[i][j] = True

    time = 0
    while (q):
        for _ in range(len(q)):  # 큐 길이(=1초 동안 추가된 바이러스 수)만큼 반복
            row, col = q.popleft()

            for d in range(4):
                nrow = row + dr[d]
                ncol = col + dc[d]

                if not (0 <= nrow < N and 0 <= ncol < N):  # 연구실 범위 벗어나면 
                    continue
                if (visited[nrow][ncol]):  # 아직 방문하지 않은 칸이면서
                    continue

                if (lab[nrow][ncol] == 0):  # 빈 칸인 경우
                    q.append((nrow, ncol))
                    visited[nrow][ncol] = 1
                    empty_cnt -= 1
                    if (empty_cnt == 0):  # 더 이상 빈 칸이 없을 경우(모든 칸이 감염된 경우) time 반환
                        return time+1
                elif (lab[nrow][ncol] == 2):  # 비활성화된 바이러스 칸인 경우
                    q.append((nrow, ncol))
                    visited[nrow][ncol] = 1
        
        time += 1
    
    return INF  # 바이러스를 모두 퍼트리는 것이 불가능할 경우


# 완전탐색으로 빈 칸의 개수를 구한 후, 바이러스들의 위치 정보 저장
for i in range(N):
    for j in range(N):
        if not (lab[i][j]):
            empty_cnt += 1  # 빈 칸의 개수 업데이트
        elif (lab[i][j] == 2):
            virus_pos.append((i, j))  # 바이러스 위치 정보 저장

# 빈 칸이 하나도 없다면
if not (empty_cnt):
    sys.exit(print(0))

# 바이러스를 활성 상태로 만들 수 있는 모든 조합에 대해 체크
result = INF
for virus_list in combinations(virus_pos, M):  # (v_p)_C_(M)
    q = deque(virus_list)
    retval = bfs(q, empty_cnt)  # BFS 수행
    result = min(result, retval)  # 최솟값 업데이트

print(-1 if result == INF else result)
