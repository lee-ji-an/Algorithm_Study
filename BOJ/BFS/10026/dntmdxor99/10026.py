from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
check = [[[0] * n for _ in range(n)] for _ in range(2)]  # False -> 적록색약, True -> 정상인
group = [0, 0]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

count = 0
dq = deque()
for y in range(n):
    for x in range(n):
        color = board[y][x]
        for flag in [False, True]:      # 적록색약과 정상인을 판단함
            if not check[flag][y][x]:     # 탐색할 필요가 있는 좌표
                group[flag] += 1        # 그룹 번호
                check[flag][y][x] = group[flag]     # 그룹 번호를 부여함
                dq.append([y, x])
                while dq:       # y, x의 색과 같은 색을 하나로 묶음
                    cy, cx = dq.popleft()
                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if not (0 <= ny < n and 0 <= nx < n): continue      # 범위를 벗어남
                        if check[flag][ny][nx] >= 1: continue       # 재방문일 경우
                        ncolor = board[ny][nx]      # 이웃한 색깔을 찾음
                        if color == ncolor:     # 색이 같다면
                            dq.append([ny, nx])
                            check[flag][ny][nx] = group[flag]       # 그룹 번호 부여함
                        else:
                            if not flag and ((color == 'R' and ncolor == 'G') or (color == 'G' and ncolor == 'R')):
                                # 적록색약의 조건
                                dq.append([ny, nx])
                                check[flag][ny][nx] = group[flag]       # 그룹 번호 부여함

print(group[1], group[0])       # 그룹 개수를 출력함
