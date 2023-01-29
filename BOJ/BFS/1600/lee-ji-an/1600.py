import sys
from collections import deque

input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())

board = []
visited = [[0] * W for _ in range(H)]
monkeyX = (0, 0, -1, 1)
monkeyY = (-1, 1, 0, 0)
horseX = (-2, -1, 1, 2, 2, 1, -1, -2)
horseY = (-1, -2, -2, -1, 1, 2, 2, 1)

for i in range(H):
    board.append(list(map(int, input().split())))

def bfs():
    visited = [[-1] * W for _ in range(H)]
    q = deque()
    q.append((0, 0, 0, K))
    visited[0][0] = K
    while q:
        y, x, cnt, horse = q.popleft()
        if horse >= 1:
            for i in range(8):  # 말의 이동 방향으로 옮기기
                movey = y + horseY[i]
                movex = x + horseX[i]
                if movey < 0 or movey >= H or movex < 0 or movex >= W:
                    continue
                if movey == H-1 and movex == W-1:
                    return cnt + 1
                if not board[movey][movex] and visited[movey][movex] < horse-1:
                    q.append((movey, movex, cnt+1, horse-1))
                    visited[movey][movex] = horse-1
        for i in range(4):   # 원숭이의 이동 방향으로 옮기기
            movey = y + monkeyY[i]
            movex = x + monkeyX[i]
            if movey < 0 or movey >= H or movex < 0 or movex >= W:
                continue
            if movey == H-1 and movex == W-1:
                return cnt + 1
            if not board[movey][movex] and visited[movey][movex] < horse:
                q.append((movey, movex, cnt+1, horse))
                visited[movey][movex] = horse
    return -1

if W == 1 and H == 1:
    print(0)
else:
    print(bfs())