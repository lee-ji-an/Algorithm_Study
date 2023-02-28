import sys
from collections import deque
input = sys.stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
visited = set()

N, M = map(int, input().split())

board = []
coin = []
for i in range(N):
    row = input().rstrip()
    board.append(row)
    for j in range(M):
        if row[j] == 'o':
            coin.append(i)  # coin 위치 저장
            coin.append(j)


def bfs(y1, x1, y2, x2):
    q = deque()
    q.append((y1, x1, y2, x2, 0))
    visited.add((y1, x1, y2, x2))

    for _ in range(10):
        for _ in range(len(q)):
            y1, x1, y2, x2, cnt = q.popleft()
            for i in range(4):
                # 방향대로 한 칸씩 옮겼을 때 좌표를 저장
                movey1, movex1, movey2, movex2 = y1 + dy[i], x1 + dx[i], y2 + dy[i], x2 + dx[i]

                # 떨어진 동전의 갯수를 체크
                fall = 0
                if not (0 <= movey1 < N) or not (0 <= movex1 < M):
                    fall += 1
                if not (0 <= movey2 < N) or not (0 <= movex2 < M):
                    fall += 1
                if fall == 1:  # 하나만 떨어졌을 때
                    return cnt + 1
                elif fall == 2:  # 둘 다 떨어졌을 때
                    continue

                # 옮길 위치가 벽이라면 다시 원상복귀
                if board[y1 + dy[i]][x1 + dx[i]] == '#':
                    movey1 = y1
                    movex1 = x1
                if board[y2 + dy[i]][x2 + dx[i]] == '#':
                    movey2 = y2
                    movex2 = x2
                if (movey1, movex1, movey2, movex2) not in visited:
                    q.append((movey1, movex1, movey2, movex2, cnt + 1))
                    visited.add((movey1, movex1, movey2, movex2))

    return -1


print(bfs(coin[0], coin[1], coin[2], coin[3]))