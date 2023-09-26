from collections import deque
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 우 -> 하 -> 좌 -> 상: 뱀은 처음에 오른쪽을 향한다.
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# board 구축
board = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    board[row-1][col-1] = 1  # 사과 정보

# 방향 전환 정보
L = int(sys.stdin.readline())
rotData = {
    int(k): v
    for k, v in (
        sys.stdin.readline().split() for _ in range(L)
    )
}


row, col, dir = 0, 0, 0
snake = deque()
time = 0
while (True):
    # 뱀 head 위치
    snake.append((row, col))
    time += 1

    # 정해진 방향대로 한칸 전진
    row += dr[dir]
    col += dc[dir]

    # 벽에 부딪히거나 자기 몸과 부딪히면 루프 탈출
    if (not (0 <= row < N and 0 <= col < N) or (board[row][col] == 2)):
        break
    # 사과를 못 먹었다면 꼬리 한 칸 제거
    if not (board[row][col]):
        r, c = snake.popleft()
        board[r][c] = 0  # 빈 칸

    board[row][col] = 2  # 뱀의 body

    # 회전
    if (inst := rotData.get(time, None)):
        dir = (dir+1) % 4 if inst == 'D' else (dir-1) % 4

print(time)
