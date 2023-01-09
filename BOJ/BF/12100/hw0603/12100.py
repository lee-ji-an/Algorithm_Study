from itertools import product
from collections import deque
import sys
import copy

# 상, 하, 좌, 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N = int(sys.stdin.readline())
orig_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 보드 출력 함수 (테스트용)
def printboard(int: dir, board: list):
    data = ("상", "하", "좌", "우")
    print(f"<< {data[dir]} >>")
    print(*board, sep="\n")
    print()

# 방향에 맞게 이동 후 board 값 변경
def moveLR(dir: int):
    global board

    for i, row in enumerate(board):
        line = deque()
        add = line.append if dir == 2 else line.appendleft
        buffer = 0
        for j in (range(N) if dir == 2 else range(N-1, -1, -1)):
            # 현재 칸에 숫자가 있다면
            if (cur := board[i][j]):
                # 버퍼에 있는 수와 같다면
                if (buffer == cur):
                    add(buffer * 2) # 버퍼 flush
                    buffer = 0 # 버퍼를 비움
                # 같지 않다면
                else:
                    # 버퍼에 저장된 수가 있다면 flush
                    if (buffer):
                        add(buffer)
                    buffer = cur # 버퍼에 현재 수 저장
        add(buffer)
        if (dir == 2):
            line = list(line) + [0] * (N - len(line))
        else:
            line = [0] * (N - len(line)) + list(line)
        board[i] = line


def moveUD(dir: int):
    global board

    for i, row in enumerate(board):
        line = deque()
        add = line.append if dir == 0 else line.appendleft
        buffer = 0
        for j in (range(N) if dir == 0 else range(N-1, -1, -1)):
            # 현재 칸에 숫자가 있다면
            if (cur := board[j][i]):
                # 버퍼에 있는 수와 같다면
                if (buffer == cur):
                    add(buffer * 2)  # 버퍼 flush
                    buffer = 0  # 버퍼를 비움
                # 같지 않다면
                else:
                    # 버퍼에 저장된 수가 있다면 flush
                    if (buffer):
                        add(buffer)
                    buffer = cur  # 버퍼에 현재 수 저장
        add(buffer)
        if (dir == 0):
            line = list(line) + [0] * (N - len(line))
        else:
            line = [0] * (N - len(line)) + list(line)
        
        # print(line)

        for idx, item in enumerate(line):
            board[idx][i] = item


result = 0
for dirlist in product(range(4), repeat=5):
    board = copy.deepcopy(orig_board)
    for dir in dirlist:
        move = moveLR if dir > 1 else moveUD
        move(dir)
    result = max(max(max(x) for x in board), result)

print(result)
