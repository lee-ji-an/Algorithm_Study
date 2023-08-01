import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

C, R = map(int, input().split())

board = []
end_point = []
visited = [[float('inf')] * C for _ in range(R)]
for r in range(R):
    row = input().rstrip()
    board.append(row)
    for c in range(C):
        if row[c] == 'C':
            end_point.append((r, c))


def bfs():
    q = deque([(end_point[0][0], end_point[0][1], 0)])
    visited[end_point[0][0]][end_point[0][1]] = 0
    while q:
        row, col, cnt = q.popleft()
        for d in range(4):
            # 상, 하, 좌, 우로 지도 끝 or 벽을 만날 때까지 탐색함 (직선으로 계속 탐색하므로 사용 거울의 갯수가 모두 같음)
            for distance in range(1, max(R, C)):
                mv_row, mv_col = row + dr[d] * distance, col + dc[d] * distance
                if not(0 <= mv_row < R and 0 <= mv_col < C) or board[mv_row][mv_col] == '*':
                    break
                # visited 에 사용한 거울의 개수를 기록
                # 해당 지점 에 기록된 거울의 갯수가 현재 거울의 갯수보다 클 때 다시 탐색
                if visited[mv_row][mv_col] <= cnt:
                    continue
                if board[mv_row][mv_col] == 'C':
                    return cnt
                visited[mv_row][mv_col] = cnt
                q.append((mv_row, mv_col, cnt + 1))


print(bfs())
