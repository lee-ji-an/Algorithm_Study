from collections import deque

F, S, G, U, D = map(int, input().split())
if S == G: print(0), exit(0)        # 현재 층과 목적지가 같다면 끝
board = [*range(0, F + 1)]
board[S] = 0
dy = [U, -D]        # U만큼 위로 가거나, D만큼 아래로 가는 것
dq = deque([[S, 0]])
while dq:
    y, cnt = dq.popleft()
    for i in range(2):
        ny = y + dy[i]
        if ny < 1 or ny > F or board[ny] == 0:      # 범위를 벗어나거나, 이미 방문한 층이라면
            continue
        if ny == G:     # 목적지에 도착했다면
            print(cnt + 1), exit(0)
        dq.append([ny, cnt + 1])
        board[ny] = 0       # 방문 표시
print("use the stairs")