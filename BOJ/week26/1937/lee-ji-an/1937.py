import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(input())
forest = []
sorted_num = []
visited = [[1] * N for _ in range(N)]
ans = 1

for i in range(N):
    forest.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        sorted_num.append((forest[i][j], i, j))
sorted_num.sort()  # 칸에 적힌 숫자를 기준으로 정렬

for i in range(N*N):  # 숫자가 작은 칸부터 탐색
    num, row, col = sorted_num[i]
    cnt = 1
    for d in range(4):
        mv_r, mv_c = row + dr[d], col + dc[d]
        if not (0 <= mv_r < N and 0 <= mv_c < N):
            continue
        if forest[mv_r][mv_c] < forest[row][col]:  # 나보다 숫자가 작은 칸에 대해서 +1을 저장
            cnt = max(cnt, visited[mv_r][mv_c] + 1)
    visited[row][col] = cnt

print(max(map(max, visited)))
