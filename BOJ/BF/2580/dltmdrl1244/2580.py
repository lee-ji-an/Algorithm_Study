import sys
input = sys.stdin.readline
board = []
blank = []
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] == 0:
            blank.append((i, j))
    board.append(tmp)

def check(y, x, num):
    for i in range(9):
        # 가로 확인
        if num == board[y][i]:
            return False
        # 세로 확인
        if num == board[i][x]:
            return False
    
    # 사각형 확인(3x3 사각형의 좌측 상단 좌표를 구함)
    sy, sx = y // 3, x // 3
    
    for i in range(3):
        for j in range(3):
            if board[sy*3+i][sx*3+j] == num:
                return False
    return True

def solve(idx):
    # 마지막 칸까지 채웠으면 board 출력
    if idx == len(blank):
        for b in board:
            print(*b)
        exit(0)
        
    y, x = blank[idx]
    
    # [y][x] = 채워야 할 칸
    # i : 채울 숫자 후보
    for i in range(1, 10):
        if check(y, x, i):
            # 백 트래킹
            board[y][x] = i
            solve(idx + 1)
            board[y][x] = 0

solve(0)