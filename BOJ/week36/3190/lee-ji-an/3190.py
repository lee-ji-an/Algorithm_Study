import sys
from collections import deque

input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

N = int(input())
K = int(input())
board = [[False] * N for _ in range(N)]
for i in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = True
L = int(input())
turn_info = deque()
for i in range(L):
    time, direction = input().split()
    time = int(time)
    turn_info.append((time, direction))

visited = [[(False, -1)] * N for _ in range(N)]


def turn(direction):
    if turn_info[0][1] == 'L':
        if direction == UP or direction == DOWN:
            return direction + 2
        elif direction == LEFT:
            return DOWN
        else:
            return UP
    else:
        if direction == LEFT or direction == RIGHT:
            return direction - 2
        elif direction == DOWN:
            return LEFT
        else:
            return RIGHT


time = 0
row, col = 0, 0
direction = RIGHT
tail = (0, 0)
visited[0][0] = (True, RIGHT)
while True:
    time += 1

    # 머리 옮기기
    row, col = row + dr[direction], col + dc[direction]
    if not (0 <= row < N) or not (0 <= col < N) or visited[row][col][0]:
        break
    # 방향 바꾸기
    if turn_info and time == turn_info[0][0]:
        direction = turn(direction)
        turn_info.popleft()

    visited[row][col] = (True, direction)

    # 꼬리 옮기기
    if not board[row][col]:
        tail_dir = visited[tail[0]][tail[1]][1]
        visited[tail[0]][tail[1]] = (False, -1)
        tail = (tail[0] + dr[tail_dir], tail[1] + dc[tail_dir])
    else:
        # 사과가 있을 때
        board[row][col] = False

print(time)
