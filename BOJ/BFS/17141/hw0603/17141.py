from collections import deque
from itertools import combinations
import sys

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
N, M = map(int, sys.stdin.readline().split())
lab = [[0]*N for _ in range(N)]
candidate = []
emptyCnt = 0  # 바이러스를 퍼트려야 하는 칸의 개수

for i in range(N):
    lab[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        match (lab[i][j]):
            case 0:
                emptyCnt += 1
            case 2:
                emptyCnt += 1
                candidate.append((i, j))
                lab[i][j] = 0

if (emptyCnt == M):
    print(0)
    sys.exit()

def spread(lab: list, viruscomb: tuple) -> int:
    q = deque(viruscomb)
    spreadCnt = 0
    for row, col in viruscomb:
        spreadCnt += 1
        lab[row][col] = 9  # 바이러스 놓기
    
    sec = 0
    while (q):
        for _ in range(len(q)):
            row, col = q.popleft()

            for i in range(4):
                nrow, ncol = row+dr[i], col+dc[i]

                if not (0 <= nrow < N and 0 <= ncol < N):
                    continue
                if (lab[nrow][ncol]):
                    continue

                lab[nrow][ncol] = 9  # 바이러스 감염
                spreadCnt += 1
                if (spreadCnt == emptyCnt):
                    return sec+1
                q.append((nrow, ncol))

        sec += 1
    
    return sys.maxsize  # 바이러스를 퍼트릴 수 없는 빈 공간이 존재하는 경우


answer = sys.maxsize
for comb in combinations(candidate, M):
    labcopy = [row[:] for row in lab]
    result = spread(labcopy, comb)
    answer = min(answer, result)

print(-1 if answer == sys.maxsize else answer)
