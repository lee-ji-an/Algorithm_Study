from collections import deque
from copy import deepcopy

n = int(input())
board = [[b for b in map(int, input().split())] for _ in range(n)]
for i in range(n):
    try:
        check = [i, board[i].index(9)]
    except:
        continue

board[check[0]][check[1]] = 0       # 상어의 위치를 0으로 둠
board_ori = deepcopy(board)     # 원본 저장

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

flag, upper, size, exp, cnt = False, 999, 2, 0, 0        # 찾았다는 표시     # 먹을 수 있는 물고기까지의 최대 거리
can_eat = []        # 먹을 수 있는 물고기의 좌표
dq = deque()
dq.append([check[0], check[1], 0])

while dq:
    y, x, dist = dq.popleft()
    if dist + 1 <= upper:       # 허용 가능 거리보다 작거나 같을 때
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] > size:
                    continue
                if board[ny][nx] == 0 or board[ny][nx] == size:     # 그냥 통과만 가능
                    dq.append([ny, nx, dist + 1])
                    board[ny][nx] = 999     # 방문 표시
                elif board[ny][nx] < size:      # 먹을 수 있음
                    if not flag:        # 아직 먹을 수 있는 애가 없음
                        flag, upper = True, dist + 1     # 먹을 수 있는것을 찾음, 허용 가능 최대 거리가 됨
                    can_eat.append([ny, nx, dist + 1])        # 먹을 수 있는 물고기의 좌표를 저장, 이 물고기를 넘어서는 좌표는 탐색할 필요가 없음
                    board[ny][nx] = 999     # 방문 표시
                    
    if flag and (dist + 1 > upper or len(dq) < 1):      
    # 먹을 수 있는 물고기가 있어야 하고,
    # 허용 가능 거리를 모두 탐색했거나, 허용 가능 거리와 같음에도 방문할 곳이 없을 때
        can_eat.sort(key = lambda x : (x[0], x[1]))     # 기준에 맞게 정렬함
        y, x, dist = can_eat.pop(0)     # 가장 우선 순위에 있는 먹잇감
        dq.clear(), can_eat.clear()     # 모든 dq를 초기화 함
        dq.append([y, x, dist])     # 가장 우선 순위에 있는 먹잇감 위치부터 다시 시작함
        board_ori[y][x] = 0
        board = deepcopy(board_ori)     # board 복구
        flag, upper = False, 9999
        cnt = dist

        exp += 1
        if exp == size:     # 경험치를 채운다면
            exp = 0
            size += 1
print(cnt)