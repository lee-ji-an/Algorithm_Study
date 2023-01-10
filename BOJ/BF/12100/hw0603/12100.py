from itertools import product
from collections import deque
import sys

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(sys.stdin.readline())
orig_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 방향에 맞게 이동 후 board 값 변경
def move(dir: int):
    global board
    for i in range(N):
        line = deque()
        add = line.append if not dir % 2 else line.appendleft  # Up, Left인 경우 append, Down, Right인 경우 appendleft
        buffer = 0
        for j in (range(N) if not dir % 2 else range(N-1, -1, -1)):  # 이동 방향에 따라 인덱스 증가 방향 설정
            cur = board[i][j] if dir >= 2 else board[j][i]
            if (cur):  # 현재 칸에 0이 아닌 숫자가 있다면
                if (buffer == cur):  # 버퍼에 있는 수와 같다면
                    add(buffer << 1)  # 버퍼 flush
                    buffer = 0  # 버퍼를 비움
                else:  # 같지 않다면
                    if (buffer):  # 버퍼에 저장된 수가 있다면 flush
                        add(buffer)
                    buffer = cur  # 버퍼에 현재 수 저장
        if (buffer):
            add(buffer)  # 마지막까지 버퍼에 남아있는 수 flush
        for _ in range(N - len(line)):
            add(0)  # 부족한 원소 수 만큼 0 채우기

        if (dir < 2):  # Up, Down
            for idx, item in enumerate(line):
                board[idx][i] = item
        else:  # Left, Right
            board[i] = list(line)

result = 0
for dirlist in product(range(4), repeat=5):
    board = [row[:] for row in orig_board]  # 단순 2D List의 경우 copy.deepcopy()보다 훨씬 빠름
    for dir in dirlist:
        move(dir)
    result = max(max(max(x) for x in board), result)

print(result)
