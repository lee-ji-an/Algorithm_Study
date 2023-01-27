from collections import deque

board = [[[b for b in input()] for _ in range(8)]]

rank = 8
for i in range(8):
    if '#' in board[0][i]:
        rank = i
        break

rank = 8 - rank
# 맨위에 있는 벽과 가장 아래까지 거리를 구함
# 따라서 해당 거리만큼만 벽이 내려가면 됨

for i in range(0, rank):        # 벽을 아래로 내려서 다른 board에 추가함
    new = [['.' for _ in range(8)] for _ in range(8)]
    for j in range(1, 8):
        new[j] = board[i][j - 1].copy()
    board.append(new)

dq = deque()
dq.append([0, 7, 0])

# 맨 위부터 시계 방향
dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
        
while dq:
    i, y, x = dq.popleft()      # i는 board들의 인덱스
    for j in range(9):
        ny, nx = y + dy[j], x + dx[j]
        if i >= rank:       # i가 rank와 같거나 크다는 뜻은 벽이 다 내려가도 살았다는 뜻임
            print(1)
            exit(0)
        elif 0 <= ny < 8 and 0 <= nx < 8 and board[i][ny][nx] != '#' and board[i + 1][ny][nx] != '#':
            # 이동할 위치가 현재 보드에서 벽이 아니어야 하고, 다음 보드에서도 벽이 아니어야 함
            dq.append([i + 1, ny, nx])      # 살았으므로 다음 board로 넘어감
print(0)