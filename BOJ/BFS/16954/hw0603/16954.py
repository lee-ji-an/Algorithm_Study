from collections import deque
import sys

# 7방향 탐색(8방향에서 아래로 한 칸 움직이는 경우 제외) + 제자리
delta = ((0, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
board = [sys.stdin.readline().rstrip() for _ in range(8)]
wall = {(i, j) for i in range(8) for j in range(8) if board[i][j] == '#'}
visited = set()
answer = 0

q = deque([(7, 0)])  # 캐릭터의 초기 위치: 가장 왼쪽 아랫 칸

while (q):
    for _ in range(len(q)):
        row, col = q.popleft()

        # pop 한 좌표가 (벽이 내려와서) 벽이 된 경우 그 경로는 더 보지 않음
        if ((row, col) in wall):
            continue
        
        # 목적지에 도착한 경우
        if ((row, col) == (0, 7)):
            answer = 1
            break

        # 8방향 탐색
        for dr, dc in delta:
            (n_row, n_col) = (row+dr, col+dc)
            if (0 <= n_row < 8 and 0 <= n_col < 8):
                if not ((n_row, n_col) in visited or (n_row, n_col) in wall):
                    visited.add((n_row, n_col))  # 방문 처리
                    q.append((n_row, n_col))

    # 체스판 범위 내에 벽이 존재한다면 visited 초기화
    # (벽이 내려오면 board 정보가 변경되므로 이전의 visited가 의미를 상실하므로)
    if (wall):
        visited.clear()

    # 벽 한 칸 내리기
    wall = {(row+1, col) for row, col in wall if row < 7}

print(answer)
