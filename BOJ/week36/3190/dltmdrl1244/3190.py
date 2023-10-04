import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
# 방향 이동 기록하는 리스트
move = []
move_idx = 0
# 증가하는 방향 -> 오른쪽으로 턴
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 사과
m = int(input())
for _ in range(m):
    y, x = map(int, input().split())
    board[y][x] = 1

# 이동
k = int(input())
for _ in range(k):
    t, d = input().split()
    move.append((int(t), d))


snake = deque([(1, 1)])
# dir = 현재 바라보는 방향
dir = 0
duration = 0
# 몸체가 있는 칸은 1, 없으면 0
body = [[0 for _ in range(n+1)] for _ in range(n+1)]
body[1][1] = 1

while True:
    duration += 1
    ny, nx = snake[0][0] + delta[dir][0], snake[0][1] + delta[dir][1]
    if not (1 <= ny <= n and 1 <= nx <= n) or body[ny][nx]:
        break

    # 사과가 없으면 꼬리를 줄인다
    if not board[ny][nx]:
        sy, sx = snake.pop()
        body[sy][sx] = 0
    # 있으면 사과 칸을 0 처리 한다
    else:
        board[ny][nx] = 0
    
    # 머리를 다음 칸으로 이동하고 몸체 마킹 처리
    snake.appendleft((ny, nx))
    body[ny][nx] = 1
    
    if move_idx < len(move) and duration == move[move_idx][0]:
        # 턴
        dir = (dir + 1) % 4 if move[move_idx][1] == 'D' else (dir + 3) % 4
        move_idx += 1

print(duration)