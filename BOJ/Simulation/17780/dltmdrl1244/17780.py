import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
color = [[2 for _ in range(n+2)]]
for _ in range(n):
    color.append([2] + list(map(int, input().split())) + [2])
color.append([2 for _ in range(n+2)])

board = [[deque() for _ in range(n+2)] for _ in range(n+2)]
marker = []
dir = []
for i in range(k):
    y, x, d = map(int, input().split())
    board[y][x].append(i)
    marker.append([y, x])
    dir.append(d - 1)

def opposite(k):
    if k == 0:
        return 1
    elif k == 1:
        return 0
    elif k == 2:
        return 3
    else:
        return 2

# idx 번째 marker를 이동시킴
def move(idx):
    tmp = deque()
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    y, x = marker[idx]
    d = dir[idx]
    
    ny, nx = y + dy[d], x + dx[d]
    
    if color[ny][nx] == 0: # 흰색
        # 현재 board의 모든 말을 순서를 유지한 채(pop -> appendleft) tmp로 이동시킴
        while board[y][x]:
            popped = board[y][x].pop()
            tmp.appendleft(popped)
            # 각 marker의 현재 위치 갱신
            marker[popped] = [ny, nx]
        # tmp를 이동할 위치에 이어 붙임
        board[ny][nx] += tmp
        
        if len(board[ny][nx]) >= 4:
            return True
                   
    elif color[ny][nx] == 1: # 빨간색
        # 현재 board의 모든 말을 순서를 반전시킨 채(pop -> append) tmp로 이동시킴
        while board[y][x]:
            popped = board[y][x].pop()
            tmp.append(popped)
            marker[popped] = [ny, nx]
        board[ny][nx] += tmp
        
        if len(board[ny][nx]) >= 4:
            return True
        
    else: # 파란색
        # 일단 방향을 바꿈
        dir[idx] = opposite(d)
        nny, nnx = y + dy[opposite(d)], x + dx[opposite(d)]
        # 바꾼 방향의 칸이 파란색이 아니면 이동
        if color[nny][nnx] != 2:
            return move(idx)
            
    return False
        
# move_marker: 모든 marker를 이동, 단 각 칸의 맨 아래에 있지 않은 marker는 이동하지 않음
def move_marker():
    for i in range(k):
        my, mx = marker[i]
        if board[my][mx].index(i) == 0:
            if move(i):
                return True

# 턴이 지날 때마다 turn 1씩 증가
turn = 1
while True:
    if turn > 1000:
        print(-1)
        break
    
    if move_marker():
        print(turn)
        break
    
    turn += 1   