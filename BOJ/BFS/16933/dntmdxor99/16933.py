from collections import deque

n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]
check = [[k + 1 for _ in range(m)] for _ in range(n)]       # 최대로 부술 수 있는 횟수로 채워 넣음
check[0][0] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dq = deque()
dq.append([0, 0, 0])
cnt = 1
day = True      # 낮

while dq:
    for _ in range(len(dq)):        # 이중 루프를 하면 한 칸 간 것과 같음 (!)
        y, x, w = dq.popleft()

        if y == n - 1 and x == m - 1:
            print(cnt)      # 찾았다면 현재의 cnt 값으로 출력함
            exit(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and check[ny][nx] > w:
            # 벽이 아닌 경우 낮이든 밤이든 이동이 가능함
            # 현재 내가 부순 벽의 개수가 더 적을 때
                if board[ny][nx] == '0':
                    dq.append([ny, nx, w])
                    check[ny][nx] = w       # 이동했다면 지금까지 부순 벽의 개수로 변경함
                # 벽인 경우
                elif w < k:     # 지금까지 부순 벽이 최댓값보다 작다면
                    if not day:  # 밤
                        dq.append([y, x, w])        # 그냥 기다림, 기다려도 cnt는 추가됨
                    else:
                        check[ny][nx] = w
                        dq.append([ny, nx, w + 1])      # 부수고 감
    cnt += 1        # inner 루프가 끝나면 한 발자국 걸어간 것
    day = not day       # 낮이면 밤으로, 혹은 그 반대
print(-1)
