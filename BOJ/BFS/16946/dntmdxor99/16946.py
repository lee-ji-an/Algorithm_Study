from collections import deque

n, m = map(int, input().split())
board = []
dq = deque()
visited = deque()
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(n):
    t = list(map(int, list(input())))
    board.append(t)

cnt_imag = 1j       # 그룹 번호, 1이 0으로 둘러싸인 경우를 피하기 위해
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:        # 0이라면 인접한 0의 개수를 모두 찾음
            cnt = 1
            dq.append([i, j])
            visited.append([i, j])      # 방문한 0의 좌표들을 모아놓음
            board[i][j] = -1        # 방문 표시함
            while dq:
                cur_i, cur_j = dq.popleft()
                for next_dir in dir:
                    next_i = cur_i + next_dir[0]
                    next_j = cur_j + next_dir[1]
                    if 0 <= next_i < n and 0 <= next_j < m and not board[next_i][next_j]:
                        # 방문할 곳의 값이 0이라면
                        dq.append([next_i, next_j])
                        visited.append([next_i, next_j])        # 방문한 좌표
                        board[next_i][next_j] = -1      # 방문 표시
                        cnt += 1
            while visited:      # 방문한 0의 좌표를 모두 그룹 갯수로 바꿈
                v = visited.popleft()
                board[v[0]][v[1]] = cnt + cnt_imag      # 인접한 0의 개수와 그룹 번호를 따로 넣음, 0은 모두 그룹화됨
            cnt_imag += 1j      # 그룹 번호 변경

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            for next_dir in dir:
                next_i = i + next_dir[0]
                next_j = j + next_dir[1]
                if 0 <= next_i < n and 0 <= next_j < m:
                    if imag := board[next_i][next_j].imag:      # 인접한 애들의 그룹 번호이 있다면
                        if imag not in visited:
                            visited.append(imag)        # 해당 그룹은 두 번 이상 더할 필요가 없음
                            board[i][j] += int(board[next_i][next_j].real)      # 근처에 있는 0의 개수를 더함
            visited.clear()
            board[i][j] %= 10

board = list(map(lambda x: 0 if x.imag > 0 else x, board[i]) for i in range(n))     # 그룹이 있다면 0이므로 0으로 바꿈

for i in board:
    print(*i, sep='')