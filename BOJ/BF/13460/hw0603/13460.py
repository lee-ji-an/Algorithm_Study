from itertools import product
import sys

"""
#: 벽
R: 빨간 구슬
B: 파란 구슬
.: 빈 칸
0: 구멍
"""
move = [0, 1, 2, 3] # 상, 하, 좌, 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
N, M  = map(int, sys.stdin.readline().split())
board = [[0] * M for _ in range(N)]

blue = (-1, -1) # 파란 구슬의 초기 좌표
red = (-1, -1) # 빨간 구슬의 초기 좌표
hole = (-1, -1) # 구멍의 좌표
# board 정보 입력받으면서 각 구슬의 좌표와 구멍의 좌표를 저장해 둠
for i in range(N):
    line = sys.stdin.readline().rstrip()
    for j, item in enumerate(line):
        board[i][j] = item
        if (item == "B"):
            blue = (i, j)
            board[i][j] = "."
        elif (item == "R"):
            red = (i, j)
            board[i][j] = "."
        elif (item == "O"):
            hole = (i, j)


# 현배 board 정보 출력 (테스트용)
def printboard(dir: int, r: tuple, b: tuple):
    import copy
    global board
    desc = ["상", "하", "좌", "우"]
    nboard = copy.deepcopy(board)
    nboard[r[0]][r[1]] = "R"
    nboard[b[0]][b[1]] = "B"
    print(*nboard, sep="\n")
    print(f"마지막 이동: {desc[dir]}")


# 방향에 맞게 기울이기
def tilt(dir: int, current_red: tuple, current_blue: tuple):
    global board
    red_new = current_red
    blue_new = current_blue
    
    stop_red = False
    stop_blue = False
    while (True):
        # red와 blue 좌표를 벽에 닿을 때 까지.. 또는 구멍에 빠질 때 까지 옮기기
        # B, R이 서로 맞물려서 움직일 수 없을 때도 고려해야 함

        # 더 이상 움직일 수 없다면 그 좌표 반환
        if (stop_red and stop_blue):
            return red_new, blue_new

        if not (stop_red):
            red_new = (red_new[0] + dr[dir], red_new[1] + dc[dir])
        if not (stop_blue):
            blue_new = (blue_new[0] + dr[dir], blue_new[1] + dc[dir])

        # 빨간 구슬이 구멍에 빠졌다면
        if (board[red_new[0]][red_new[1]] == "O"):
            # 빨간 구슬이 구멍에 들어간 이후에도 파란 구슬은 계속 진행하여
            # 구멍에 빠지는지 여부를 체크해야 함
            stop_red = True
        
        # 파란 구슬이 구멍에 빠졌다면
        if (board[blue_new[0]][blue_new[1]] == "O"):
            return red_new, blue_new

        # 빨간 구슬이 벽 위치라면
        if (board[red_new[0]][red_new[1]] == "#"):
            # 빨간 구슬 옮기기 취소
            red_new = (red_new[0] - dr[dir], red_new[1] - dc[dir])
            stop_red = True
            
        # 파란 구슬이 벽 위치라면
        if (board[blue_new[0]][blue_new[1]] == "#"):
            # 파란 구슬 옮기기 취소
            blue_new = (blue_new[0] - dr[dir], blue_new[1] - dc[dir])
            stop_blue = True

        
        # 이동하고 보니 두 구슬이 겹쳐서 같은 위치에 있는 경우
        # 둘 중에 하나를 실행취소 해야 하는데..
        # 상: row가 더 큰걸 취소
        # 하: row가 더 작은걸 취소
        # 좌: col이 더 큰걸 취소
        # 우: col이 더 작은걸 취소
        if (red_new == blue_new):
            # 일단 겹쳤다는건 끝까지 왔다는 소리니까 둘 다 stop
            stop_red, stop_blue = True, True
            victim = ""
            if (dir == 0):
                victim = "Red" if current_red[0] > current_blue[0] else "Blue"
            elif (dir == 1):
                victim = "Red" if current_red[0] < current_blue[0] else "Blue"
            elif (dir == 2):
                victim = "Red" if current_red[1] > current_blue[1] else "Blue"
            else:
                victim = "Red" if current_red[1] < current_blue[1] else "Blue"
            
            if (victim == "Red"):
                red_new = (red_new[0] - dr[dir], red_new[1] - dc[dir])
            else:
                blue_new = (blue_new[0] - dr[dir], blue_new[1] - dc[dir])



count_min = 11
# PI(4, 10)의 모든 경우(중복순열))
for dirlist in product(move, repeat=10):
    # 연속해서 같은 방향으로 기울이는 경우는 의미가 없으므로 skip
    if (any(i == j for i, j in zip(dirlist, dirlist[1:]))):
        continue
    
    # 구슬의 초기 위치 초기화
    r, b = red, blue
    cnt = 0
    for dir in dirlist:
        r, b = tilt(dir, r, b)
        cnt += 1

        # Blue가 빠지면 그 경우는 실패
        if (b == hole):
            break
        # Red가 빠지면 성공
        elif (r == hole):
            count_min = min(count_min, cnt)
            break

print(count_min if count_min != 11 else -1)
